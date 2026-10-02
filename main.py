import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from dotenv import load_dotenv

from keyboards import main_menu, back_to_menu
from playlists import PLAYLISTS, format_playlist
from quiz import QUESTIONS, calculate_result

# ---------- Загрузка токена ----------
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Не найден BOT_TOKEN в файле .env")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


# ---------- FSM для викторины ----------
class QuizStates(StatesGroup):
    answering = State()  # пользователь проходит викторину


# ---------- /start ----------
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🎧 Привет! Подберём музыку под твоё настроение.\n\n"
        "Выбери, что ты сейчас чувствуешь, или нажми "
        "«Определи за меня» — и я задам пару вопросов.",
        reply_markup=main_menu(),
    )


# ---------- Отправка плейлиста (с картинкой) ----------
async def send_mood(message: types.Message, mood_key: str):
    """Отправляет картинку + описание + треки."""
    text = format_playlist(mood_key)
    photo_path = f"images/{mood_key}.jpg"

    if os.path.exists(photo_path):
        photo = FSInputFile(photo_path)
        await message.answer_photo(photo=photo, caption=text)
    else:
        # Если картинки нет — просто текст (чтобы бот не падал)
        await message.answer(text)


# ---------- Режим 1: кнопки с настроением ----------
@dp.callback_query(F.data.in_(PLAYLISTS.keys()))
async def send_playlist(callback: types.CallbackQuery):
    await send_mood(callback.message, callback.data)
    await callback.answer()


# ---------- Режим 2: викторина ----------
@dp.callback_query(F.data == "quiz_start")
async def quiz_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(QuizStates.answering)
    await state.update_data(step=0, answers=[])

    await callback.message.answer("✨ Отвечай честно — так точнее подберу ✨")
    await ask_question(callback.message, 0)
    await callback.answer()


async def ask_question(message: types.Message, step: int):
    """Отправляет вопрос №step с вариантами ответа."""
    question = QUESTIONS[step]

    # Варианты ответа как inline-кнопки.
    # callback_data: "ans:{номер_вопроса}:{номер_варианта}"
    buttons = [
        [types.InlineKeyboardButton(
            text=opt["text"],
            callback_data=f"ans:{step}:{i}",
        )]
        for i, opt in enumerate(question["options"])
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer(
        f"Вопрос {step + 1} из {len(QUESTIONS)}\n\n{question['text']}",
        reply_markup=keyboard,
    )


@dp.callback_query(F.data.startswith("ans:"), QuizStates.answering)
async def quiz_answer(callback: types.CallbackQuery, state: FSMContext):
    # Разбираем callback_data
    _, step_str, option_str = callback.data.split(":")
    step = int(step_str)
    option_index = int(option_str)

    # Сохраняем ответ
    data = await state.get_data()
    answers = data.get("answers", [])
    answers.append(QUESTIONS[step]["options"][option_index])
    await state.update_data(answers=answers)

    # Убираем старые кнопки (чтобы нельзя было нажать дважды)
    try:
        await callback.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    next_step = step + 1

    if next_step < len(QUESTIONS):
        # Задаём следующий вопрос
        await state.update_data(step=next_step)
        await ask_question(callback.message, next_step)
    else:
        # Викторина окончена — считаем результат
        mood_key = calculate_result(answers)
        await state.clear()

        await callback.message.answer("Готово! Секунду...")
        await send_mood(callback.message, mood_key)
        await callback.message.answer(
            "Хочешь ещё? Выбери другое настроение",
            reply_markup=main_menu(),
        )

    await callback.answer()


# ---------- Кнопка «В меню» ----------
@dp.callback_query(F.data == "main_menu")
async def back_menu(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(
        "Выбери настроение 👇",
        reply_markup=main_menu(),
    )
    await callback.answer()


# ---------- Запуск ----------
async def main():
    print("Бот запущен. Нажми Ctrl+C для остановки.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())