# Métodos HTTP – Como e quando usar (visão de Suporte)

## O que são métodos HTTP?

Os métodos HTTP indicam **qual ação o cliente deseja executar** sobre um recurso no servidor. Em suporte a aplicações, entender esses métodos ajuda a identificar a intenção do usuário e onde o fluxo pode ter falhado.

---

## Principais métodos HTTP (Os mais importantes)

| Verbo | Para que serve | Exemplo Real | Idempotente? |
| :--- | :--- | :--- | :--- |
| **GET** | Buscar dados | Ver saldo da conta | Sim |
| **POST** | Criar algo | Cadastrar novo cliente | Não |
| **PUT** | Atualizar tudo | Alterar cadastro completo | Sim |
| **PATCH** | Atualizar parte | Alterar apenas o e-mail | Não |
| **DELETE** | Remover | Excluir uma conta | Sim |

---

### 🔍 Detalhamento Técnico:

#### GET – Buscar informações
Usado estritamente para consulta.
* **📌 Erros comuns:** `404` (ID pesquisado não existe) ou `401` (sessão expirada).

#### POST – Criar um novo recurso
Envia dados no corpo (body) da requisição para criar algo novo.
* **📌 Erros comuns:** `400` (falta de campos obrigatórios) ou `409` (conflito/duplicidade).

#### PUT vs PATCH – Atualizações
* **PUT:** Substitui o recurso inteiro. Se você esquecer um campo, ele pode ser apagado ou ficar em branco.
* **PATCH:** Altera apenas o que foi enviado. É mais seguro para atualizações rápidas.

#### DELETE – Remover um recurso
Solicita a exclusão de um registro.
* **📌 Nota de Suporte:** Muitos sistemas usam "Soft Delete", onde o dado é apenas desativado, mas o método HTTP continua sendo o DELETE.

---

## 🛠️ Relação com chamados de Suporte

| Situação do Chamado | Método Envolvido |
| :--- | :--- |
| Tela de listagem não carrega dados | **GET** |
| Erro ao clicar em "Salvar Novo" | **POST** |
| Cadastro não atualiza após edição | **PUT / PATCH** |
| Erro ao tentar cancelar/excluir | **DELETE** |

---
*Este documento ajuda o suporte a reproduzir o erro exatamente como o cliente o gerou.*