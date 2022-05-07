from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards import level_keyboard, form_keyboard, topping_keyboard, berries_keyboard, decor_keyboard, inscription_keyboard, comment_keyboard, promocode_keyboard

from create_bot import dispatcher


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
async def order_start(message: types.Message):
    await FSMOrder.levels.set()
    await message.reply('Выберите количество уровней торта', reply_markup=level_keyboard)


# ловим первый ответ
async def choose_levels(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['levels'] = message.text
    await FSMOrder.next()
    await message.reply('Выберите форму торта', reply_markup=form_keyboard)


# ловим второй ответ
async def choose_form(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['form'] = message.text
    await FSMOrder.next()
    await message.reply('Выберите топпинг', reply_markup=topping_keyboard)


# третий ответ
async def choose_topping(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['topping'] = message.text
    await FSMOrder.next()
    await message.reply('Выберите ягоды', reply_markup=berries_keyboard)


# четвертый ответ
async def choose_berries(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['berries'] = message.text
    await FSMOrder.next()
    await message.reply('Выберите декор', reply_markup=decor_keyboard)


# пятый ответ
async def choose_decor(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['decor'] = message.text
    await FSMOrder.next()
    await message.reply('Надпись на торт', reply_markup=inscription_keyboard)


# шестой ответ
async def choose_inscription(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['inscription'] = message.text
    await FSMOrder.next()
    await message.reply('Комментарий к заказу', reply_markup=comment_keyboard)


# седьмой ответ
async def get_comment(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['comment'] = message.text
    await FSMOrder.next()
    await message.reply('Укажите адрес доставки')


# восьмой ответ
async def specify_adress(message: types.Message, state: FSMContext):
    # TODO Уточнение адреса из бд
    async with state.proxy() as cake:
        cake['delivery_adress'] = message.text
    await FSMOrder.next()
    await message.reply('Выберите дату доставки')


# девятый ответ
async def choose_date(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['delivery_date'] = message.text
    await FSMOrder.next()
    await message.reply('Выберите время доставки')


# десятый ответ
async def choose_time(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['delivery_time'] = message.text
    await FSMOrder.next()
    await message.reply('Введите промокод, если он у вас есть', reply_markup=promocode_keyboard)


# одиннадцатый ответ
async def specify_promocode(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['promocode'] = message.text
    # TODO Здесь запись в бд
    async with state.proxy() as cake:
        await message.reply(str(cake))
    await state.finish()


# Выход из машины состояний
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


# регистрируем хендлеры
def register_handlers_order(dispatcher: Dispatcher):
    dispatcher.register_message_handler(order_start, commands=['Собрать_торт'], state=None)
    dispatcher.register_message_handler(cancel_handler, state="*", commands='отмена')
    dispatcher.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dispatcher.register_message_handler(choose_levels, state=FSMOrder.levels)
    dispatcher.register_message_handler(choose_form, state=FSMOrder.form)
    dispatcher.register_message_handler(choose_topping, state=FSMOrder.topping)
    dispatcher.register_message_handler(choose_berries, state=FSMOrder.berries)
    dispatcher.register_message_handler(choose_decor, state=FSMOrder.decor)
    dispatcher.register_message_handler(choose_inscription, state=FSMOrder.inscription)
    dispatcher.register_message_handler(get_comment, state=FSMOrder.comment)
    dispatcher.register_message_handler(specify_adress, state=FSMOrder.delivery_address)
    dispatcher.register_message_handler(choose_date, state=FSMOrder.delivery_date)
    dispatcher.register_message_handler(choose_time, state=FSMOrder.delivery_time)
    dispatcher.register_message_handler(specify_promocode, state=FSMOrder.promocode)
