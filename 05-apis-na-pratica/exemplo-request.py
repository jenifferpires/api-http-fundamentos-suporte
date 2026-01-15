import requests

# ==============================================================================
# Exemplo Prático de Request HTTP usando Python
# Objetivo: Demonstrar o fluxo de uma requisição PUT e o diagnóstico de respostas.
# Foco: Suporte a Aplicações / Troubleshooting de APIs.
# ==============================================================================

# 1. URL (Endpoint): Recurso 'clientes' com o ID '123'
url = "https://api.sistema.com/api/clientes/123"

# 2. Headers: Metadados para Autenticação e Formato de Dados
headers = {
    "Authorization": "Bearer token_exemplo",
    "Content-Type": "application/json"
}

# 3. Payload: Dados enviados no corpo da requisição
payload = {
    "nome": "Empresa X",
    "email": "contato@empresa.com",
    "ativo": True
}

try:
    # 4. Envio da requisição utilizando o método PUT
    # O parâmetro 'json=' já faz a serialização correta do dicionário Python para JSON.
    response = requests.put(url, json=payload, headers=headers)

    # 5. Leitura do Status Code para Diagnóstico
    print("-" * 30)
    print(f"DEBUG SUPORTE - Status Code: {response.status_code}")
    print("-" * 30)

    # 6. Fluxo de Decisão baseado no Status Code
    if response.status_code == 200:
        print("✅ Sucesso: Cadastro atualizado.")
        print(f"Resposta: {response.json()}")

    elif response.status_code == 400:
        print("❌ Erro 400 (Bad Request): Requisição inválida.")
        print("Ação: Validar se todos os campos obrigatórios estão no Payload.")

    elif response.status_code == 401:
        print("❌ Erro 401 (Unauthorized): Falha na autenticação.")
        print("Ação: Verificar se o token de Authorization expirou.")

    elif response.status_code == 403:
        print("❌ Erro 403 (Forbidden): Sem permissão.")
        print("Ação: Validar o perfil de acesso do usuário.")

    elif response.status_code == 404:
        print("❌ Erro 404 (Not Found): Recurso não localizado.")
        print("Ação: Validar se o ID 123 existe no banco de dados.")

    elif response.status_code >= 500:
        print("🔥 Erro 5xx (Server Error): Falha interna no servidor.")
        print("Ação: Escalar para o time de Desenvolvimento/Infraestrutura.")

except requests.exceptions.RequestException as error:
    # 7. Tratamento de Exceções de Rede
    print("⚠️ Erro de Conexão: Falha ao tentar se comunicar com a API.")
    print(f"Detalhes: {error}")