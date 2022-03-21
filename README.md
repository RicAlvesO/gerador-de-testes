# Gerador de testes de programação

Gerador de testes modelo para várias linguagens de programação.

## Tabela de Conteúdos

- **[Linguages](#Linguages)**
- **[Requisitos](#Requisitos)**
- **[Como Utilisar](#Como-Utilisar)**
- **[Como Pode Contribuir](#Como-Pode-Contribuir)**

## Linguagens

Atualmente o programa suporta as seguintes linguagens:
    - C
    - Haskell
    - Java

No entanto algumas destas podém ainda não conter um dataset dde perguntas suficientes para os testes.

`NOTA:O total de perguntas pode ser consultado no menu do programa!`

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

Para limpar os testes gerados anteriormente e as suas respostas pode executar o comando:
- `make clean`

## Como Pode Contribuir

Atualmente a quantidade das perguntas, bem como a sua complexidade deixa a desejar, visto isso, para além da implementação de novas funcionalidades, agradeçe-se a nova contribuição de perguntas, respostas e exemplos.

De modo a adicionar novas perguntas deve correr o comando:

- `make adder`

`NOTA: Atualmente as perguntas e respostas são armazenadas localmente em ficheiros .JSON`