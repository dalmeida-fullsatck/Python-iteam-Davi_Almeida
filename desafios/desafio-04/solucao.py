# Desafio 04 — Tabuada Personalizada
# Aluno: (Davi Almeida de Oliveira)
# Data:  (21/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
ind = 1
while ind==1 :
    num = int (input('Digite um número que você quer ver a tabuada\n'))

    for i in range(1, 11, 1):

        mult = num*i
        print(f'{num} X {i} = {mult}\n----------------')
        
    dig = (int(input('Se você quiser parar digite (0)\n Se não digite (1)')))
    if dig != 1:
        break
