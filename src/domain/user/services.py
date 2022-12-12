from typing import List, Callable, Tuple

from src.domain.user.entities import User


class UserService:

    @staticmethod
    def increase_points(user: User, qtd_points: int) -> User:
        user.points += qtd_points
        return user

    @staticmethod
    def increase_points_to_all(users: List[User], qtd_points: int) -> Tuple[User]:

        func: Callable[[User], None] = lambda user: UserService.increase_points(
            user, qtd_points)

        return tuple(map(func, users))
