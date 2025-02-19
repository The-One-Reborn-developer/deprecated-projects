import { constructWebSocketURL } from "./construct_websocket_url";

const MAX_RECONNECT_ATTEMPTS = 5;
const RECONNECT_BASE_DELAY = 5000; // 5 seconds
let SHOULD_RECONNECT = true;
let RECONNECT_ATTEMPTS = 0;

export function initializeWebSocket(
  validatedTelegramID: number,
  onMessage?: (data: any) => void
): WebSocket | null {
  if (!validatedTelegramID) {
    console.error("Telegram ID not found, unable to initialize WebSocket");
    return null;
  } else if (RECONNECT_ATTEMPTS >= MAX_RECONNECT_ATTEMPTS) {
    console.error(
      "Maximum reconnect attempts reached, unable to initialize WebSocket"
    );
    return null;
  } else {
    try {
      const validatedTelegramIDString = validatedTelegramID.toString();
      const socket = new WebSocket(
        constructWebSocketURL(validatedTelegramIDString)
      );
      socket.addEventListener("open", () => {
        console.log(
          `WebSocket connection established for Telegram ID: ${validatedTelegramID}`
        );
        RECONNECT_ATTEMPTS = 0;
      });

      socket.addEventListener("close", () => {
        if (SHOULD_RECONNECT) {
          RECONNECT_ATTEMPTS++;
          const delay =
            RECONNECT_BASE_DELAY * Math.pow(2, RECONNECT_ATTEMPTS - 1); // Exponential backoff
          setTimeout(
            () => initializeWebSocket(validatedTelegramID),
            Math.min(delay, 60000)
          ); // Limit to 1 minute
        }
      });

      socket.addEventListener("error", (error) => {
        console.error(
          `WebSocket error for Telegram ID ${validatedTelegramID}: ${error}`
        );
      });

      socket.addEventListener("message", (event) => {
        try {
          const messageData = JSON.parse(event.data);
          console.log(`Received message: ${JSON.stringify(messageData)}`);
          if (onMessage) {
            onMessage(messageData);
          }
        } catch (error) {
          console.error(`Error parsing message data: ${error}`);
        }
      });

      return socket;
    } catch (error) {
      console.error(`Error initializing WebSocket: ${error}`);
      return null;
    }
  }
}
