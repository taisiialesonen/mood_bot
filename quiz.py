# Викторина: вопросы, варианты ответов и логика подсчёта.

# Структура:
# QUESTIONS — список вопросов. Каждый вопрос:
#   - text: текст вопроса
#   - options: список вариантов. Каждый вариант:
#       - text: что показывается на кнопке
#       - scores: словарь {настроение: очки}

QUESTIONS = [
    {
        "text": "Как ты сегодня спала?",
        "options": [
            {"text": "Мало и плохо", "scores": {"yearning": 2, "bittersweet": 1}},
            {"text": "Нормально", "scores": {"study": 1, "vibey": 1}},
            {"text": "Отлично, полна сил", "scores": {"joyful": 2, "euphoric": 1}},
        ],
    },
    {
        "text": "Что хочется делать прямо сейчас?",
        "options": [
            {"text": "Танцевать и веселиться", "scores": {"dance": 2, "fun": 1}},
            {"text": "Поплакать и обняться", "scores": {"yearning": 2, "romantic": 1}},
            {"text": "Закрыться в комнате с наушниками", "scores": {"dreamy": 2, "vibey": 1}},
            {"text": "Просто отдохнуть", "scores": {"study": 2, "vibey": 1}},
            {"text": "Что-то создавать", "scores": {"creative": 2, "dreamy": 1}},
        ],
    },
    {
        "text": "О чём ты думаешь больше всего?",
        "options": [
            {"text": "О ком-то особенном", "scores": {"romantic": 2, "dreamy": 1}},
            {"text": "О прошлом", "scores": {"nostalgia": 2, "bittersweet": 1}},
            {"text": "О будущем", "scores": {"dreamy": 2, "spring": 1}},
            {"text": "О том, что бесит", "scores": {"yearning": 2, "creative": 1}},
            {"text": "О делах и учёбе", "scores": {"study": 2, "vibey": 1}},
        ],
    },
    {
        "text": "Какая погода за окном (или у тебя внутри)?",
        "options": [
            {"text": "Солнце, тепло", "scores": {"joyful": 2, "spring": 1}},
            {"text": "Дождь, слякоть", "scores": {"yearning": 2, "autumn": 1}},
            {"text": "Листья, ветер", "scores": {"autumn": 2, "bittersweet": 1}},
            {"text": "Всё цветёт", "scores": {"spring": 2, "dreamy": 1}},
            {"text": "Холодно, но уютно", "scores": {"study": 2, "nostalgia": 1}},
        ],
    },
    {
        "text": "Что бы ты включила прямо сейчас?",
        "options": [
            {"text": "Что-то громкое и мощное", "scores": {"euphoric": 2, "dance": 1}},
            {"text": "Что-то тихое и медленное", "scores": {"yearning": 2, "dreamy": 1}},
            {"text": "Что-то с ритмом и битом", "scores": {"dance": 2, "fun": 1}},
            {"text": "Что-то знакомое и старое", "scores": {"nostalgia": 2, "study": 1}},
            {"text": "Что-то нестандартное", "scores": {"creative": 2, "vibey": 1}},
        ],
    },
    {
        "text": "Какое ощущение тебе ближе всего?",
        "options": [
            {"text": "Тепло, дом, уют", "scores": {"study": 2, "bittersweet": 1}},
            {"text": "Что-то неуловимое, «просто вайб»", "scores": {"vibey": 2, "dreamy": 1}},
            {"text": "Хочется праздника", "scores": {"fun": 2, "euphoric": 1}},
            {"text": "Грустно, но по-доброму", "scores": {"bittersweet": 2, "nostalgia": 1}},
            {"text": "На пике, всё круто", "scores": {"euphoric": 2, "joyful": 1}},
        ],
    },
]


def calculate_result(answers: list[dict]) -> str:
    """
    answers — список словарей вида {"scores": {...}},
    по одному на каждый ответ пользователя.
    Возвращает ключ настроения с максимальным количеством очков.
    При равенстве — приоритет тому, кто раньше в списке.
    """
    total: dict[str, int] = {}
    for answer in answers:
        for mood, points in answer["scores"].items():
            total[mood] = total.get(mood, 0) + points

    # Возвращаем настроение с максимумом очков.
    # max() вернёт первый по порядку при равенстве — это ок.
    return max(total, key=total.get)