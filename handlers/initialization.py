import asyncio

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import dispatcher, bot
from functions import get_user_data_async, get_order_data_async, create_or_update_user_async

user_info = {'first_name': '',
             'last_name': '',
             'username': '',
             'id': '',
             'phone_number': ''}

menu = ''

username = ''


class Initialization(StatesGroup):
    waiting_for_check_user = State()
    waiting_for_enter_name = State()
    waiting_for_confirm_name = State()
    waiting_for_enter_contact = State()
    waiting_for_confirm_contact = State()


@dispatcher.message_handler(commands='start')
# Здесь стартует приём сообщений от пользователя
async def check_user(message: types.Message, state: FSMContext):
    user_id = message.from_user.username
    user_info = await get_user_data_async(user_id)  #Здесь вызывается функция для получения данных о пользователе
    if user_info: #Если данные есть, говорим, что они есть и сразу переходим к процессу сборки торта
        button_start_order = KeyboardButton('Собрать торт')
        button_check_orders = KeyboardButton('История заказов')
        global menu
        menu = ReplyKeyboardMarkup(resize_keyboard=True)
        menu.add(button_start_order, button_check_orders)
        await bot.send_message(message.from_user.id, text='Вы уже зарегистрированы', reply_markup=menu)
        print(user_info)
        await state.finish()
        result = await get_order_data_async(1)
        print(result)
    else: #Если данных нет, идём по процессу регистрации
        await Initialization.waiting_for_check_user.set()


@dispatcher.message_handler(state=Initialization.waiting_for_check_user)
async def get_name(message: types.Message):
    global user_info
    global username
    username = message.from_user.username
    user_info['first_name'] = message.from_user.first_name
    user_info['last_name'] = message.from_user.last_name
    user_info['username'] = message.from_user.username
    user_info['id'] = message.from_user.id
    keyboard_markup = types.InlineKeyboardMarkup()
    user_agree_button = types.InlineKeyboardButton('Да, моё', callback_data='1')
    user_disagree_button = types.InlineKeyboardButton('Нет, ввести имя', callback_data='2')
    keyboard_markup.row(user_agree_button, user_disagree_button)
    await Initialization.waiting_for_enter_name.set()
    await message.answer(f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}! Это Ваше имя?', reply_markup=keyboard_markup)


@dispatcher.callback_query_handler(text='1', state=Initialization.waiting_for_enter_name)
async def confirm_name(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    keyboard_markup = types.InlineKeyboardMarkup()
    user_agree_button = types.InlineKeyboardButton('Хорошо', callback_data='get_number')
    keyboard_markup.row(user_agree_button)
    await bot.send_message(chat_id=call.from_user.id,  text='Далее потребуется указать ваш номер телефона', reply_markup=keyboard_markup)
    await Initialization.waiting_for_enter_contact.set()


@dispatcher.callback_query_handler(text='2', state=Initialization.waiting_for_enter_name)
async def ask_name(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.send_message(chat_id=call.from_user.id,  text='Введите своё имя и фамилию')
    await Initialization.waiting_for_confirm_name.set()


@dispatcher.message_handler(state=Initialization.waiting_for_confirm_name)
async def read_name(message: types.Message):
    global user_info
    user_enter = message.text
    user_full_name = user_enter.split()
    user_info['first_name'] = user_full_name[0]
    user_info['last_name'] = user_full_name[1]
    keyboard_markup = types.InlineKeyboardMarkup()
    user_agree_button = types.InlineKeyboardButton('Хорошо', callback_data='get_number')
    keyboard_markup.row(user_agree_button)
    await message.answer('Далее потребуется указать ваш номер телефона', reply_markup=keyboard_markup)
    await Initialization.waiting_for_enter_contact.set()


@dispatcher.callback_query_handler(text='get_number', state=Initialization.waiting_for_enter_contact)
async def get_contact(message: types.Message):
    markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Поделиться контактом ', request_contact=True))
    await bot.send_message(message.from_user.id, text='Пожалуйста, поделитесь своим номером телефона', reply_markup=markup_request)
    await Initialization.waiting_for_confirm_contact.set()


@dispatcher.message_handler(content_types='contact', state=Initialization.waiting_for_confirm_contact)
async def confirm_contact(message: types.Message, state: FSMContext):

    user_info['phone_number'] = str(message.contact.phone_number)

    button_start_order = KeyboardButton('Собрать торт')
    button_check_orders = KeyboardButton('История заказов')
    global menu
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(button_start_order, button_check_orders)

    await bot.send_message(message.from_user.id, text='Спасибо, регистрация пройдена', reply_markup=menu)

    print(user_info) #К этому моменту собрана вся информация о пользователе, здесь в БД можно сохранять всё, что касается регистрации 
    await create_or_update_user_async(user_info)
    await state.finish()


# defegister_handlers_food(dp: dispatcher):
# #     dp.register_message_handler(get_name, commands='registration', state="*")
# #     dp.register_message_handler(confirm_name, state=Initialization.waiting_for_enter_name)
# #     dp.register_message_handler(ask_name, state=Initialization.waiting_for_confirm_name)
# #     dp.register_message_handler(read_name, state=Initialization.waiting_for_enter_name)
# #     dp.register_message_handler(get_contact, state=Initialization.waiting_for_enter_contact)
# #     dp.register_message_handler(confirm_contact, state=Initialization.waiting_for_confirm_contact) r
