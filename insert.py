import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("table-3aa4ba2c")

    try:
        data = json.loads(event["body"])
        table.put_item(Item=data)
        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "produto adicionado com sucesso"}),
        }

    except Exception as e:
        response = {"statusCode": 500, "body": json.dumps({"message": str(e)})}

    return response
