import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("table-3aa4ba2c")

    try:
        product_name = json.loads(event["body"])["nome"]
        table.delete_item(Key={"nome": product_name})
        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "Produto deletado com sucesso"}),
        }
    except Exception as e:
        response = {"statusCode": 500, "body": json.dumps({"message": str(e)})}

    return response
