# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: (Davi Almeida)
# Data:  (25/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?


# ── Sua solução abaixo ─────────────────────────────────────────────────────
 
nome = input('Digite o seu nome: ')
cpf = input('Digite o seu CPF: ')

try : 
    nascimento = int(input('Digite o ano em que você nasceu:\n'))
    altura = float(input('Digite a sua altura. Exemplo: 1.80\n'))
except ValueError: 
    print('Digite no formato correto!\nAno:(2000)\n' \
    'Altura:(1.75) ')
idade = 2026  - nascimento;

print(f'Olá {nome}\nSeu CPF é: {cpf} - idade: {idade} anos - Altura: {altura} metros')


"""
Float serve para altura porque a altura na maioria das vezes é um número com casas decimais
e em sua maioria não é algo a ser truncado, mas sim demonstrado com duas casas.
"""