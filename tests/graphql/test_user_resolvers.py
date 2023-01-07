import pytest

from src.api.resolvers.schema import schema
from src.bootstrap import bootstrap_di
from tests.utils.utils import UserSeed


@pytest.fixture(autouse=True)
def run_around_tests():
    UserSeed.insert_all()
    yield
    UserSeed.remove_all()


bootstrap_di()


def test_query():
    query = """
query FindUsers {
  findUsers(skip: 0, limit: 10) {
    id
    name
    email
  }
}
    """

    result = schema.execute_sync(
        query,
    )

    assert result.errors is None
    assert result.data["users"] == [
        {
            "name": "Tester",
            "email": "@gmail.com",
        }
    ]
