from kink import di
import strawberry
import typing
from strawberry.fastapi import GraphQLRouter
from strawberry.extensions import Extension
from strawberry.types.info import Info
from sqlalchemy.orm.session import Session

from app.core.database.models import db_session, SessionLocal
from app.user.usecases import (
    CreateUserUseCase,
    FindUserUseCase,
    UpdateUserUseCase,
    FindUsersUseCase,
    InactivateUserUseCase,
    DeleteUserUseCase,
    LoginUserUseCase,
)
from app.user.domain.contracts.repositories import UserRepository
from app.user.domain.contracts.gateways import SyncCloud
from app.api.resolvers.graphql.user_types import User


class SQLAlchemySession(Extension):
    def on_request_start(self):
        self.execution_context.context["db_session"] = SessionLocal()

    def on_request_end(self):
        self.execution_context.context["db_session"].close()


user_repository: UserRepository = di[UserRepository]
sync_cloud: SyncCloud = di[SyncCloud]

create_user_use_case = CreateUserUseCase(user_repository, sync_cloud)
find_user_use_case = FindUserUseCase(user_repository)
find_users_use_case = FindUsersUseCase(user_repository)
inactivate_user_use_case = InactivateUserUseCase(user_repository)
update_user_use_case = UpdateUserUseCase(user_repository)
delete_user_use_case = DeleteUserUseCase(user_repository)
login_user_use_case = LoginUserUseCase(user_repository)


@strawberry.type
class Query:
    @strawberry.field
    def find_users(self, info: Info, skip: int, limit: int) -> typing.List[User]:
        db: Session = info.context["db_session"]
        db_session.set(db)

        users = find_users_use_case.prepare_input(skip, limit).execute()
        return users.users


schema = strawberry.Schema(Query, extensions=[SQLAlchemySession])
graphql_app = GraphQLRouter(schema)
