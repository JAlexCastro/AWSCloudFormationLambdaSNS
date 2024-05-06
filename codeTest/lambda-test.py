import boto3
import json

# Especifica la región de AWS que deseas utilizar
region_name = 'us-west-2'

# Crea un cliente de AWS Lambda
lambda_client = boto3.client('lambda', region_name=region_name)

# Define el payload que pasará a la función Lambda
payload = {
    "key1": "valor1",
}

function_arn = "ARN DE LA FUNCION LAMBDA"

# Invoca la función Lambda
response = lambda_client.invoke(
    FunctionName=function_arn,
    InvocationType='RequestResponse',  # 'RequestResponse' para una invocación síncrona
    Payload=json.dumps(payload)  # El payload debe ser una cadena JSON
)

# Lee la respuesta de la invocación
response_payload = json.loads(response['Payload'].read().decode("utf-8"))

# Imprime la respuesta de la función Lambda
print(response_payload)
