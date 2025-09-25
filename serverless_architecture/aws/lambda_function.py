import json

def lambda_handler(event, context):
    """
    Função AWS Lambda de exemplo que retorna uma mensagem de boas-vindas.
    """
    print(f"Evento recebido: {event}")
    return {
        'statusCode': 200,
        'body': json.dumps('Olá da SuperIA Lambda Function!')
    }

