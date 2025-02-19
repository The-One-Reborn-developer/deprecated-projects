export function constructWebSocketURL(telegramID: string) {
  const queryParameters = new URLSearchParams({
    telegram_id: telegramID,
  });

  return `wss://${window.location.host}/ws/?${queryParameters.toString()}`;
}
