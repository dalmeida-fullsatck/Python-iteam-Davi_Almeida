# Explicação — Desafio 03 — Sistema de Multas

**Aluno:** _Davi ALmeida de Oliveira_
**Data:** _20/05/2026_

---

## O que meu programa faz

_Recebe velocidade do carro por meio de input. Atenção: limitando-se a "int" para futuros tratamentos de erro. É criado uma variável chamada 'permitido' que tem o valor inteiro de (80) que se refere a velocidade permitida, ou seja, se passar daquilo terá consequências. Inicia a primeira condicional que diz lê-se da seguinte forma: SE 'velocidade'(inserida pelo usuário) for maior do que permitido(80) e com ele ainda possui um CONECTIVO LÓGICO que é o 'and' que significa 'e', ou seja, se o carro estiver em uma velocidade maior que o permitido(80) E estiver menor do que 240km/h o programa entra nessa condição. Estando dentro desa condição têm-se: a variável local dentro do escopo do primeiro if que é a variável 'acima', ela é a diferença da velocidade do carro pela velocidade permitida. E ela vai ser utilizada para gerar os valores das multas. A variável 'multa' é a variável acima multiplicado por 7. Isso porque 'acima' é a diferença da velocidade do carro pela velocidade permitida, ou seja, 'multa' é o limite excedido multiplicado por 7. Ainda foi adicionado alguns elif's, um para velocidade muito abaixo, foi fixado em 5km/h e outro para se passar de uma velocidade real, no caso, foi fixado em 240km/h e se você tiver em uma velocidade regular então o 'else' agirá trazendo uma mensagem de que você está dentro da legalidade._

---

## Resposta à Pergunta Obrigatória

> Por que usamos `elif` e não múltiplos `if` separados? Dê um exemplo concreto onde a diferença causaria um resultado errado.

_(Se fosse um amontoado de if's, se uma uma condição for true, mas tiver ainda condições true abaixo também será realizado os outros if's e não apenas só o primeiro. Exemplo:

if numero < 10:
    print('Menor do que 10')
if numero<5;  
    print('Menor do que 5')
if numero < 3;  
    print('Menor do que 3')
else:
    print('Não é maior do que 10');
    
Nesse exemplo fica claro, porque se você colocar o numero 9 por exemplo, ele vai executar tudo, menos o else.    
    )_

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
