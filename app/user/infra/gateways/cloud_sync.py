import boto3
from mypy_boto3_dynamodb import DynamoDBClient

from app.user.domain.entities import User


class SyncCloudService:
    def send_user(self, user: User) -> bool:
        dynamodb: DynamoDBClient = boto3.client("dynamodb")
        dynamodb.create_table(
            TableName="users",
            KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
            AttributeDefinitions=[
                {"AttributeName": "id", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )

        dynamodb.put_item(
            TableName="users",
            Item={
                "id": {"S": "1"},
                "name": {"S": "Tester V"},
                "email": {"S": "email@example.com"},
            },
        )

        item = dynamodb.get_item(TableName="users", Key={"id": {"S": "1"}})
        return bool(item.get("Item"))
