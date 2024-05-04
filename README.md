# API de Zoológico em Python

Este projeto implementa uma API simples para um zoológico virtual em Python, utilizando a metodologia de desenvolvimento orientada a testes (TDD). A API permite realizar as seguintes operações:

- Criação de animais com nome, espécie e nível de felicidade.
- Criação de recintos para abrigar animais da mesma espécie, com diferentes níveis de cuidados.
- Alimentação dos animais para aumentar ou diminuir sua felicidade.
- Recebimento de visitantes no zoológico, com base na felicidade dos animais e nos recintos bem cuidados.

## Estrutura do Projeto

- animal.py: Define a classe Animal.
- recinto.py: Define a classe Recinto.
- zoo.py: Implementa a classe Zoo e a API do zoológico.
- test_animal.py: Testes unitários para a classe Animal.
- test_recinto.py: Testes unitários para a classe Recinto.
- test_zoo.py: Testes unitários para a classe Zoo e a API.
- system_test_zoo.py: Testes de sistema finais para a API do zoológico.

## Como Executar os Testes

1. Certifique-se de ter o Python instalado.
2. No terminal, navegue até o diretório do projeto.
3. Execute python -m unittest para os testes unitários.
4. Execute python -m unittest system_test_zoo.py para os testes de sistema.

## Classes Principais

- Animal: Representa um animal do zoológico com nome, espécie e felicidade.
- Recinto: Representa um local do zoológico para abrigar animais da mesma espécie.
- Zoo: Representa o zoológico e oferece operações como criar animais, recintos, alimentar animais e receber visitantes.

## Testes

O projeto inclui testes unitários para cada classe e testes de sistema finais para validar o comportamento da API como um todo.

