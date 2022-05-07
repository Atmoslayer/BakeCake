from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

history_button = KeyboardButton('/История_заказов')
order_button = KeyboardButton('/Собрать_торт')

keyboard_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

keyboard_client.row(history_button, order_button)