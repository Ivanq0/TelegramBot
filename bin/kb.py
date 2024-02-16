from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="📝 Калькулятор", callback_data="calculate_number"),
    InlineKeyboardButton(text="🖼 Перевод", callback_data="transform_number")],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти в меню", callback_data="menu")]])

choice_system_first = [
    [InlineKeyboardButton(text="Двоичная", callback_data="first_two"),
    InlineKeyboardButton(text="Троичная", callback_data="first_three")],
    [InlineKeyboardButton(text="Восьмиричная", callback_data="first_eight"),
    InlineKeyboardButton(text="Десятичная", callback_data="first_ten")],
    [InlineKeyboardButton(text="Шестнадцатеричная", callback_data="first_sixteen")]
]
choice_system_first = InlineKeyboardMarkup(inline_keyboard=choice_system_first)

choice_system_second = [
    [InlineKeyboardButton(text="Двоичная", callback_data="second_two"),
    InlineKeyboardButton(text="Троичная", callback_data="second_three")],
    [InlineKeyboardButton(text="Восьмиричная", callback_data="second_eight"),
    InlineKeyboardButton(text="Десятичная", callback_data="second_ten")],
    [InlineKeyboardButton(text="Шестнадцатеричная", callback_data="second_sixteen")]
]

choice_system_second = InlineKeyboardMarkup(inline_keyboard=choice_system_second)

choice_operation = [
    [InlineKeyboardButton(text="Сложение", callback_data="plus"),
    InlineKeyboardButton(text="Вычитание", callback_data="minus")],
    [InlineKeyboardButton(text="Деление", callback_data="divide"),
    InlineKeyboardButton(text="Умножение", callback_data="multiply")],
]

choice_operation = InlineKeyboardMarkup(inline_keyboard=choice_operation)

choice_system_answer = [
    [InlineKeyboardButton(text="Двоичная", callback_data="answer_two"),
    InlineKeyboardButton(text="Троичная", callback_data="answer_three")],
    [InlineKeyboardButton(text="Восьмиричная", callback_data="answer_eight"),
    InlineKeyboardButton(text="Десятичная", callback_data="answer_ten")],
    [InlineKeyboardButton(text="Шестнадцатеричная", callback_data="answer_sixteen")]
]

choice_system_answer = InlineKeyboardMarkup(inline_keyboard=choice_system_answer)