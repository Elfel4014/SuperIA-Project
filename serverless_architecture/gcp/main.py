def hello_superia(request):
    """
    Função Google Cloud Function de exemplo que retorna uma mensagem de boas-vindas.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'Mundo'

    return f'Olá, {name}! Esta é a SuperIA Google Cloud Function!'

