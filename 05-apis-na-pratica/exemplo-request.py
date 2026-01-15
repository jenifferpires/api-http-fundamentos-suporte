import requests

# ============================================
# Exemplo prático de request HTTP usando Python
# Foco: Suporte a Aplicações / Diagnóstico
# ============================================

# URL da API (endpoint)
url = "https://api.sistema.com/api/clientes/123"

# Headers da requisição
headers = {
    "Authorization": "Bearer token_exemplo",
    "Content-Type": "application/json"
}

# Payload (dados enviados)
payload = {
    "nome": "Empresa X",
    "email": "contato@empresa.com",
    "ativo": True
}

try:
    # Envio da requisição PUT
    response = requests.put(url, json=payload, headers=headers)

    # Exibe o status code retornado
    print(f"Status Code: {response.status_code}")

    # Tratamento básico baseado no status code
    if response.status_code == 200:
        print("Cadastro atualizado com sucesso.")
        print("Resposta da API:")
        print(response.json())

    elif response.status_code == 400:
        print("Erro 400 - Requisição inválida.")
        print("Verifique o payload enviado.")
        print(response.text)

    elif response.status_code == 401:
        print("Erro 401 - Não autorizado.")
        print("Token inválido ou expirado.")

    elif response.status_code == 403:
        print("Erro 403 - Acesso negado.")
        print("Usuário autenticado, mas sem permissão.")

    elif response.status_code == 404:
        print("Erro 404 - Recurso não encontrado.")
        print("Verifique o endpoint ou o ID.")

    elif response.status_code >= 500:
        print("Erro no servidor (5xx).")
        print("Problema interno na API.")
        print(response.text)

    else:
        print("Resposta inesperada:")
        print(response.text)

except requests.exceptions.RequestException as error:
    print("Erro ao tentar se comunicar com a API.")
    print(error)

🧠 EXPLICAÇÃO CONCEITUAL (ligando com tudo que você viu) 
1️⃣ import requests 

Biblioteca usada para fazer requisições HTTP em Python.  

📌 Em suporte: 

Muito usada para testar APIs 

Simular chamadas de app ou integração 

Reproduzir erros reportados por clientes 

2️⃣ URL (endpoint) 

url = "https://api.sistema.com/api/clientes/123"

✔ Recurso: clientes 
✔ ID: 123 

👉 Se isso estiver errado → 404 

3️⃣ Headers
headers = {
    "Authorization": "Bearer token_exemplo",
    "Content-Type": "application/json"
}


👉 Aqui entram os erros mais comuns:

Token errado → 401

Header ausente → 400 / 401

4️⃣ Payload
payload = {
    "nome": "Empresa X",
    "email": "contato@empresa.com",
    "ativo": True
}


👉 Se faltar campo obrigatório → 400
👉 Se tipo estiver errado → erro de validação

5️⃣ Envio da requisição
response = requests.put(url, json=payload, headers=headers)


✔ Método: PUT
✔ JSON automaticamente serializado
✔ Headers enviados corretamente

6️⃣ Leitura do status code
```python
response.status_code

```

7️⃣ Tratamento de erros

O if / elif simula exatamente o raciocínio: 

2xx → sucesso 

4xx → erro de requisição/autenticação 

5xx → erro interno 


8️⃣ Tratamento de exceções  
except requests.exceptions.RequestException as error:  


📌 Captura:  

API fora do ar  
Timeout  
DNS  
Falha de rede.  

👉 Cenário real de suporte / infraestrutura.  