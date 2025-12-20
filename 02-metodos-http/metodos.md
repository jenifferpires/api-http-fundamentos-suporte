# Métodos HTTP – Como e quando usar (visão de Suporte)

## O que são métodos HTTP?

Os métodos HTTP indicam **qual ação o cliente deseja executar** sobre um recurso no servidor.

Em suporte a aplicações, entender os métodos HTTP ajuda a responder perguntas como:
- O cliente está apenas consultando dados?
- Está tentando criar algo novo?
- Está atualizando ou excluindo informações?

Cada método tem um propósito específico, e o uso incorreto geralmente gera erros.

---

## Principais métodos HTTP

### GET – Buscar informações

O método **GET** é usado para **consultar dados**.

📌 Características:
- Não altera dados no servidor
- Não possui body (na maioria dos casos)
- Pode ser repetido sem causar efeitos colaterais

📌 Exemplos reais em suporte:
- Buscar lista de clientes
- Consultar pedidos
- Abrir uma tela de cadastro já existente

📌 Exemplo:
```http
GET /api/clientes/123 HTTP/1.1
Host: api.sistema.com
Authorization: Bearer token_valido
📌 Erros comuns:

401 (token inválido)

404 (ID não encontrado)

POST – Criar um novo recurso
O método POST é usado para criar dados novos no servidor.

📌 Características:

Envia informações no body

Pode gerar duplicidade se chamado mais de uma vez

Muito usado em formulários

📌 Exemplos reais em suporte:

Criar cliente

Criar pedido

Enviar formulário

📌 Exemplo:

http
Copiar código
POST /api/clientes HTTP/1.1
Content-Type: application/json

{
  "nome": "Empresa X",
  "email": "contato@empresa.com"
}
📌 Erros comuns:

400 (campo obrigatório ausente)

409 (registro já existe)

PUT – Atualizar um recurso por completo
O método PUT é usado para atualizar totalmente um recurso existente.

📌 Características:

Normalmente exige todos os campos

Substitui o recurso anterior

📌 Exemplos reais em suporte:

Atualizar cadastro completo

Substituir configurações

📌 Exemplo:

http
Copiar código
PUT /api/clientes/123 HTTP/1.1
Content-Type: application/json

{
  "nome": "Empresa X",
  "email": "novo@email.com",
  "ativo": true
}
📌 Erros comuns:

400 (campo ausente)

404 (ID não existe)

PATCH – Atualizar parcialmente um recurso
O método PATCH é usado para atualizações parciais.

📌 Características:

Atualiza apenas os campos enviados

Mais flexível que PUT

📌 Exemplos reais em suporte:

Alterar status

Atualizar apenas email ou telefone

📌 Exemplo:

http
Copiar código
PATCH /api/clientes/123 HTTP/1.1
Content-Type: application/json

{
  "ativo": false
}
📌 Erros comuns:

400 (campo inválido)

403 (sem permissão para alterar)

DELETE – Remover um recurso
O método DELETE é usado para excluir dados.

📌 Características:

Pode ser reversível ou não (depende da regra de negócio)

Nem sempre remove fisicamente (soft delete)

📌 Exemplos reais em suporte:

Excluir usuário

Cancelar pedido

Inativar cadastro

📌 Exemplo:

http
Copiar código
DELETE /api/clientes/123 HTTP/1.1
Authorization: Bearer token_valido

📌 Erros comuns:

403 (sem permissão)

404 (ID inexistente)

Relação dos métodos HTTP com chamados de suporte
Situação do chamado	Método envolvido
Tela não carrega dados	GET
Erro ao salvar formulário	POST
Falha ao atualizar cadastro	PUT / PATCH
Erro ao excluir registro	DELETE

Entender isso ajuda o suporte a:

Investigar corretamente

Reproduzir o erro

Comunicar melhor com o time técnico

Conclusão
Os métodos HTTP definem o tipo de ação realizada em uma aplicação.

Para suporte, compreender os métodos significa:

Diagnosticar problemas com mais precisão

Evitar análises superficiais

Atuar de forma mais técnica e segura

Esse conhecimento é essencial para quem trabalha com aplicações web, APIs e integrações.


---
