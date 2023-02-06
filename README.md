# Gerador de testes de programação

Gerador de testes modelo para várias linguagens de programação.

## Tabela de Conteúdos

- **[Requisitos](#requisitos)**
- **[Como Utilisar](#como-utilizar)**
- **[Licença](#licença)**

## Requisitos

Este projeto foi desenvolvido utilizando `Python 3.10+`.

De modo a garantir que possuí os requisitos necessários para este projeto deve correr o comando:

`make setup`

## Como Utilizar

De modo a executar este programa deve correr o ficheiro `src/gen.py`. Para tal pode recorrer aos comandos:
- `make` (Verifica requisitos e executa o programa)
- `make run` (Executa o programa)

Durante a execução será deparado com um menu para escolher a linguagem desejada para o teste e a quantidade de perguntas.

Após escolher os items desejados será gerada na pasta `output/testes` um novo teste, identificado pela data & hora atual, e seguindo a mesma estrutura, uma sugestão de resolução deste na pasta `output/resolucoes`.

As perguntas são classificadas conforme a sua dificuldade. Isto é, ao gerar o teste é lhe atribuido uma dificuldade global que serve para ajudar a classificar as perguntas mais uniformemente.
Assim, as cotaçãoes são relativas ao teste gerado e não tem um significado único global.

Para limpar os testes gerados anteriormente e as suas respostas pode executar o comando:
- `make clean`

## Licença

Copyright (c) 2022, Ricardo O.

Este projeto está licenciado sob a Licença MIT - veja o ficheiro LICENSE para detalhes.
