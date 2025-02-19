import os

from dotenv import load_dotenv, find_dotenv

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo


def webapp_keyboard() -> InlineKeyboardMarkup:
    load_dotenv(find_dotenv())

    app_instance = os.getenv('APP_INSTANCE')

    if app_instance == 'demo':
        return InlineKeyboardMarkup(
            inline_keyboard = [
                [
                    InlineKeyboardButton(text=f'Открыть приложение 📱',
                                        web_app=WebAppInfo(url=''))
                ]
            ]
        )
    elif app_instance == 'dev':
        return InlineKeyboardMarkup(
            inline_keyboard = [
                [
                    InlineKeyboardButton(text=f'Открыть приложение 📱',
                                        web_app=WebAppInfo(url='https://servisplus-game-dev.mooo.com:12443/'))
                ]
            ]
        )
    elif app_instance == 'prod':
        return InlineKeyboardMarkup(
            inline_keyboard = [
                [
                    InlineKeyboardButton(text=f'Открыть приложение 📱',
                                        web_app=WebAppInfo(url=''))
                ]
            ]
        )
