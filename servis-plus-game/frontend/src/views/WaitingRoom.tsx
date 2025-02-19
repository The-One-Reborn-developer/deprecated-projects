import { useNavigate } from "react-router-dom";
import { MouseEvent, useEffect, useState } from "react";

import { useWebsocket } from "../contexts/websocket";
import SubtitleHeader from "../components/SubtitleHeader";
import Button from "react-bootstrap/Button";

import "../scss/waiting_room.scss";

function WaitingRoom() {
  const navigate = useNavigate();
  const { socket } = useWebsocket();
  const [timeLeft, setTimeLeft] = useState(60);

  useEffect(() => {
    if (socket) {
      socket.onmessage = (event) => {
        const data = JSON.parse(event.data);

        if (data.type === "timer_update") {
          setTimeLeft(data.time_left);
        } else if (data.type === "timer_reset") {
          setTimeLeft(data.time_left);
        }
      };

      if (socket.readyState === WebSocket.OPEN) {
        const payload = {
          type: "waiting_room",
          message: "player_joined",
        };
        socket.send(JSON.stringify(payload));
      }
    }

    return () => {
      if (socket) {
        socket.onmessage = null;
      }
    };
  }, [socket]);

  const formatTime = (seconds: number) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return `${hours} час ${hours !== 1 ? "a" : ""} ${minutes} минут${
      minutes !== 1 ? "ы" : ""
    } ${secs} секунд${secs !== 1 ? "ы" : ""}`;
  };

  const handleButtonClick = (event: MouseEvent<HTMLButtonElement>) => {
    if (event.currentTarget.id === "cancel-button") {
      navigate("/menu");
    }
  };

  return (
    <div className="container">
      <div className="content">
        <SubtitleHeader
          text={`Следующая игра начнётся через ${formatTime(timeLeft)}`}
        />
        <Button
          id="cancel-button"
          className="btn-waiting-room"
          onClick={handleButtonClick}
        >
          Отмена
        </Button>
      </div>
    </div>
  );
}

export default WaitingRoom;
