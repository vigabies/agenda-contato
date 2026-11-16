# Agenda de Contatos

Aplicação de terminal em Python para gerenciar uma lista de contatos. Os dados ficam apenas na memória e são perdidos ao fechar o programa.

## Funcionalidades

- Menu com lista de opções, onde o usuário digita a escolha para iniciar a ação
- Adicionar contato (nome, telefone, email e favorito)
- Visualizar a lista de contatos cadastrados
- Editar um contato existente
- Marcar/desmarcar um contato como favorito
- Visualizar a lista de contatos favoritos
- Apagar um contato (com confirmação)

## Como rodar

É necessário ter o [Python 3](https://www.python.org/downloads/) instalado. Não há bibliotecas externas.

```bash
git clone https://github.com/vigabies/agenda-contatos.git
cd agenda-contatos
python agenda_contatos.py
```

No Windows, se `python` não funcionar, tente `py agenda_contatos.py`.

## Exemplo de uso

```
===== AGENDA DE CONTATOS =====
1 - Adicionar contato
2 - Ver todos os contatos
3 - Editar contato
4 - Marcar/desmarcar favorito
5 - Ver contatos favoritos
6 - Apagar contato
0 - Sair
Escolha uma opção: 2

--- TODOS OS CONTATOS ---
1. ★ Ana | Tel: 11999999999 | Email: ana@email.com
2. ☆ Bia | Tel: 11988888888 | Email: bia@email.com
```

A estrela cheia (★) indica contato favorito e a vazia (☆) indica contato comum.

## Estrutura

```
agenda-contatos/
├── agenda_contatos.py
└── README.md
```
