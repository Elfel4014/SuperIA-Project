import boto3

def create_s3_bucket(bucket_name, region='us-east-1'):
    """
    Cria um bucket S3 na AWS.
    :param bucket_name: Nome único do bucket S3.
    :param region: Região da AWS onde o bucket será criado. Default é 'us-east-1'.
    :return: True se o bucket foi criado com sucesso, False caso contrário.
    """
    try:
        s3_client = boto3.client('s3', region_name=region)
        if region == 'us-east-1':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
        print(f"Bucket '{bucket_name}' criado com sucesso na região '{region}'.")
        return True
    except Exception as e:
        print(f"Erro ao criar o bucket S3: {e}")
        return False

def delete_s3_bucket(bucket_name, region='us-east-1'):
    """
    Deleta um bucket S3 na AWS.
    :param bucket_name: Nome do bucket S3 a ser deletado.
    :param region: Região da AWS onde o bucket está localizado.
    :return: True se o bucket foi deletado com sucesso, False caso contrário.
    """
    try:
        s3_client = boto3.client('s3', region_name=region)
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deletado com sucesso na região '{region}'.")
        return True
    except Exception as e:
        print(f"Erro ao deletar o bucket S3: {e}")
        return False

if __name__ == '__main__':
    # Exemplo de uso:
    # Certifique-se de que suas credenciais AWS estão configuradas (variáveis de ambiente, ~/.aws/credentials, etc.)
    # export AWS_ACCESS_KEY_ID='YOUR_ACCESS_KEY'
    # export AWS_SECRET_ACCESS_KEY='YOUR_SECRET_KEY'

    bucket_name = 'superia-test-bucket-12345'
    aws_region = 'us-east-1' # ou 'sa-east-1' para São Paulo

    print(f"Tentando criar o bucket: {bucket_name} na região: {aws_region}")
    if create_s3_bucket(bucket_name, aws_region):
        print("Bucket criado. Você pode verificar no console da AWS.")
        # Para deletar o bucket após a criação (descomente para usar):
        # input("Pressione Enter para deletar o bucket...")
        # delete_s3_bucket(bucket_name, aws_region)
    else:
        print("Falha ao criar o bucket.")

