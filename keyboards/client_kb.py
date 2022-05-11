from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

history_button = KeyboardButton('История заказов')
order_button = KeyboardButton('Собрать торт')

keyboard_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

keyboard_client.row(order_button, history_button)