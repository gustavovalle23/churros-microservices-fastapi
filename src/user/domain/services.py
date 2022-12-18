from typing import List, Callable, Tuple

from src.user.domain.entities import User


class UserService:

    @staticmethod
    def increase_points(users: List[User], qtd_points: int) -> Tuple[User]:

        func: Callable[[User], None] = lambda user: user.increase_points(
            qtd_points)

        return tuple(map(func, users))
