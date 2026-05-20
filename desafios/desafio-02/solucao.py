# Desafio 02 — Calculadora de IMC
# Aluno: (Davi Almeida de Oliveira)
# Data:  (20/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
nome = input('Digite o seu nome: ')
peso = float(input('Digite o seu peso\n(exemplo: 74)\n'))
altura = float(input('Digite o a sua altura\n(exemplo: 1.60)\n'))

imc=peso/pow(altura,2)


print (f"Olá {nome}, seu IMC é {imc:.2f}")