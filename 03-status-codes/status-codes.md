# Status Codes HTTP – Como interpretar erros em Suporte

## O que são Status Codes?

Os **Status Codes HTTP** são códigos numéricos retornados pelo servidor para indicar o **resultado de uma requisição**. Para o suporte técnico, eles funcionam como o "RG" do problema: dizem imediatamente se a falha é de quem pediu (Cliente) ou de quem processou (Servidor).

---

## 🚦 Categorias e Ações de Suporte:

| Categoria | Significado | Quem errou? | Ação Sugerida |
| :--- | :--- | :--- | :--- |
| **2xx** | Sucesso | Ninguém | Validar se o dado refletiu na tela/UI. |
| **3xx** | Redirecionamento | - | Verificar se a URL ou ambiente estão corretos. |
| **4xx** | Erro do Cliente | O Cliente/App | Validar dados, tokens e permissões enviados. |
| **5xx** | Erro do Servidor | O Sistema/Infra | Acionar time técnico ou verificar logs. |

---

## 🔍 Detalhamento por Categoria:

### 🟢 2xx – Sucesso
* **200 OK:** Sucesso total.
* **201 Created:** Sucesso na criação (comum após um POST).
* **💡 Insight de Suporte:** Se o status é 2xx mas a tela não mostra o que deveria, o problema é no **Front-end** (exibição) e não na API.

### 🟡 4xx – Erro do Cliente (Foco no Payload/Acesso)
Estes são os mais comuns em chamados de integração:
* **400 Bad Request:** Dados inválidos ou faltando (ex: e-mail sem @).
* **401 Unauthorized:** Problema de autenticação (Token inválido ou expirado).
* **403 Forbidden:** O usuário logou, mas não tem o "perfil" necessário para aquela ação.
* **404 Not Found:** O recurso não existe (ID inválido) ou a URL está errada.

### 🔴 5xx – Erro do Servidor (Foco na Infra/Código)
Indica que o pedido foi correto, mas o sistema falhou:
* **500 Internal Server Error:** O backend "travou" ou deu erro de código.
* **502 / 504 Gateway Timeout:** O servidor demorou muito para responder ou está fora do ar.
* **💡 Insight de Suporte:** Estes erros exigem a coleta de **Logs** para o time de desenvolvimento.

---



## 📝 Exemplo de Diagnóstico em Suporte:s

**Cenário:** Cliente tenta cadastrar um novo usuário e recebe **400 Bad Request**.

**Análise técnica:**
1. Verificamos o método: `POST`.
2. Verificamos o body enviado: O campo `nome` estava vazio.
3. **Conclusão:** Não é um bug do sistema. É um erro de preenchimento.
4. **Ação:** Orientar o cliente a preencher o campo obrigatório.

---
*Dominar os status codes reduz drasticamente o tempo de diagnóstico e evita escalonamentos desnecessários para o time de desenvolvimento.*