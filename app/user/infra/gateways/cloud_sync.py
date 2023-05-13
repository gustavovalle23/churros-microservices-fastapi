import boto3
from mypy_boto3_dynamodb import DynamoDBClient

from app.user.domain.entities import User


def create_dynamodb_client() -> DynamoDBClient:
    return boto3.client("dynamodb")


class SyncCloudService:
    def __init__(self, dynamodb: DynamoDBClient) -> None:
        self.dynamodb = dynamodb

    def send_user(self, user: User) -> bool:
        self.dynamodb.put_item(
            TableName="users",
            Item={
                "id": {"S": str(user.id)},
                "name": {"S": user.name},
                "email": {"S": user.email},
            },
        )

        item = self.dynamodb.get_item(TableName="users", Key={"id": {"S": "1"}})
        return bool(item.get("Item"))
