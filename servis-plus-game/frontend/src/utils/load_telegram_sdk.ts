export const loadTelegramSDK = (): Promise<void> => {
  return new Promise((resolve, reject) => {
    if (document.getElementById("telegram-web-app-sdk")) {
      resolve();
      return;
    }

    const script = document.createElement("script");
    script.src = "https://telegram.org/js/telegram-web-app.js?56";
    script.id = "telegram-web-app-sdk";
    script.onload = () => resolve();
    script.onerror = () => reject(new Error("Failed to load Telegram SDK"));
    document.body.appendChild(script);
  });
};
