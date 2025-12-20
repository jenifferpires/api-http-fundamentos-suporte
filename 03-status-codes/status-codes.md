# Status Codes HTTP – Como interpretar erros em Suporte

## O que são Status Codes?

Os **Status Codes HTTP** são códigos numéricos retornados pelo servidor para indicar o **resultado de uma requisição**.

Eles permitem que o cliente (app, navegador, sistema) saiba se a requisição:
- Foi bem-sucedida
- Teve erro
- Não pôde ser processada

Para suporte técnico, os status codes são uma das **principais pistas de diagnóstico**.

---

## Categorias de Status Codes

Os códigos HTTP são agrupados por categoria:

| Categoria | Significado geral |
|--------|------------------|
| 2xx | Sucesso |
| 3xx | Redirecionamento |
| 4xx | Erro do cliente (requisição) |
| 5xx | Erro do servidor (backend) |

---

## 2xx – Sucesso

Indicam que a requisição foi processada corretamente.

### Exemplos comuns:

- **200 OK**  
Requisição executada com sucesso.

- **201 Created**  
Recurso criado com sucesso (muito comum em POST).

📌 Em suporte:
> Se o cliente recebe 2xx mas relata erro visual, o problema **geralmente está na interface**, não na API.

---

## 3xx – Redirecionamento

Indicam que a requisição precisa seguir outro caminho.

- **301 / 302** – Redirecionamento permanente ou temporário

📌 Em suporte:
- Muito comum em problemas de ambiente (URL errada, redirecionamento inesperado).

---

## 4xx – Erro do cliente (requisição)

Indicam que **algo enviado pelo cliente está incorreto**.

### Os mais comuns em suporte:

- **400 Bad Request**  
Dados inválidos, campos ausentes ou formato incorreto.

- **401 Unauthorized**  
Problema de autenticação (token inválido ou expirado).

- **403 Forbidden**  
Usuário autenticado, mas sem permissão.

- **404 Not Found**  
Recurso ou endpoint inexistente.

📌 Leitura correta em suporte:
> Erros 4xx normalmente indicam que **o backend recebeu a requisição**, mas **não conseguiu processá-la por erro no que foi enviado**.

---

## 5xx – Erro do servidor (backend)

Indicam que **a requisição está correta**, mas o servidor falhou ao processá-la.

### Os mais comuns:

- **500 Internal Server Error**  
Erro genérico no backend.

- **502 Bad Gateway**  
Falha de comunicação entre serviços.

- **503 Service Unavailable**  
Serviço indisponível ou sobrecarregado.

📌 Leitura correta em suporte:
> Erros 5xx indicam falha interna e geralmente precisam de análise do time técnico ou infraestrutura.

---

## Diferença prática: 400 x 500

| Código | Onde está o problema? |
|-----|----------------------|
| 400 | Na requisição enviada |
| 500 | No servidor / backend |

Essa distinção é fundamental para:
- Direcionar corretamente o chamado
- Evitar retrabalho
- Comunicar melhor com cliente e desenvolvimento

---

## Exemplo real de suporte

### Requisição

```http
POST /api/clientes HTTP/1.1
Content-Type: application/json

{
  "email": "cliente@empresa.com"
}


```
Resposta
```http
400 Bad Request
```

📌 Diagnóstico:

Campo obrigatório ausente (nome)

Erro no payload enviado

Conclusão
Os status codes HTTP são uma das ferramentas mais importantes para suporte técnico.

Eles permitem:

Diagnóstico rápido

Identificação da origem do erro

Comunicação clara com o cliente e com o time técnico

Entender status codes é essencial para atuar com aplicações web, APIs e integrações.


---
