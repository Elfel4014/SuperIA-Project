import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Requisição HTTP recebida pela SuperIA Azure Function.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        return func.HttpResponse(f"Olá, {name}! Esta é a SuperIA Azure Function.")
    else:
        return func.HttpResponse(
             "Por favor, passe um nome na string de consulta ou no corpo da requisição para a SuperIA Azure Function.",
             status_code=200
        )

