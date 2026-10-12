def split_words(text: str) -> list[str]:
    return text.lower().translate(
        dict.fromkeys(
            map(ord, '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~«»—–…'),
            " "
        )
    ).split()




# Уровень 2
def count_word_frequencies(words: list[str]) -> dict[str, int]:
    return dict(
        zip(
            words,
            map(words.count, words)
        )
    )




# Уровень 3
def top_word(freq: dict[str, int]) -> str | None:
    return max(
        freq,
        key=freq.get,
        default=None
    )




# Уровень 4
# Побочных эффектов нет.
# Исходные данные функции не изменяют.
# Все функции детерминированы:
# одинаковые входные данные дают одинаковый результат.
#
# Для пустых данных:
# split_words("") -> []
# count_word_frequencies([]) -> {}
# top_word({}) -> None




# =========================
# ПРОВЕРКА
# =========================


assert split_words("Привет, мир! Привет.") == ["привет", "мир", "привет"]


assert split_words(
    "Слово—слово; тест..."
) == ["слово", "слово", "тест"]


assert split_words("") == []


assert count_word_frequencies(
    ["привет", "мир", "привет"]
) == {
    "привет": 2,
    "мир": 1
}


assert count_word_frequencies([]) == {}


assert top_word(
    {
        "привет": 2,
        "мир": 1
    }
) == "привет"


assert top_word({}) is None


assert top_word(
    count_word_frequencies(
        split_words(
            "Кот, пёс! Кот. Кот?"



        )
    )
) == "кот"


print("Все проверки пройдены успешно.)







6083f6258d328147d85359eb06b1406f
