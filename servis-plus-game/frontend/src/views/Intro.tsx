import { useNavigate } from "react-router-dom";
import { ChangeEvent } from "react";

import TitleHeader from "../components/TitleHeader";
import SubtitleHeader from "../components/SubtitleHeader";
import CheckboxWithLabel from "../components/CheckboxWithLabel";

import "../scss/reset.scss";
import "../scss/intro.scss";

function Intro() {
  const navigate = useNavigate();

  const handleCheckboxChange = (event: ChangeEvent<HTMLInputElement>) => {
    if (event.target.checked) {
      navigate("/menu");
    }
  };

  return (
    <div className="container">
      <div className="content">
        <TitleHeader text="Иллюзиум" />
        <SubtitleHeader text="Краткое описание" />
        <div className="checkbox">
          <CheckboxWithLabel
            text="С правилами игры ознакомлен"
            onChange={handleCheckboxChange}
          />
        </div>
      </div>
    </div>
  );
}

export default Intro;
