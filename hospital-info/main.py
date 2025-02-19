import os
import aiogram
import asyncio

from app.handlers import router
from dotenv import load_dotenv, find_dotenv


async def main() -> None:
    load_dotenv(find_dotenv())

    token = os.getenv("TOKEN")

    bot = aiogram.Bot(token=token)
    dp = aiogram.Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped.")