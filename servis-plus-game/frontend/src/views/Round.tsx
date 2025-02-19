import SubtitleHeader from "../components/SubtitleHeader";
import UserBox from "../components/UserBox";

import Button from "react-bootstrap/Button";

function Round() {
  return (
    <div>
      <div className="user-box">
        <UserBox username="username" />
        <span>Против</span>
        <UserBox username="username" />
      </div>
      <div className="btn-group" role="group">
        <Button id="first-choice-button">Ответ 1</Button>
        <Button id="second-choice-button">Ответ 2</Button>
      </div>
      <SubtitleHeader text="До конца раунда осталось 0 секунд" />
    </div>
  );
}

export default Round;
