# Explicação — Desafio 01

**Aluno:** _(Davi Almeida de Oliveira)_  
**Data:** _(19/05/2026)_

---

## O que meu programa faz

_(O código escrito primeiramente, por meio de input pede para o usuário inserir o seu nome e guarda na variável 'nome' que foi justamente criada para receber string, mas que ainda não tem tratamento para caso receba outro tipo não definido. Em seguida ocorre o mesmo processo com a variável 'sobrenome' o usuário digita o sobrenome e ele fica guardado na variável de mesmo nome.Depois de inserir nome e sobrenome ao usuário vai ser solicitado inserir o seu ano de nascimento, por meio de input. Obrserve que é especificado o tipo a ser recebido, nesse caso interiro, se não for inteiro o programa quebra e não prossegue. É difinida uma variável denominada 'anoAtual' e essa recebe um inteiro que o usuário nãoa vai ter contato, pois ela vai ser apenas para fazer a subtração e encontrar a idade do usuário. Após toda essa inserção de dados, utilizando o método fString e por meio de print escreveremos o nome e sobrenome concatenado do usuário e afirmamos o ano de nascimento e logo em seguida quantos anos ele tem.)_

---

## Resposta à Pergunta Obrigatória

> Por que é necessário converter o resultado do `input()` antes de calcular a idade?

 O que acontece se não converter?

_(Sua resposta aqui — use suas próprias palavras. Pode incluir exemplos de código se ajudar a explicar.)_

R = É necessário para um tratamento de erro futuro, como os sistemas não são feitos para o desenvolvedor, é necessário sempre pensar no pior caso. O que pode acontecer se não for feito a conversão é o usuário digitar caracteres alfanuméricos ao invés de apenas numéricos.

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
