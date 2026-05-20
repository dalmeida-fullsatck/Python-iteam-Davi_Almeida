# Explicação — Desafio 02 — Calculadora de IMC

**Aluno:** _(Davi Almeida de Oliveria)_
**Data:** _(20/05/2026)_

---

## O que meu programa faz

_O programa recebe nome, peso e altura por meio de inputs. Atenção aos iputs de peso e altura que estão definidos como floats para futuros tratamentos de erros. Após serem inseridos, os dados altura e peso são copiados para uma variável chamada 'imc' e lá é que a mágica acontece: é feita a conta de peso dividido por altura que está elevada ao quadrado. No código em questão foi utilizado uma função nativa de python chamada 'pow' que tem a sintaxe bem comum entre outras linguagens seria 'pow(base,expoente)'. Mesmo utilizando essa facilidade, o exercicio poderia ser facilmente resolvido também apenas multiplicando altura por altura, ou seja, peso / (altura*altura). Após o calculo tudo isso foi redirecionado em um print('') que concatena o texto a ser imprimido utilizando fString  print(f'texto') e adicionando o nome das variáveis entre chaves. Ponto importante, na variável 'imc' tem mais caracteres além do nome da variável em si. Isso está acontecendo para limitar ela em dois caracteres após virgula, uma vez que ela é uma  variável do float por processar dados float. Dessa forma um número não fica tão grande_

---

## Resposta à Pergunta Obrigatória

> Por que é necessário usar `float()` ao capturar peso e altura com `input()`? O que aconteceria se usássemos `int()` para a altura `1.75`?

_(Sua resposta aqui — use suas próprias palavras.)_
Se não fosse utilizado floats não teria como ser inseridos dados que geralmentes são quebrados e não inteiros como altura que utiliza (1.algo) e não (1 metro). geralmente alguém tem um metro virgula alguma coisa e não apenas 1 metro. Dessa forma o float vem para conseguirmos inserir dados numéricos que não são inteiros.
---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
