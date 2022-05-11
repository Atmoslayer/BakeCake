from aiogram import types
from aiogram.types import ContentType, KeyboardButton, ReplyKeyboardMarkup
from create_bot import dispatcher, bot, yoo_token

price = ''
button_start_order = KeyboardButton('Собрать торт')
button_check_orders = KeyboardButton('История заказов')


def payment(price):

    @dispatcher.callback_query_handler(text='payment')
    async def get_payment(call: types.CallbackQuery):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_invoice(chat_id=call.from_user.id, title='Оплата заказа',

                               description='Заказ на изготовление торта',
                               payload='cake_payment',
                               provider_token=yoo_token,
                               currency='RUB',
                               start_parameter='text_pay',
                               prices = [types.LabeledPrice(label='Оплата заказа', amount=int(price / 10))])

    @dispatcher.pre_checkout_query_handler()
    async def payment_pre_checout_query(pre_checkout_query: types.PreCheckoutQuery):
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

    @dispatcher.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
    async def process_pay(message: types.Message):
        if message.successful_payment.invoice_payload == 'cake_payment':
            menu = ReplyKeyboardMarkup(resize_keyboard=True)
            menu.add(button_start_order, button_check_orders)
            await bot.send_message(message.from_user.id, text='Торт оплачен, спасибо!', reply_markup=menu)
