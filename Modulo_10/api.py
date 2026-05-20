import requests

# =========================
# CONFIGURAÇÃO DA API
# =========================

API_KEY = "SUA_API_KEY"
cidade = "São Paulo"

# URL da API
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

# =========================
# REQUISIÇÃO
# =========================

try:
    resposta = requests.get(url)

    # Verifica se deu erro
    resposta.raise_for_status()

    dados = resposta.json()

    # =========================
    # EXIBINDO INFORMAÇÕES
    # =========================

    temperatura = dados["main"]["temp"]
    clima = dados["weather"][0]["description"]
    umidade = dados["main"]["humidity"]

    print("\n===== PREVISÃO DO TEMPO =====")
    print(f"Cidade: {cidade}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Clima: {clima}")
    print(f"Umidade: {umidade}%")

# =========================
# TRATAMENTO DE ERROS
# =========================

except requests.exceptions.HTTPError:
    print("Erro HTTP na requisição.")

except requests.exceptions.ConnectionError:
    print("Erro de conexão com a internet.")

except requests.exceptions.Timeout:
    print("Tempo de conexão esgotado.")

except requests.exceptions.RequestException as erro:
    print(f"Erro: {erro}")
