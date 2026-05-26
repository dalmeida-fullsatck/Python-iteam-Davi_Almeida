# Desafio 03 — Sistema de Multas
# Aluno: (Davi Almeida de Oliveira)
# Data:  (20/05/2026)

#── Escreva sua solução abaixo ──────────────────────────────────────────────#

velocidade = int (input ('Qual a velocidade do seu carro?\n(em km/h)'))
permitido = 80;
if velocidade > permitido and velocidade < 241:
    acima = velocidade - permitido; 
    multa = acima*7;
    print(f'Você excedeu em {acima}km/h da velocidadde permitida que é {permitido}km/h\nSua multa será de R${multa},00 ')
elif velocidade < 5  :
    print(f'Você está muito a baixo de {permitido}km/h, também está errado!');
elif velocidade > 240   :
    print('Velocidade inválida!');
else : 
    print(f'Você está dentro da legalidade que é {permitido}km/h, tá correto!');