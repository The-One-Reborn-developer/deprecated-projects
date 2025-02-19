declare global {
  interface Window {
    Telegram: {
      WebApp: {
        initData: string;
        initDataUnsafe: any;
        [key: string]: any; // Extend with other properties as needed
      };
    };
  }
}

export {};
