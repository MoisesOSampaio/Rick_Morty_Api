import requests

class Request:
    @staticmethod
    def getData(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Levanta um erro se o status não for 200
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return {"error": "Erro ao buscar personagem", "details": str(e)}
        