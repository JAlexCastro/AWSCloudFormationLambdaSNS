import boto3

# Especifica la región de AWS que deseas utilizar
region_name = 'us-west-2'

# Crea un cliente de AWS Lambda
sns_client = boto3.client('sns', region_name=region_name)

# Aquí agregaremos ejemplos de suscripción por correo electrónico y por SMS
def suscribirEmail(email, arn_tema):
    email_subscrito = sns_client.subscribe(
        TopicArn=arn_tema,
        Protocol='email',
        Endpoint=email
    )

    print(f"Email {email} suscrito.")
    return email_subscrito


arnTemaTest = "ARN DEL TEMA SNS"
suscribirEmail("CORREO_ELECTRONICO", arnTemaTest)