from google.cloud import storage

def create_gcs_bucket(bucket_name, project_id, location=\'US\'):
    """
    Cria um bucket no Google Cloud Storage.
    :param bucket_name: Nome único do bucket GCS.
    :param project_id: ID do projeto GCP.
    :param location: Localização do bucket. Default é \'US\'.
    :return: True se o bucket foi criado com sucesso, False caso contrário.
    """
    try:
        storage_client = storage.Client(project=project_id)
        bucket = storage_client.create_bucket(bucket_name, location=location)
        print(f"Bucket \'{bucket.name}\' criado com sucesso na localização \'{location}\' no projeto \'{project_id}\'")
        return True
    except Exception as e:
        print(f"Erro ao criar o bucket GCS: {e}")
        return False

def delete_gcs_bucket(bucket_name, project_id):
    """
    Deleta um bucket no Google Cloud Storage.
    :param bucket_name: Nome do bucket GCS a ser deletado.
    :param project_id: ID do projeto GCP.
    :return: True se o bucket foi deletado com sucesso, False caso contrário.
    """
    try:
        storage_client = storage.Client(project=project_id)
        bucket = storage_client.get_bucket(bucket_name)
        bucket.delete()
        print(f"Bucket \'{bucket_name}\' deletado com sucesso no projeto \'{project_id}\'")
        return True
    except Exception as e:
        print(f"Erro ao deletar o bucket GCS: {e}")
        return False

if __name__ == \'__main__\':
    # Exemplo de uso:
    # Certifique-se de que suas credenciais GCP estão configuradas (variável de ambiente GOOGLE_APPLICATION_CREDENTIALS)
    # export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/keyfile.json"

    bucket_name = \'superia-test-bucket-gcp-12345\'
    project_id = \'your-gcp-project-id\' # Substitua pelo ID do seu projeto GCP
    gcp_location = \'us-central1\' # ou \'southamerica-east1\' para São Paulo

    if project_id == \'your-gcp-project-id\':
        print("Por favor, configure a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS e substitua o project_id no código.")
    else:
        print(f"Tentando criar o bucket: {bucket_name} na localização: {gcp_location} no projeto: {project_id}")
        if create_gcs_bucket(bucket_name, project_id, gcp_location):
            print("Bucket criado. Você pode verificar no console do GCP.")
            # Para deletar o bucket após a criação (descomente para usar):
            # input("Pressione Enter para deletar o bucket...")
            # delete_gcs_bucket(bucket_name, project_id)
        else:
            print("Falha ao criar o bucket.")

