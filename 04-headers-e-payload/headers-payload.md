# Headers e Payload – Onde o erro se esconde

## 🧐 O que são Headers e Payload?

Em uma requisição HTTP, podemos separar a mensagem em duas partes principais:
1. **Headers (Cabeçalhos):** Instruções de "como" a mensagem deve ser lida (metadados).
2. **Payload (Corpo):** A informação "o que" está sendo enviado de fato (dados).

---

## 🛠️ 1. Headers Comuns (O checklist do Suporte)

Muitas integrações falham não pelo conteúdo, mas pela "instrução" de envio.

| Header | Função | Erro comum em Suporte |
| :--- | :--- | :--- |
| **Authorization** | Credenciais de acesso | Token expirado ou formato `Bearer` ausente. |
| **Content-Type** | Formato do dado enviado | Esquecer de definir como `application/json`. |
| **Accept** | Formato que o cliente aceita | API retornar XML quando o cliente só lê JSON. |
| **User-Agent** | Identifica quem está pedindo | Bloqueio de segurança se o "sistema" for desconhecido. |

> **📌 Insight de Suporte:** Se o status code for **401** ou **403**, sua primeira parada de investigação deve ser o Header de **Authorization**.

---

## 📦 2. Payload (O Corpo da Requisição)

O Payload é onde enviamos os dados, geralmente no formato **JSON**.

### Checklist de Erros de Payload:
* **Campos Obrigatórios:** Faltou o `e-mail` ou `CPF`? (Gera erro 400).
* **Tipagem Incorreta:** Enviar um número onde se espera texto, ou `"true"` (texto) onde se espera `true` (boolean).
* **Sintaxe do JSON:** Falta de vírgulas, aspas ou chaves desalinhadas.



---

## 🔍 3. Relação Prática no Troubleshooting

Um analista de suporte eficiente valida a requisição nesta ordem lógica:

1. **Método:** (O verbo está certo para a ação?)
2. **Endpoint:** (A URL está correta?)
3. **Headers:** (O token e o formato estão lá?)
4. **Payload:** (Os dados estão completos e sem erros de digitação?)

### Exemplo Real de Diagnóstico

**Requisição enviada:**
```http
POST /api/clientes HTTP/1.1
Content-Type: application/json
Authorization: Bearer token_valido

{
  "nome": "Empresa X"
  "email": "contato@empresa.com"
}
```

Resposta do Servidor: 
```
400 Bad Request
```

Diagnóstico do Suporte:   
Observe o payload acima. Falta uma vírgula após "Empresa X".   
O servidor não conseguiu ler o JSON por erro de sintaxe.   
Ação: Corrigir a pontuação no envio dos dados.  

Dominar a leitura de Headers e Payload evita que problemas simples de preenchimento sejam escalados como bugs para o time de desenvolvimento.  