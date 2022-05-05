from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

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
    await message.reply('Выберите количество уровней торта')


# ловим первый ответ
async def choose_levels(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['levels'] = message.text
    await FSMOrder.next()
    await message.reply('Выберите форму торта')


# ловим второй ответ
async def choose_form(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['form'] = message.text
    await FSMOrder.next()
    await message.reply('Выберите топпинг')


# третий ответ
async def choose_topping(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['topping'] = message.text
    await FSMOrder.next()
    await message.reply('Выберите ягоды')


# четвертый ответ
async def choose_berries(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['berries'] = message.text
    await FSMOrder.next()
    await message.reply('Выберите декор')


# пятый ответ
async def choose_decor(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['decor'] = message.text
    await FSMOrder.next()
    await message.reply('Надпись на торт')


# шестой ответ
async def choose_inscription(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['inscription'] = message.text
    await FSMOrder.next()
    await message.reply('Комментарий к заказу')


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
    await message.reply('Введите промокод, если он у вас есть')


# одиннадцатый ответ
async def specify_promocode(message: types.Message, state: FSMContext):
    async with state.proxy() as cake:
        cake['promocode'] = message.text
    # TODO Здесь запись в бд
    async with state.proxy() as cake:
        await message.reply(str(cake))
    await state.finish()


# Выход из машины состояний
# TODO разобраться почему не работает
async def cancel_order(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


# регистрируем хендлеры
def register_handlers_order(dispatcher: Dispatcher):
    dispatcher.register_message_handler(order_start, commands=['order'], state=None)
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
    dispatcher.register_message_handler(cancel_order, state="*", commands='отмена')
    dispatcher.register_message_handler(cancel_order, Text(equals='отмена', ignore_case=True), state="*")
