import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import { loadTelegramSDK } from "./utils/load_telegram_sdk";
import { WebsocketProvider } from "./contexts/websocket";

import Intro from "./views/Intro";
import Menu from "./views/Menu";
import WaitingRoom from "./views/WaitingRoom";
import Loser from "./views/Loser";
import Ad from "./views/Ad";
import Round from "./views/Round";

function App() {
  const [telegramID, setTelegramID] = useState<number | null>(null);

  useEffect(() => {
    const initializeTelegramSDK = async () => {
      try {
        await loadTelegramSDK();
        const initData = window.Telegram.WebApp.initData;
        const initDataParams = new URLSearchParams(initData);
        const initDataObject: { [key: string]: string } = {};
        initDataParams.forEach((value, key) => {
          initDataObject[key] = value;
        });
        const validateInitData = async () => {
          try {
            const response = await fetch("/api/common/validate-init-data", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(initDataObject),
            });

            const status = response.status;
            const result = await response.json();

            if (result && status === 200) {
              const dataString = result.data;
              const data = JSON.parse(dataString);
              const telegramID = parseInt(data.telegram_id);
              setTelegramID(telegramID);
            }
          } catch (error) {
            console.error(`Error validating init data: ${error}`);
          }
        };

        await validateInitData();
      } catch (error) {
        console.error(`Error initializing Telegram SDK: ${error}`);
      }
    };

    initializeTelegramSDK();
  }, []);

  if (telegramID === null) {
    return <div>Загрузка...</div>;
  }

  return (
    <WebsocketProvider telegramID={telegramID}>
      <Router>
        <Routes>
          <Route path="/" element={<Intro />} />
          <Route path="/menu" element={<Menu />} />
          <Route path="/waiting-room" element={<WaitingRoom />} />
          <Route path="/loser" element={<Loser />} />
          <Route path="/ad" element={<Ad />} />
          <Route path="/round" element={<Round />} />
        </Routes>
      </Router>
    </WebsocketProvider>
  );
}

export default App;
