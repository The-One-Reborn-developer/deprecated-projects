import crypto from "crypto";

interface validateTelegramDataResult {
  status: number;
  message: string | { [key: string]: any };
  isValid: boolean;
}

export function validateTelegramData(
  telegramData: string
): validateTelegramDataResult {
  if (typeof telegramData !== "string" || !telegramData) {
    return {
      status: 400,
      message: "Invalid Telegram data",
      isValid: false,
    };
  }

  // Decode and parse user data
  const userDataString = new URLSearchParams(telegramData).get("user");
  if (!userDataString) {
    return {
      status: 400,
      message: "Invalid user data",
      isValid: false,
    };
  }

  const userData = JSON.parse(decodeURIComponent(userDataString));
  if (typeof userData.id !== "number") {
    return {
      status: 400,
      message: "Invalid user ID",
      isValid: false,
    };
  }

  // Check environment variable
  const botToken = process.env.TELEGRAM_BOT_TOKEN;
  if (!botToken) {
    console.error("TELEGRAM_BOT_TOKEN is not set.");
    return {
      status: 500,
      message: "TELEGRAM_BOT_TOKEN is not set.",
      isValid: false,
    };
  }

  // Compute secret key
  const secretKey = crypto
    .createHmac("sha256", "WebAppData")
    .update(botToken)
    .digest();

  // Create data check string
  const dataCheckString = telegramData
    .split("&")
    .filter((pair) => pair.split("=")[0] !== "hash") // Exclude hash
    .sort()
    .map(
      (pair) =>
        pair.split("=")[0] + "=" + decodeURIComponent(pair.split("=")[1])
    )
    .join("\n"); // Format as key=value\n

  // Compute hash
  const computedHash = crypto
    .createHmac("sha256", secretKey)
    .update(dataCheckString)
    .digest("hex");

  // Compare hashes
  const receivedHash = new URLSearchParams(telegramData).get("hash");
  if (!receivedHash || computedHash !== receivedHash) {
    return {
      status: 400,
      message: "Invalid hash",
      isValid: false,
    };
  }

  // Check timestamp
  const authDateString = new URLSearchParams(telegramData).get("auth_date");
  if (!authDateString) {
    return {
      status: 400,
      message: "Invalid auth date",
      isValid: false,
    };
  }

  const authDate = parseInt(authDateString, 10);
  const now = Math.floor(Date.now() / 1000);
  if (now - authDate > 86400) {
    // 24 hours
    return {
      status: 400,
      message: "Telegram data is expired",
      isValid: false,
    };
  }

  const urlEncodedValidatedTelegramData = new URLSearchParams(telegramData);
  const validatedTelegramDataObject: { [key: string]: string } = {};
  urlEncodedValidatedTelegramData.forEach((value, key) => {
    validatedTelegramDataObject[key] = value;
  });
  return {
    status: 200,
    message: validatedTelegramDataObject,
    isValid: true,
  };
}
