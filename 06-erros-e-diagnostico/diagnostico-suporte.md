# 🔍 Diagnóstico de Erros em APIs – Guia de Sobrevivência para Suporte. 

O suporte técnico é a "linha de frente" da investigação. Seu papel não é apenas repassar o erro, mas diagnosticar a origem da falha e garantir que o chamado chegue ao destino correto com todas as evidências necessárias.

---

## 🧭 1. Fluxo de Investigação (Checklist). 

Antes de escalar qualquer problema para o time de desenvolvimento, percorra este caminho:

1.  **Status do Serviço:** A API está respondendo? (Verifique se não é uma queda de infra).
2.  **Endpoint:** A URL está correta e aponta para o ambiente certo (Produção vs Homologação)?
3.  **Método:** O verbo utilizado (GET, POST, etc.) condiz com a ação?
4.  **Autenticação:** O token no Header está presente e é válido?
5.  **Contrato (Payload):** Os campos enviados no JSON batem com a documentação?
6.  **Reprodutibilidade:** O erro acontece sempre ou foi uma instabilidade momentânea?



---

## 🚦 2. Classificação de Ações por Categoria. 

### Erros 4xx (Responsabilidade do Cliente/Integrador)
* **Ação:** Consultar a documentação e orientar o cliente.
* **Exemplo:** Se o cliente recebe `400 Bad Request`, peça para ele revisar o preenchimento dos campos.

### Erros 5xx (Responsabilidade do Sistema/Infra)
* **Ação:** Coletar logs e abrir um incidente interno.
* **Exemplo:** Se o cliente recebe `500 Internal Server Error`, o problema está no código do backend ou banco de dados.

---

## 📝 3. Como Documentar um Incidente (Template de Suporte)

Para que o time de desenvolvimento resolva o problema rápido, o ticket deve ser técnico e objetivo. Use este modelo:

* **Ambiente:** (Ex: Produção)
* **Horário do erro:** (Ex: 15:45 - Horário de Brasília)
* **Endpoint:** `POST https://api.sistema.com/v1/pagamentos`
* **Evidência (Payload):**
    ```json
    { "valor": 100, "moeda": "BRL" }
    ```
* **Resposta (Status + Body):** `500 Internal Server Error` - `{ "message": "Null pointer exception" }`

---

## 🗣️ 4. Tradução Técnica: Cliente vs. Desenvolvedor. 

Saber falar com cada público é uma habilidade sênior:

| Para o Cliente (Linguagem Clara) | Para o Desenvolvedor (Linguagem Técnica) |
| :--- | :--- |
| "Seu login expirou, por favor, entre novamente." | "Requisição retornando 401 com token expirado." |
| "Falta preencher o campo 'CPF' no formulário." | "Payload incompleto gerando 400 Bad Request." |
| "Estamos com uma instabilidade interna em nosso servidor." | "Endpoint /v1/pix retornando 503 Service Unavailable." |

---

## ✅ Conclusão

Um bom suporte não apenas relata que "algo não funciona", mas aponta **onde** e **por que** não funciona.  
Ao dominar o diagnóstico de APIs, você reduz o tempo médio de atendimento (TMA) e ganha o respeito das equipes de engenharia.

---
*Este é o módulo final do curso básico de APIs para Suporte Técnico.*