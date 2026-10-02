from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu() -> InlineKeyboardMarkup:
    """Главное меню: 14 настроений + кнопка викторины."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            # 1 ряд
            [
                InlineKeyboardButton(text="Радостное", callback_data="joyful"),
                InlineKeyboardButton(text="Весёлое", callback_data="fun"),
            ],
            # 2 ряд
            [
                InlineKeyboardButton(text="Мечтательное", callback_data="dreamy"),
                InlineKeyboardButton(text="Ностальгия", callback_data="nostalgia"),
            ],
            # 3 ряд
            [
                InlineKeyboardButton(text="Тоскливое", callback_data="yearning"),
                InlineKeyboardButton(text="Светлая грусть", callback_data="bittersweet"),
            ],
            # 4 ряд
            [
                InlineKeyboardButton(text="Эйфорическое", callback_data="euphoric"),
                InlineKeyboardButton(text="Романтичное", callback_data="romantic"),
            ],
            # 5 ряд
            [
                InlineKeyboardButton(text="Творческое", callback_data="creative"),
                InlineKeyboardButton(text="Учебное", callback_data="study"),
            ],
            # 6 ряд
            [
                InlineKeyboardButton(text="Вайбово", callback_data="vibey"),
                InlineKeyboardButton(text="Осеннее", callback_data="autumn"),
            ],
            # 7 ряд
            [
                InlineKeyboardButton(text="Весеннее", callback_data="spring"),
                InlineKeyboardButton(text="Танцевальное", callback_data="dance"),
            ],
            # Отдельная кнопка на всю ширину
            [
                InlineKeyboardButton(
                    text="Определи за меня",
                    callback_data="quiz_start",
                ),
            ],
        ]
    )


def back_to_menu() -> InlineKeyboardMarkup:
    """Кнопка возврата в главное меню (пригодится позже)."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅В меню",
                    callback_data="main_menu",
                ),
            ],
        ]
    )