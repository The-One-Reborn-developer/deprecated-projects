import { useNavigate } from "react-router-dom";
import { MouseEvent } from "react";

import Button from "react-bootstrap/Button";

import "../scss/reset.scss";
import "../scss/menu.scss";

function Menu() {
  const navigate = useNavigate();

  const handleButtonClick = (event: MouseEvent<HTMLButtonElement>) => {
    if (event.currentTarget.id === "start-button") {
      navigate("/waiting-room");
    } else if (event.currentTarget.id === "transactions-history-button") {
      navigate("/transactions-history");
    } else if (event.currentTarget.id === "rules-button") {
      navigate("/rules");
    } else if (event.currentTarget.id === "settings-button") {
      navigate("/settings");
    }
  };

  return (
    <>
      <div className="container">
        <div className="btn-group" role="group">
          <Button
            id="start-button"
            className="btn-menu"
            onClick={handleButtonClick}
          >
            Начать игру
          </Button>
          <Button
            id="transactions-history-button"
            className="btn-menu"
            onClick={handleButtonClick}
            disabled
          >
            История платежей
          </Button>
          <Button
            id="rules-button"
            className="btn-menu"
            onClick={handleButtonClick}
            disabled
          >
            Правила
          </Button>
          <Button
            id="settings-button"
            className="btn-menu"
            onClick={handleButtonClick}
            disabled
          >
            Настройки
          </Button>
        </div>
      </div>
    </>
  );
}

export default Menu;
