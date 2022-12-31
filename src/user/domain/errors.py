from typing import List

class EmailAlreadyRegisteredError(Exception):
    def __init__(self, email: str) -> None:
        super().__init__(f'Email "{email}" already registered')


class NotificationError(ValueError):
    def __init__(self, errors: List[str]) -> None:
        super().__init__(" ".join(errors))
