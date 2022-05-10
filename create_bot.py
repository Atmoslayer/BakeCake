from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from dotenv import load_dotenv
import os


load_dotenv()
token_bot = os.getenv('TOKEN_BOT')
yoo_token = os.getenv('YOO_TOKEN')

storage = MemoryStorage()

bot = Bot(token=token_bot)
dispatcher = Dispatcher(bot, storage=storage)