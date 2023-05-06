from abc import ABC, abstractmethod

from app.user.domain.entities import User


class SyncCloud(ABC):
    @abstractmethod
    def send_user(self, user: User) -> None:
        raise NotImplementedError()
