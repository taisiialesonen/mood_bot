# Все плейлисты и описания. Чтобы добавить новое настроение —
# допиши его в PLAYLISTS и в keyboards.py (кнопку).

PLAYLISTS = {
    "joyful": {
        "title": "Радостное",
        "description": (
            "Радость — это тёплое чувство, когда хочется улыбаться без причины. "
            "Всё внутри звучит легко и правильно, как будто мир на твоей стороне."
        ),
        "tracks": [
            "Pharrell Williams — Happy",
            "Lizzo — Good as Hell",
            "Dua Lipa — Levitating",
            "Harry Styles — Treat People With Kindness",
            "Coldplay — A Sky Full of Stars",
        ],
    },
    "fun": {
        "title": "Весёлое",
        "description": (
            "Веселье — это когда хочется шутить, дурачиться и заражать "
            "всех вокруг своим настроем. Музыка — яркая, энергичная, «улыбательная»."
        ),
        "tracks": [
            "Meghan Trainor — All About That Bass",
            "Katy Perry — Roar",
            "Bruno Mars — 24K Magic",
            "Ava Max — Kings & Queens",
            "OneRepublic — I Ain't Worried",
        ],
    },
    "dreamy": {
        "title": "Мечтательное",
        "description": (
            "Мечтательное состояние — когда мысли улетают далеко, а реальность "
            "становится полупрозрачной. Хочется смотреть в окно и улыбаться своим мыслям."
        ),
        "tracks": [
            "Taylor Swift — Wildest Dreams",
            "Lana Del Rey — Young and Beautiful",
            "Cigarettes After Sex — Apocalypse",
            "Novo Amor — Anchor",
            "Billie Eilish — lovely",
        ],
    },
    "nostalgia": {
        "title": "Ностальгическое",
        "description": (
            "Ностальгия — это тёплое чувство о прошлом. Те моменты уже не вернуть, "
            "но музыка возвращает их на пару минут. Грустно и сладко одновременно."
        ),
        "tracks": [
            "Linkin Park — In the End",
            "Avril Lavigne — Complicated",
            "Coldplay — Yellow",
            "Adele — Someone Like You",
            "One Direction — Night Changes",
        ],
    },
    "yearning": {
        "title": "Тоскливое",
        "description": (
            "Тоска — тихое, глубокое чувство. Не рыдание, а сосущая пустота. "
            "Хочется побыть одному и просто дать себе это прожить."
        ),
        "tracks": [
            "Radiohead — Creep",
            "Lana Del Rey — Video Games",
            "Bon Iver — Skinny Love",
            "Tom Odell — Another Love",
            "Billie Eilish — when the party's over",
        ],
    },
    "bittersweet": {
        "title": "Светлая грусть",
        "description": (
            "Светлая грусть — это когда грустно, но тепло. Ты вспоминаешь что-то важное, "
            "и от этого щемит в груди, но улыбка всё равно пробивается. Грусть, которая лечит."
        ),
        "tracks": [
            "Coldplay — Fix You",
            "Ed Sheeran — Photograph",
            "The Lumineers — Ho Hey",
            "Passenger — Let Her Go",
            "Kodaline — All I Want",
        ],
    },
    "euphoric": {
        "title": "Эйфорическое",
        "description": (
            "Эйфория — это когда внутри всё искрит. Ты на пике, ты чувствуешь себя "
            "неуязвимым, весь мир — твой. Музыка должна соответствовать — мощная, взрывная."
        ),
        "tracks": [
            "The Weeknd — Blinding Lights",
            "Dua Lipa — Don't Start Now",
            "Calvin Harris — Feel So Close",
            "Ava Max — Sweet but Psycho",
            "David Guetta — Titanium",
        ],
    },
    "romantic": {
        "title": "Романтическое",
        "description": (
            "Любовь — это чувство, которое перенастраивает тебя изнутри: мир не меняется, но ты"
            " начинаешь улыбаться без причины и что-то теплое как будто растекается по всему телу."
        ),
        "tracks": [
            "Ed Sheeran — Perfect",
            "Taylor Swift — Lover",
            "John Legend — All of Me",
            "Elvis Presley — Can't Help Falling in Love",
            "Adele — Make You Feel My Love",
        ],
    },
    "creative": {
        "title": "Творческое",
        "description": (
            "Творческое состояние — когда хочется создавать. Писать, рисовать, "
            "придумывать. Внутри зреет что-то новое, и музыка помогает ему выйти наружу."
        ),
        "tracks": [
            "Glass Animals — Heat Waves",
            "Alt-J — Breezeblocks",
            "Tame Impala — The Less I Know the Better",
            "Milky Chance — Stolen Dance",
            "Empire of the Sun — Walking on a Dream",
        ],
    },
    "study": {
        "title": "Учебное",
        "description": (
            "Учебное настроение — это когда нужно сосредоточиться. Музыка должна быть "
            "фоном: без слов (или почти без), без резких перепадов. Идеально для "
            "конспектов, кода, чтения."
        ),
        "tracks": [
            "Ólafur Arnalds — Near Light",
            "Nujabes — Feather",
            "Tycho — Awake",
            "Bonobo — Kerala",
            "Brian Eno — An Ending (Ascent)",
        ],
    },
    "vibey": {
        "title": "Вайбово",
        "description": (
            "«Вайбово» сложно объяснить словами — это просто ощущение. Lo-fi, chill, "
            "атмосфера. Не важно, что играет, важно, как оно звучит. Фон для жизни."
        ),
        "tracks": [
            "Idealism — Controlla",
            "Jinsang — Reflection",
            "Saib — West Lake",
            "Nujabes — Feather",
            "Kudasai — Technicolor",
        ],
    },
    "autumn": {
        "title": "Осеннее",
        "description": (
            "Осеннее — это когда пахнет дождём и листьями, хочется свитер, какао "
            "и что-то медленное. Лёгкая меланхолия, но уютная. Осень внутри, "
            "даже если за окном май."
        ),
        "tracks": [
            "Bon Iver — Holocene",
            "The Paper Kites — Bloom",
            "Vancouver Sleep Clinic — Collapse",
            "SYML — Where's My Love",
            "Earth, Wind & Fire — September",
        ],
    },
    "spring": {
        "title": "Весеннее",
        "description": (
            "Весеннее — это свежесть, лёгкость, ощущение, что всё только начинается. "
            "Хочется открыть окно, впустить воздух, и чтобы музыка звучала так же прозрачно."
        ),
        "tracks": [
            "Rex Orange County — Sunflower",
            "Harry Styles — Watermelon Sugar",
            "Vampire Weekend — This Life",
            "Fleet Foxes — Mykonos",
            "Beach House — Space Song",
        ],
    },
    "dance": {
        "title": "Танцевальное",
        "description": (
            "Танцевальное — это когда тело само просит движения. Ритм, бит, bassline — "
            "и ты уже не можешь усидеть. Главное — двигаться."
        ),
        "tracks": [
            "Dua Lipa — Physical",
            "Doja Cat — Say So",
            "The Weeknd — Save Your Tears",
            "Bad Bunny — Tití Me Preguntó",
            "David Guetta & Bebe Rexha — I'm Good (Blue)",
        ],
    },
}


def format_playlist(mood_key: str) -> str:
    """Возвращает красиво оформленный текст: заголовок, описание, треки."""
    playlist = PLAYLISTS[mood_key]
    tracks = "\n".join(f"• {t}" for t in playlist["tracks"])
    return (
        f"{playlist['title']}\n\n"
        f"{playlist['description']}\n\n"
        f"Плейлист:\n{tracks}"
    )