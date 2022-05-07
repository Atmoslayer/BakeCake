from aiogram import types, Dispatcher


async def echo_send(message : types.Message):
    if message.text == 'Привет':
        await message.answer('И тебе привет!')


def register_handlers_other(dispatcher : Dispatcher):
    dispatcher.register_message_handler(echo_send)
