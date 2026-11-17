from dataclasses import dataclass
from enum import Enum




# Уровень 1
# Тип-сумма: значение LoadState может быть только одним из трёх вариантов.


class LoadState(Enum):
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"




# Уровень 2
# Тип-произведение: один User одновременно содержит имя, возраст и email.
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


def load_users() -> Result[tuple[User, ...], str]:
    return (
        lambda users:
            Success(users) if users
            else Failure("Список пользователей пуст")
    )




# Уровень 4 — мощность типов
#
# LoadState:
# |LoadState| = 3
#

#
#
# User:
# |User| = |str| × |int| × |str|
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
# |Result[tuple[User, ...], str]| = |tuple[User, ...]| + |str|        |tuple[User, ...]| = 1 + |User| + |User|² + ... (кортежи длины 0, 1, 2, ...)
#
# Оба множества без дополнительных ограничений являются счётно бесконечными, поэтому Result также имеет счётно бесконечную мощность.







a40c25bcb708a3f113a95adbad3b671d431837a8c37cd4e35fefc2de102923b2
