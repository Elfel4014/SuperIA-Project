from kubernetes import client, config

def deploy_nginx_app(api_client, namespace="default", name="nginx-example", replicas=1):
    """
    Cria um Deployment e um Service para uma aplicação Nginx no Kubernetes.
    :param api_client: Instância da API de AppsV1Api do Kubernetes.
    :param namespace: Namespace onde o Deployment e o Service serão criados.
    :param name: Nome base para o Deployment e o Service.
    :param replicas: Número de réplicas para o Deployment.
    """
    # Configuração do Deployment
    container = client.V1Container(
        name=name,
        image="nginx:latest",
        ports=[client.V1ContainerPort(container_port=80)]
    )
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": name}),
        spec=client.V1PodSpec(containers=[container])
    )
    spec = client.V1DeploymentSpec(
        replicas=replicas,
        template=template,
        selector={"matchLabels": {"app": name}}
    )
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=name),
        spec=spec
    )

    # Criação do Deployment
    try:
        api_client.create_namespaced_deployment(body=deployment, namespace=namespace)
        print(f"Deployment '{name}' criado com sucesso no namespace '{namespace}'.")
    except client.ApiException as e:
        print(f"Erro ao criar Deployment '{name}': {e}")
        return

    # Configuração do Service
    service_spec = client.V1ServiceSpec(
        selector={"app": name},
        ports=[client.V1ServicePort(protocol="TCP", port=80, target_port=80)],
        type="LoadBalancer" # Ou NodePort, ClusterIP dependendo do ambiente
    )
    service = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(name=name + "-service"),
        spec=service_spec
    )

    # Criação do Service
    try:
        client.CoreV1Api().create_namespaced_service(body=service, namespace=namespace)
        print(f"Service '{name}-service' criado com sucesso no namespace '{namespace}'.")
    except client.ApiException as e:
        print(f"Erro ao criar Service '{name}-service': {e}")

def delete_nginx_app(api_client, namespace="default", name="nginx-example"):
    """
    Deleta um Deployment e um Service de uma aplicação Nginx no Kubernetes.
    :param api_client: Instância da API de AppsV1Api do Kubernetes.
    :param namespace: Namespace onde o Deployment e o Service estão localizados.
    :param name: Nome base do Deployment e do Service.
    """
    try:
        api_client.delete_namespaced_deployment(
            name=name,
            namespace=namespace,
            body=client.V1DeleteOptions(propagation_policy="Foreground", grace_period_seconds=5)
        )
        print(f"Deployment '{name}' deletado com sucesso.")
    except client.ApiException as e:
        print(f"Erro ao deletar Deployment '{name}': {e}")

    try:
        client.CoreV1Api().delete_namespaced_service(
            name=name + "-service",
            namespace=namespace,
            body=client.V1DeleteOptions(propagation_policy="Foreground", grace_period_seconds=5)
        )
        print(f"Service '{name}-service' deletado com sucesso.")
    except client.ApiException as e:
        print(f"Erro ao deletar Service '{name}-service': {e}")

if __name__ == "__main__":
    # Carrega a configuração do Kubernetes (do ~/.kube/config ou variáveis de ambiente)
    try:
        config.load_kube_config()
    except config.config_exception.ConfigException:
        print("Não foi possível carregar a configuração do kube. Verifique se o arquivo ~/.kube/config existe ou se as variáveis de ambiente estão configuradas.")
        exit(1)

    apps_v1 = client.AppsV1Api()

    app_name = "superia-nginx"
    app_namespace = "default"

    print(f"Tentando implantar a aplicação Nginx: {app_name} no namespace: {app_namespace}")
    deploy_nginx_app(apps_v1, namespace=app_namespace, name=app_name, replicas=2)

    # Para deletar a aplicação após a implantação (descomente para usar):
    # input("Pressione Enter para deletar a aplicação Nginx...")
    # delete_nginx_app(apps_v1, namespace=app_namespace, name=app_name)

