# API & HTTP – Fundamentos para Suporte Técnico

Este repositório foi criado com o objetivo de consolidar e demonstrar conhecimentos práticos sobre **HTTP, APIs e diagnóstico de erros**, com foco direto na **rotina de suporte técnico, sustentação de aplicações e análise de incidentes**.

O conteúdo é organizado de forma **didática**, mas sempre conectado a **cenários reais enfrentados por times de suporte**, integrações de sistemas e troubleshooting de APIs.

---

## 🎯 Objetivo do Repositório

- Compreender como funciona a comunicação HTTP
- Entender APIs do ponto de vista de **quem dá suporte**
- Diagnosticar erros de integração com mais rapidez
- Interpretar corretamente **status codes, headers e payloads**
- Servir como material de estudo e também **portfólio técnico**

Este repositório não tem foco em desenvolvimento avançado de APIs, mas sim em **análise, leitura e diagnóstico**, habilidades essenciais para profissionais de suporte e sustentação.

---

## 🧩 Estrutura do Conteúdo

O material está dividido em módulos progressivos:

### 📘 01 – HTTP Básico
📁 `01-http-basico/`

Introduz os conceitos fundamentais:
- O que é HTTP
- Como funciona uma requisição e uma resposta
- Comunicação cliente ↔ servidor
- Onde normalmente surgem problemas em produção

Arquivo:
- `conceitos-http.md`

---

### 📗 02 – Métodos HTTP
📁 `02-metodos-http/`

Explica os principais métodos usados em APIs:
- GET
- POST
- PUT
- PATCH
- DELETE

Com foco em:
- Quando cada método deve ser usado
- Erros comuns causados por método incorreto
- Impacto direto no suporte técnico

Arquivo:
- `metodos.md`

---

### 📙 03 – Status Codes HTTP
📁 `03-status-codes/`

Um dos módulos mais importantes para suporte.

Aborda:
- Diferença entre erros 4xx e 5xx
- Significado dos principais status codes
- Como interpretar rapidamente uma falha
- O que é erro de cliente x erro de servidor

Arquivo:
- `status-codes.md`

---

### 📕 04 – Headers e Payload
📁 `04-headers-e-payload/`

Onde grande parte dos erros de integração acontecem.

Conteúdo:
- Headers HTTP (Authorization, Content-Type, etc.)
- Payload e estrutura de dados
- Erros comuns de autenticação e validação
- Relação direta entre headers incorretos e falhas de requisição

Arquivo:
- `headers-payload.md`

---

### 📒 05 – APIs na Prática
📁 `05-apis-na-pratica/`

Demonstra exemplos reais de requisição:
- Estrutura completa de uma chamada HTTP
- Exemplo documentado em Markdown
- Exemplo prático em Python

Arquivos:
- `guia-definitivo-apis.md` (Guia mestre de conceitos e diagnóstico)
- `exemplo-request.md` (Documentação de uma chamada real)
- `exemplo-request.py` (Script de automação/teste)

Este módulo conecta teoria e prática, consolidando o conhecimento para o dia a dia.

---

### 📓 06 – Erros e Diagnóstico
📁 `06-erros-e-diagnostico/`

Foco total em troubleshooting.

Aborda:
- Como analisar um erro de API
- Ordem correta de verificação (método, endpoint, headers, payload)
- Diferença entre falha de integração e bug
- Comunicação clara com clientes e times de desenvolvimento

Arquivo:
- `diagnostico-suporte.md`

---

## 🛠 Público-Alvo

Este repositório é voltado para:
- Suporte Técnico
- Sustentação de Aplicações
- Analistas de Sistemas
- Profissionais que lidam com APIs e integrações
- Pessoas em transição para áreas técnicas

---

## 🚀 Como usar este repositório

- Leia os módulos em ordem
- Utilize os exemplos práticos como referência
- Consulte durante atendimentos e análises de incidentes
- Use como material de revisão para entrevistas técnicas

---

## 📌 Considerações finais

Dominar HTTP e APIs do ponto de vista de suporte técnico permite:
- Reduzir tempo de diagnóstico
- Evitar abertura de bugs desnecessários
- Comunicar problemas com mais clareza
- Atuar de forma mais estratégica em incidentes

Este repositório representa um aprendizado **prático, estruturado e orientado a problemas reais** enfrentados em ambientes de produção.
