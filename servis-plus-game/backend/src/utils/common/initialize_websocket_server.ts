import { WebSocketServer, WebSocket } from "ws";
import { IncomingMessage, Server } from "http";
import { createClient } from "redis";

export function initializeWebsocketServer(server: Server) {
  const wss = new WebSocketServer({ server });

  const redisClient = createClient({
    url: "redis://redis:6379",
  });
  redisClient.connect().catch((error) => {
    console.error(`Error connecting to Redis: ${error}`);
  });

  const users: Map<string, WebSocket> = new Map();
  let countdownInterval: NodeJS.Timer | null = null;
  let countdownTime = 60;

  wss.on("connection", (ws: WebSocket, req: IncomingMessage) => {
    if (!req.url) {
      ws.close(1008, "Missing URL");
      return;
    }
    const params = new URLSearchParams(req.url.split("?")[1]);
    const telegramID = String(params.get("telegram_id"));

    if (!telegramID) {
      ws.close(1008, "Missing Telegram ID");
      return;
    }

    if (users.has(telegramID)) {
      console.warn(
        `Duplicate connection for Telegram ID ${telegramID}. Closing.`
      );
      users.get(telegramID)?.close(1008, "Duplicate connection");
    }

    users.set(telegramID, ws);
    console.log(`WebSocket connected for Telegram ID ${telegramID}`);

    ws.on("message", async (rawMessage: string) => {
      try {
        console.log(
          `Received message from Telegram ID ${telegramID}: ${rawMessage}`
        );
        const message = JSON.parse(rawMessage);

        if (
          message.type === "waiting_room" &&
          message.message === "player_joined"
        ) {
          console.log(
            `Player with Telegram ID ${telegramID} joined waiting room`
          );
          await redisClient.sAdd("waiting_room", telegramID);
          console.log(
            `Player with Telegram ID ${telegramID} added to waiting room`
          );
        }
      } catch (error) {
        console.error(
          `Error parsing message from Telegram ID ${telegramID}: ${error}`
        );
        ws.send(JSON.stringify({ error: "Failed to parse message" }));
      }
    });

    // Handle disconnections
    ws.on("close", (code: number, reason: Buffer) => {
      users.delete(telegramID);
      console.log(
        `WebSocket closed for Telegram ID ${telegramID}. Code: ${code}, Reason: ${reason}`
      );
      try {
        redisClient.sRem("waiting_room", telegramID);
      } catch (error) {
        console.error(
          `Error removing Telegram ID ${telegramID} from waiting room: ${error}`
        );
      }
    });

    // Handle errors
    ws.on("error", (error) => {
      console.error(
        `WebSocket error for Telegram ID ${telegramID}: ${error.message}`
      );
    });
  });

  function sendMessageToUser(recipientTelegramIDString: string, message: any) {
    const user = users.get(recipientTelegramIDString);
    if (user) {
      user.send(JSON.stringify(message));
    } else {
      console.error(
        `User with Telegram ID ${recipientTelegramIDString} is not connected.`
      );
    }
  }

  let isGameRunning = false;

  if (!countdownInterval) {
    countdownInterval = setInterval(async () => {
      if (isGameRunning) {
        return;
      }

      if (countdownTime > 0) {
        countdownTime--;

        const players = await redisClient.sMembers("waiting_room");
        players.forEach((telegramID) => {
          const ws = users.get(telegramID);
          if (ws && ws.readyState === WebSocket.OPEN) {
            ws.send(
              JSON.stringify({
                type: "timer_update",
                time_left: countdownTime,
              })
            );
          }
        });
      } else {
        countdownTime = 60;
        console.log("Countdown complete and reset to 60 seconds.");

        const players = await redisClient.sMembers("waiting_room");

        if (players.length > 1) {
          isGameRunning = true;
          const shuffledPlayers = players.sort(() => 0.5 - Math.random());

          const pairs = [];
          for (let i = 0; i < shuffledPlayers.length; i += 2) {
            if (shuffledPlayers[i + 1]) {
              pairs.push([shuffledPlayers[i], shuffledPlayers[i + 1]]);
            } else {
              await redisClient.sAdd("waiting_room", shuffledPlayers[i]);
            }
          }

          for (const [player1, player2] of pairs) {
            await redisClient.sRem("waiting_room", [player1, player2]);

            const ws1 = users.get(player1);
            const ws2 = users.get(player2);

            if (ws1 && ws1.readyState === WebSocket.OPEN) {
              ws1.send(
                JSON.stringify({
                  type: "pair_created",
                  pair_with: player2,
                })
              );
            }

            if (ws2 && ws2.readyState === WebSocket.OPEN) {
              ws2.send(
                JSON.stringify({
                  type: "pair_created",
                  pair_with: player1,
                })
              );
            }

            console.log(`Paired ${player1} with ${player2}`);
          }
        }

        // Notify remaining players
        const remainingPlayers = await redisClient.sMembers("waiting_room");
        remainingPlayers.forEach((telegramID) => {
          const ws = users.get(telegramID);
          if (ws && ws.readyState === WebSocket.OPEN) {
            ws.send(
              JSON.stringify({
                type: "waiting",
                message: "Waiting for another player to join",
              })
            );
          }
        });
      }
    }, 1000);
  }

  return { sendMessageToUser };
}
