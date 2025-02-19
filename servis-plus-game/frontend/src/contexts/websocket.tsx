import { createContext, useContext, useState, useEffect } from "react";
import { initializeWebSocket } from "../utils/initialize_websocket";

interface WebsocketContextProps {
  socket: WebSocket | null;
}

const WebsocketContext = createContext<WebsocketContextProps | undefined>(
  undefined
);

export const WebsocketProvider: React.FC<{
  telegramID: number;
  children: React.ReactNode;
}> = ({ telegramID, children }) => {
  const [socket, setSocket] = useState<WebSocket | null>(null);

  useEffect(() => {
    let newSocket: WebSocket | null = null;
    if (telegramID) {
      newSocket = initializeWebSocket(telegramID);
      setSocket(newSocket);
    } else {
      setSocket(null);
    }

    return () => {
      if (newSocket) {
        newSocket.close();
      }
    };
  }, [telegramID]);

  return (
    <WebsocketContext.Provider value={{ socket }}>
      {children}
    </WebsocketContext.Provider>
  );
};

export const useWebsocket = () => {
  const context = useContext(WebsocketContext);
  if (!context) {
    throw new Error("useWebsocket must be used within a WebsocketProvider");
  }
  return context;
};
