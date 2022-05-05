from aiogram import types, Dispatcher
from keyboards import keyboard_client


async def command_start(message: types.Message):
    await message.answer('Собери сой торт сам!', reply_markup=keyboard_client)


async def command_history(message: types.Message):
    await message.answer('Здесь будет история заказов клиента')


async def command_order(message: types.Message):
    await message.answer('Логика сборки и заказа торта')


def register_handlers_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(command_start, commands=['start', 'help'])
    dispatcher.register_message_handler(command_history, commands=['История_заказов'])
    dispatcher.register_message_handler(command_order, commands=['Собрать_торт'])