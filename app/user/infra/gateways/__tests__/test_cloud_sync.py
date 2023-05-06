from moto import mock_dynamodb

from app.user.infra.gateways.cloud_sync import SyncCloudService
from app.user.domain.entities import User

sync_cloud = SyncCloudService()
user = User(1, "Tester", "test@gmail.com", "123", True)


@mock_dynamodb
def test_should_send_user_to_dinamodb():
    assert sync_cloud.send_user(user) == True
