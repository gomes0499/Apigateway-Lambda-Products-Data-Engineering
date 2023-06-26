import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('NomeDaSuaTabela')

    try:
        product_name = event['queryStringParameters']['nome']
        dynamodb_response = table.get_item(Key={'nome': product_name})
        
        if 'Item' in dynamodb_response:
            response = {
                'statusCode': 200,
                'body': json.dumps(dynamodb_response['Item'])
            }
        else:
            response = {
                'statusCode': 404,
                'body': json.dumps({'message': 'Produto não encontrado'})
            }
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }

    return response
