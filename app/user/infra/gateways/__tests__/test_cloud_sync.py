import boto3
from moto import mock_dynamodb
from mypy_boto3_dynamodb import DynamoDBClient

from app.user.infra.gateways.cloud_sync import SyncCloudService, create_dynamodb_client
from app.user.domain.entities import User

user = User(1, "Tester", "test@gmail.com", "123", True)


def create_user_table(dynamodb: DynamoDBClient):
    dynamodb.create_table(
        TableName="users",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )


@mock_dynamodb
def test_should_send_user_to_dinamodb():
    client = create_dynamodb_client()
    sync_cloud = SyncCloudService(client)

    create_user_table(client)

    assert sync_cloud.send_user(user) == True
