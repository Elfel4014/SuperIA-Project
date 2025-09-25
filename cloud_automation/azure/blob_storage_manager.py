from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def create_blob_container(connection_string, container_name):
    """
    Cria um contêiner de blob no Azure Storage.
    :param connection_string: String de conexão da conta de armazenamento do Azure.
    :param container_name: Nome do contêiner a ser criado.
    :return: True se o contêiner foi criado com sucesso, False caso contrário.
    """
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.create_container(container_name)
        print(f"Contêiner \'{container_name}\' criado com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao criar o contêiner de blob: {e}")
        return False

def delete_blob_container(connection_string, container_name):
    """
    Deleta um contêiner de blob no Azure Storage.
    :param connection_string: String de conexão da conta de armazenamento do Azure.
    :param container_name: Nome do contêiner a ser deletado.
    :return: True se o contêiner foi deletado com sucesso, False caso contrário.
    """
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_service_client.delete_container(container_name)
        print(f"Contêiner \'{container_name}\' deletado com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao deletar o contêiner de blob: {e}")
        return False

if __name__ == '__main__':
    # Exemplo de uso:
    # Substitua pela sua string de conexão do Azure Storage
    # export AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=..."
    connection_string = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
    container_name = "superia-test-container-12345"

    if connection_string == "YOUR_AZURE_STORAGE_CONNECTION_STRING":
        print("Por favor, configure a variável de ambiente AZURE_STORAGE_CONNECTION_STRING ou substitua no código.")
    else:
        print(f"Tentando criar o contêiner: {container_name}")
        if create_blob_container(connection_string, container_name):
            print("Contêiner criado. Você pode verificar no portal do Azure.")
            # Para deletar o contêiner após a criação (descomente para usar):
            # input("Pressione Enter para deletar o contêiner...")
            # delete_blob_container(connection_string, container_name)
        else:
            print("Falha ao criar o contêiner.")

