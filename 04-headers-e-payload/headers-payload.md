# Headers e Payload – Onde muitos erros de integração acontecem

## O que são Headers HTTP?

Headers são **informações adicionais** enviadas junto com a requisição HTTP.  
Eles não fazem parte do conteúdo principal (payload), mas **instruem o servidor sobre como interpretar a requisição**.

Em suporte técnico, erros de headers estão entre as **principais causas de falha em integrações**, mesmo quando o endpoint e o método estão corretos.

---

## Headers mais comuns em aplicações:

### Authorization

Usado para **autenticação e autorização** da requisição. 

Exemplo: 
```http
Authorization: Bearer token_exemplo
```

📌 Problemas comuns em suporte:    

Token expirado.  
Token inválido.  
Header não enviado.  
Token enviado no formato errado.  

📌 Resultados mais comuns:    
 
401 Unauthorized   
403 Forbidden   

Content-Type  

Indica o formato do corpo da requisição (payload).

Exemplo:  
```http
Content-Type: application/json
```

📌 Problemas comuns:  

Content-Type ausente.  
Content-Type incorreto.  
Backend esperando JSON e recebendo outro formato.  

📌 Resultado comum:   

400 Bad Request    

Outros headers frequentes:

Accept  
User-Agent  
Cache-Control  

📌 Em suporte, esses headers ajudam a identificar:  

Tipo de cliente (app mobile, navegador, integração externa).  
Versão da aplicação.  
Problemas relacionados a cache ou comportamento inesperado.  

O que é Payload?  

Payload é o conteúdo principal enviado na requisição, geralmente em JSON.  
Ele é utilizado principalmente nos métodos:  

POST   
PUT   
PATCH   

Exemplo de payload correto:    

```http
{
  "nome": "Empresa X",
  "email": "contato@empresa.com",
  "ativo": true
}
```
Erros comuns em payload (muito frequentes em suporte): 
Campo obrigatório ausente. 

```http
{
  "email": "contato@empresa.com"
} 
```

📌 Resultado comum: 

400 Bad Request. 

Tipo de dado incorreto:
```json
{
  "ativo": "true"
}
```
📌 Se o backend espera boolean:   

Pode gerar erro de validação.  
Pode gerar comportamento inesperado.   
Estrutura diferente da esperada.   

```http 
{
  "cliente": {
    "nome": "Empresa X"
  }
}
```

📌 Se a API espera o campo no nível raiz:    

Erro de validação.    
Erro de mapeamento no backend.    
Relação entre Headers, Payload e Suporte Técnico.    
 
Em muitos chamados de suporte:    

Endpoint está correto.     
Método HTTP está correto.   
Headers ou payload estão incorretos.   

Por isso, o suporte técnico deve sempre validar nesta ordem:   

Método HTTP    
Endpoint     
Headers     
Payload     

Exemplo real de diagnóstico em suporte:     

Requisição   
```http
POST /api/clientes HTTP/1.1
Content-Type: application/json
Authorization: Bearer token_expirado

{
  "nome": "Empresa X",
  "email": "contato@empresa.com"
} 
```
Resposta    
```http
401 Unauthorized
```

📌 Diagnóstico:   

Endpoint correto.   
Método correto.   
Payload válido.   
Erro no token de autenticação (Authorization).   

Conclusão:   

Headers e payload são fontes frequentes de erro em aplicações e integrações.   

Entender esses conceitos permite ao suporte:  

Diagnosticar falhas com mais precisão.   
Evitar abertura desnecessária de bugs.   
Comunicar problemas de forma clara com clientes e desenvolvedores.   

Esse conhecimento é essencial para quem trabalha com APIs e sistemas integrados.   