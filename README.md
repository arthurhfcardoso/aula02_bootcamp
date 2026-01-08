# aula02_bootcamp

## Objetivo

README focado no meu aprendizado da aula 02 e no que eu implementei.

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python exercicios.py ex01
```

Troque `ex01` por `ex02`, `ex03`, etc.

## Estrutura dos exercicios

Cada exercicio virou uma funcao `exNN()` dentro de `exercicios.py`.
Para rodar um exercicio especifico, eu passo o nome no terminal e o script
chama a funcao correspondente.

Exemplo:

```bash
python exercicios.py ex10
```

## O que eu pratiquei

- Entrada e saida com `input()` e `print()`
- Conversao de tipos: `int`, `float`, string para booleano
- Operadores matematicos: `+ - * / // % **`
- Strings: `upper`, `lower`, `strip`, `split`, concatenacao
- Logica booleana: `and`, `or`, `not`, comparacoes
- Controle de fluxo: `if/elif/else`
- Tratamento de erro com `try/except`

## Dificuldades e aprendizados

- Aprendi que `input()` sempre retorna string e precisa converter.
- Entendi que `True` e `False` sao os unicos booleanos reais.
- Percebi que `bool("false")` vira `True`, entao tive que comparar texto.
- Divisao inteira pode dar 0 quando o numerador e menor que o denominador.
- `try/except` evita que o programa quebre com entradas invalidas e permite
  mostrar mensagens mais claras.

## Arquivos principais

- `exercicios.py`: minhas solucoes dos exercicios.
