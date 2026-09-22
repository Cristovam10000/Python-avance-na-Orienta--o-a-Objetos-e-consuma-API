from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/api/hello")
def hello_word():
    """Atende `GET /api/hello` com uma mensagem de saudação.

    Returns:
        set[str]: conjunto Python com a mensagem "message: Hello World!".
            O FastAPI converte esse conjunto para uma lista na resposta JSON.
    """
    return {"message: Hello World!"}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    """Consulta a API de restaurantes e, opcionalmente, filtra um cardápio.

    Args:
        restaurante: Nome exato do restaurante. Se omitido, a rota retorna
            todos os registros recebidos; se informado, retorna apenas os
            itens desse restaurante.

    Returns:
        dict: Em caso de sucesso, contém todos os dados ou o restaurante e
            seu cardápio filtrado. Se a API responder com status diferente de
            200, contém a chave `Erro` com o status e o corpo da resposta.
    """
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()

        if restaurante is None:
            return {"Dados": dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "descricao": item['description']
                })
        return {'Restaurante' : restaurante, 'Cardapio': dados_restaurante}

    else:
        return {'Erro': f'{response.status_code} - {response.text}'}
