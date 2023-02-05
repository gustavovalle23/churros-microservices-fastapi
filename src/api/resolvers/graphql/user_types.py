import typing
import strawberry

@strawberry.type
class User:
    id: int
    name: str
    email: str
