from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

level_1_btn = KeyboardButton('1 уровень(+400)')
level_2_btn = KeyboardButton('2 уровня(+750)')
level_3_btn = KeyboardButton('3 уровня(+1100)')

level_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
level_keyboard.add(level_1_btn).add(level_2_btn).add(level_3_btn)

square_btn = KeyboardButton('Квадрат(+600)')
circle_btn = KeyboardButton('Круг(+400)')
rectangle_btn = KeyboardButton('Прямоугольник(+1000)')

form_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
form_keyboard.add(square_btn).add(circle_btn).add(rectangle_btn)

topping_none_btn = KeyboardButton('Без топпинга(+0)')
topping_white_btn = KeyboardButton('Белый соус(+200)')
topping_caramel_btn = KeyboardButton('Карамельный сироп(+180)')
topping_maple_btn = KeyboardButton('Кленовый сироп(+200)')
topping_strawberry_btn = KeyboardButton('Клубничный сироп(+300)')
topping_blueberry_btn = KeyboardButton('Черничный сироп(+350)')
topping_milk_btn = KeyboardButton('Молочный шоколад(+200)')

topping_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
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

berries_none_btn = KeyboardButton('Без ягод(+0)')
berries_blackberry_btn = KeyboardButton('Ежевика(+400)')
berries_raspberry_btn = KeyboardButton('Малина(+300)')
berries_blueberry_btn = KeyboardButton('Голубика(+450)')
berries_strawberry_btn = KeyboardButton('Клубника(+500)')

berries_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
berries_keyboard.add(
    berries_none_btn
    ).row(
        berries_blackberry_btn,
        berries_raspberry_btn
    ).row(
        berries_blueberry_btn,
        berries_strawberry_btn
    )

decor_none_btn = KeyboardButton('Без декора(+0)')
decor_pistachios_btn = KeyboardButton('Фисташки(+300)')
decor_meringue_btn = KeyboardButton('Безе(+400)')
decor_hazelnut_btn = KeyboardButton('Фундук(+350)')
decor_pecan_btn = KeyboardButton('Пекан(+300)')
decor_marshmallow_btn = KeyboardButton('Маршмеллоу(+200)')
decor_marzipan_btn = KeyboardButton('Марципан(+280')

decor_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
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
inscription_keyboard.add(inscription_btn)

comment_btn = KeyboardButton('Без комментария')
comment_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
comment_keyboard.add(comment_btn)

promocode_btn = KeyboardButton('Нет промокода')
promocode_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
promocode_keyboard.add(promocode_btn)
