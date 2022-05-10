from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel_button = KeyboardButton('Главное меню')

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.row(cancel_button)

level_1_btn = InlineKeyboardButton(text='1 уровень', callback_data='cb_1 уровень:40000')
level_2_btn = InlineKeyboardButton(text='2 уровня', callback_data='cb_2 уровня:75000')
level_3_btn = InlineKeyboardButton(text='3 уровня', callback_data='cb_3 уровня:110000')

level_keyboard = InlineKeyboardMarkup(row_width=1)
level_keyboard.add(level_1_btn).add(level_2_btn).add(level_3_btn)

square_btn = InlineKeyboardButton(text='Квадрат',callback_data='cb_Квадрат:60000')
circle_btn = InlineKeyboardButton(text='Круг',callback_data='cb_Круг:40000')
rectangle_btn = InlineKeyboardButton(text='Прямоугольник',callback_data='cb_Прямоугольник:100000')

form_keyboard = InlineKeyboardMarkup(row_width=1)
form_keyboard.add(square_btn).add(circle_btn).add(rectangle_btn)

topping_none_btn = InlineKeyboardButton(text='Без топпинга', callback_data='cb_Без топпинга:0')
topping_white_btn = InlineKeyboardButton(text='Белый соус', callback_data='cb_Белый соус:20000')
topping_caramel_btn = InlineKeyboardButton(text='Карамельный сироп', callback_data='cb_Карамельный сироп:18000')
topping_maple_btn = InlineKeyboardButton(text='Кленовый сироп', callback_data='cb_Кленовый сироп:20000')
topping_strawberry_btn = InlineKeyboardButton(text='Клубничный сироп', callback_data='cb_Клубничный сироп:30000')
topping_blueberry_btn = InlineKeyboardButton(text='Черничный сироп', callback_data='cb_Черничный сироп:35000')
topping_milk_btn = InlineKeyboardButton(text='Молочный шоколад', callback_data='cb_Молочный шоколад:20000')

topping_keyboard = InlineKeyboardMarkup(row_width=2)
topping_keyboard.add(
    topping_none_btn
    ).row(
        topping_white_btn,
        topping_caramel_btn
    ).row(
        topping_maple_btn,
        topping_strawberry_btn
    ).row(
        topping_blueberry_btn,
        topping_milk_btn
    )

berries_none_btn = InlineKeyboardButton(text='Без ягод', callback_data='cb_Без ягод:0')
berries_blackberry_btn = InlineKeyboardButton(text='Ежевика', callback_data='cb_Ежевика:40000')
berries_raspberry_btn = InlineKeyboardButton(text='Малина', callback_data='cb_Малина:30000')
berries_blueberry_btn = InlineKeyboardButton(text='Голубика', callback_data='cb_Голубика:45000')
berries_strawberry_btn = InlineKeyboardButton(text='Клубника', callback_data='cb_Клубника:50000')

berries_keyboard = InlineKeyboardMarkup(row_width=2)
berries_keyboard.add(
    berries_none_btn
    ).row(
        berries_blackberry_btn,
        berries_raspberry_btn
    ).row(
        berries_blueberry_btn,
        berries_strawberry_btn
    )

decor_none_btn = InlineKeyboardButton(text='Без декора', callback_data='cb_Без декора:0')
decor_pistachios_btn = InlineKeyboardButton(text='Фисташки', callback_data='cb_Фисташки:30000')
decor_meringue_btn = InlineKeyboardButton(text='Безе', callback_data='cb_Безе:40000')
decor_hazelnut_btn = InlineKeyboardButton(text='Фундук', callback_data='cb_Фундук:35000')
decor_pecan_btn = InlineKeyboardButton(text='Пекан', callback_data='cb_Пекан:30000')
decor_marshmallow_btn = InlineKeyboardButton(text='Маршмеллоу', callback_data='cb_Маршмеллоу:20000')
decor_marzipan_btn = InlineKeyboardButton(text='Марципан', callback_data='cb_Марципан:28000')

decor_keyboard = InlineKeyboardMarkup(row_width=2)
decor_keyboard.add(
        decor_none_btn
    ).row(
        decor_pistachios_btn,
        decor_meringue_btn
    ).row(
        decor_hazelnut_btn,
        decor_pecan_btn
    ).row(
        decor_marshmallow_btn,
        decor_marzipan_btn
    )

inscription_btn = KeyboardButton('Без надписи')
inscription_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
inscription_keyboard.add(inscription_btn).add(cancel_button)

comment_btn = KeyboardButton('Без комментария')
comment_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
comment_keyboard.add(comment_btn).add(cancel_button)

promocode_btn = KeyboardButton('Нет промокода')
promocode_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
promocode_keyboard.add(promocode_btn).add(cancel_button)

time_9_btn = KeyboardButton('9 часов')
time_10_btn = KeyboardButton('10 часов')
time_11_btn = KeyboardButton('11 часов')
time_12_btn = KeyboardButton('12 часов')
time_13_btn = KeyboardButton('13 часов')
time_14_btn = KeyboardButton('14 часов')
time_15_btn = KeyboardButton('15 часов')
time_16_btn = KeyboardButton('16 часов')
time_17_btn = KeyboardButton('17 часов')
time_18_btn = KeyboardButton('18 часов')
time_19_btn = KeyboardButton('19 часов')
time_20_btn = KeyboardButton('20 часов')

time_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
time_keyboard.row(
            time_9_btn,
            time_10_btn,
            time_11_btn
        ).row(
            time_12_btn,
            time_13_btn,
            time_14_btn
        ).row(
            time_15_btn,
            time_16_btn,
            time_17_btn
        ).row(
            time_18_btn,
            time_19_btn,
            time_20_btn
        ).add(cancel_button)
