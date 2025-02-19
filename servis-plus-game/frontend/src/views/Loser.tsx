import TitleHeader from "../components/TitleHeader";
import SubtitleHeader from "../components/SubtitleHeader";

function Loser() {
  return (
    <div>
      <TitleHeader text="Вы проиграли" />
      <SubtitleHeader text="Следующая игра начнётся через 0 часов 0 минут 0 секунд" />
    </div>
  );
}

export default Loser;
