from dataclasses import dataclass




# Уровень 1
# Тип-сумма: значение LoadState может быть только
# одним из трёх вариантов.


class LoadState(Enum):
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"




# Уровень 2
# Тип-произведение: один User одновременно содержит
# имя, возраст и email.
# frozen=True запрещает изменение созданного пользователя.


@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str




# Уровень 3
# Успешный результат содержит значение.


@dataclass(frozen=True)
class Success[T]:
    value: T




# Ошибка содержит описание ошибки.


@dataclass(frozen=True)
class Failure[E]:
    error: E




# Result является суммой двух вариантов:
# либо Success, либо Failure.


type Result[T, E] = Success[T] | Failure[E]




# Чистая функция загрузки пользователей.
# Никаких внешних данных она не изменяет.
# Один и тот же вызов всегда возвращает один и тот же результат.


def load_users() -> Result[list[User], str]:
    return (
        lambda users:
            (
                lambda: Failure("Список пользователей пуст"),
                lambda: Success(users)
            )[bool(users)]()
    )(
        [
            User("Анна", 20, "anna@example.com"),
            User("Иван", 24, "ivan@example.com")
        ]
    )




# Уровень 4 — мощность типов
#
# LoadState:
# |LoadState| = 3
#
# Потому что существует только три возможных значения:
# LOADING, SUCCESS, ERROR.
#
#
# User:
# |User| = |str| × |int| × |str|
#
# Это тип-произведение, потому что User одновременно
# содержит имя И возраст И email.
#
# Так как строки и целые числа не ограничены условием,
# множество возможных User является счётно бесконечным.
#
#
# Result[T, E]:
# |Result[T, E]| = |T| + |E|
#
# Это тип-сумма, потому что результат является
# либо Success, либо Failure.
#
#
# Для нашей функции:
#
# |Result[list[User], str]|
# =
# |list[User]| + |str|
#
# Оба множества без дополнительных ограничений
# являются счётно бесконечными,
# поэтому Result также имеет счётно бесконечную мощность.




# ==========================================
# ПРОВЕРКА
# В этом блоке нет ни одной переменной.
# ==========================================


assert LoadState.LOADING.value == "loading"
assert LoadState.SUCCESS.value == "success"
assert LoadState.ERROR.value == "error"


assert User(
    "Анна",
    20,
    "anna@example.com"
) == User(
    "Анна",
    20,
    "anna@example.com"
)


assert Success(
    [
        User("Анна", 20, "anna@example.com"),
        User("Иван", 24, "ivan@example.com")
    ]
) == Success(
    [
        User("Анна", 20, "anna@example.com"),
        User("Иван", 24, "ivan@example.com")
    ]
)


assert Failure(
    "Список пользователей пуст"
) == Failure(
    "Список пользователей пуст"
)


assert isinstance(
    load_users(),
    Success
)


assert load_users() == Success(
    [
        User("Анна", 20, "anna@example.com"),
        User("Иван", 24, "ivan@example.com")
    ]
)


assert load_users() == load_users()


print("Все проверки пройдены успешно.")