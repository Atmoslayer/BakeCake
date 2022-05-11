from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards import keyboard_client, menu_keyboard, level_keyboard, form_keyboard, topping_keyboard, berries_keyboard, decor_keyboard, inscription_keyboard, comment_keyboard, promocode_keyboard, time_keyboard
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from handlers.payment import payment
from create_bot import dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions import create_order_async

# from create_bot import dispatcher

order_cost = 0
order_data = {}
promocodes = ['async', 'to', 'sync']
delivery_date = ''

pay_inline_markup = InlineKeyboardMarkup(row_width=1)
pay_button = InlineKeyboardButton(text='Оплатить', callback_data='payment')
pay_inline_markup.insert(pay_button)


class FSMOrder(StatesGroup):
    levels = State()
    form = State()
    topping = State()
    berries = State()
    decor = State()
    inscription = State()
    comment = State()
    delivery_address = State()
    delivery_date = State()
    delivery_time = State()
    promocode = State()


# начало диалога
@dispatcher.message_handler(text='Собрать торт')
async def order_start(message: types.Message):
    await FSMOrder.levels.set()
    await message.reply('В этом разделе вы можете собрать торт по своим предпочтениям', reply_markup=menu_keyboard)
    await message.answer('Шаг 1')
    await message.reply('Выберите количество уровней торта', reply_markup=level_keyboard)


# Выход из машины состояний
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK', reply_markup=keyboard_client)


# ловим первый ответ
async def choose_levels(callback: types.CallbackQuery, state: FSMContext):
    global order_cost
    global order_data
    user_input = callback.data.split(':')
    order_cost += int(user_input[1])
    order_data['layers'] = user_input[0][3:]
    await FSMOrder.next()
    await callback.message.answer('Шаг 2')
    await callback.message.reply('Выберите форму торта', reply_markup=form_keyboard)
    await callback.answer()


# ловим второй ответ
async def choose_form(callback: types.CallbackQuery, state: FSMContext):
    global order_cost
    global order_data
    user_input = callback.data.split(':')
    order_cost += int(user_input[1])
    order_data['form'] = user_input[0][3:]
    await FSMOrder.next()
    await callback.message.answer('Шаг 3')
    await callback.message.reply('Выберите топпинг', reply_markup=topping_keyboard)
    await callback.answer()


# третий ответ
async def choose_topping(callback: types.CallbackQuery, state: FSMContext):
    global order_cost
    global order_data
    user_input = callback.data.split(':')
    order_cost += int(user_input[1])
    order_data['topping'] = user_input[0][3:]
    await FSMOrder.next()
    await callback.message.answer('Шаг 4')
    await callback.message.reply('Выберите ягоды', reply_markup=berries_keyboard)
    await callback.answer()


# четвертый ответ
async def choose_berries(callback: types.CallbackQuery, state: FSMContext):
    global order_cost
    global order_data
    user_input = callback.data.split(':')
    order_cost += int(user_input[1])
    order_data['berries'] = user_input[0][3:]
    await FSMOrder.next()
    await callback.message.answer('Шаг 5')
    await callback.message.reply('Выберите декор', reply_markup=decor_keyboard)
    await callback.answer()


# пятый ответ
async def choose_decor(callback: types.CallbackQuery, state: FSMContext):
    global order_cost
    global order_data
    user_input = callback.data.split(':')
    order_cost += int(user_input[1])
    order_data['decor'] = user_input[0][3:]
    await FSMOrder.next()
    await callback.message.answer('Шаг 6')
    await callback.message.reply('Надпись на торт', reply_markup=inscription_keyboard)
    await callback.answer()


# шестой ответ
async def choose_inscription(message: types.Message, state: FSMContext):
    global order_data
    order_data['inscription'] = message.text
    await FSMOrder.next()
    await message.answer('Шаг 7')
    await message.reply('Комментарий к заказу', reply_markup=comment_keyboard)


# седьмой ответ
async def get_comment(message: types.Message, state: FSMContext):
    global order_data
    order_data['comment'] = message.text
    await FSMOrder.next()
    await message.answer('Шаг 8')
    await message.reply('Укажите адрес доставки', reply_markup=menu_keyboard)


# восьмой ответ
async def specify_adress(message: types.Message, state: FSMContext):
    # TODO Уточнение адреса из бд
    global delivery_date
    delivery_date = message.text
    await FSMOrder.next()
    await message.answer('Шаг 7', reply_markup=menu_keyboard)
    await message.reply('Выберите дату доставки', reply_markup=await SimpleCalendar().start_calendar())


# девятый ответ
async def choose_date(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    global order_data
    global delivery_date
    if selected:
        order_data['delivery'] = delivery_date + date.strftime("%d/%m/%Y")
        await FSMOrder.next()
        await callback.message.answer('Шаг 8', reply_markup=menu_keyboard)
        await callback.message.reply('Выберите время доставки', reply_markup=time_keyboard)
        await callback.answer()


# десятый ответ
async def choose_time(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['delivery_time'] = message.text
    await FSMOrder.next()
    await message.answer('Шаг 8')
    await message.reply('Введите промокод, если он у вас есть', reply_markup=promocode_keyboard)


# одиннадцатый ответ
async def specify_promocode(message: types.Message, state: FSMContext):
    global order_data
    while not message.text == 'Нет промокода':
        if message.text in promocodes:
                order_data['promocode'] = message.text
                order_data['price'] = int(order_cost * 0.8)
                await message.answer('Спасибо! Ваш промокод применён')
                break
        else:
            order_data['promocode'] = ''
            order_data['price'] = order_cost
            await message.answer('К сожалению, такого промокода нет. Попробуйте ввести другой')

    # TODO Здесь запись в бд

    await create_order_async(message.from_user.username, order_data)
    # await message.answer(str(order_cost))
    await message.answer('Пожалуйста, оплатите заказ', reply_markup=pay_inline_markup)
    await state.finish()


# регистрируем хендлеры
def register_handlers_order(dispatcher: Dispatcher):
    dispatcher.register_message_handler(order_start, commands=['Собрать_торт'], state=None)
    dispatcher.register_message_handler(cancel_handler, state="*", commands='Главное меню')
    dispatcher.register_message_handler(cancel_handler, Text(equals='Главное меню', ignore_case=True), state="*")
    dispatcher.register_callback_query_handler(choose_levels, Text(startswith='cb_'), state=FSMOrder.levels)
    dispatcher.register_callback_query_handler(choose_form, Text(startswith='cb_'), state=FSMOrder.form)
    dispatcher.register_callback_query_handler(choose_topping, Text(startswith='cb_'), state=FSMOrder.topping)
    dispatcher.register_callback_query_handler(choose_berries, Text(startswith='cb_'), state=FSMOrder.berries)
    dispatcher.register_callback_query_handler(choose_decor, Text(startswith='cb_'), state=FSMOrder.decor)
    dispatcher.register_message_handler(choose_inscription, state=FSMOrder.inscription)
    dispatcher.register_message_handler(get_comment, state=FSMOrder.comment)
    dispatcher.register_message_handler(specify_adress, state=FSMOrder.delivery_address)
    dispatcher.register_callback_query_handler(choose_date, simple_cal_callback.filter(), state=FSMOrder.delivery_date)
    dispatcher.register_message_handler(choose_time, state=FSMOrder.delivery_time)
    dispatcher.register_message_handler(specify_promocode, state=FSMOrder.promocode)
