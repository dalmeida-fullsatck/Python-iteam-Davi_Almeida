# Lista 01 — Questão 06: Validador de Senha
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Escreva um programa que solicite uma senha em loop até que atenda TODOS:
#   1. Mínimo 8 caracteres.
#   2. Pelo menos um dígito (use .isdigit() em cada caractere).
#   3. Pelo menos uma letra maiúscula.
# Para cada tentativa inválida, informe qual critério não foi atendido.
# Ao aceitar: 'Senha válida após X tentativa(s).'

# ── Sua solução abaixo ──────────────────────────────────────────────────────

tentativas = 0
while True:
      senha = input('\nDigite uma senha, mas tem alguns detalhes\n'
           '1. Mínimo 8 caracteres.\n'\
            '2. Pelo menos um dígito \n'\
            '3. Pelo menos uma letra maiúscula.\n')

      
      tamanho = len(senha) >= 8 
            
      digito = any(caracteres.isdigit() for caracteres in senha)

      maiuscula = any(caracteres.isupper() for caracteres in senha)

      if tamanho and digito and maiuscula: 
            print(f'\nSenha válida após {tentativas} tentativas!')
            break
      if not tamanho: 
            print('\n- Tente digitar no mínimo 8 caracteres!')
      if not digito: 
            print('\n- Tente colocar pelo menos um digito numérico!')
      if not maiuscula: 
            print('\n- Tente colocar no mínimo uma letra MAIUSCULA!')

      if not maiuscula or tamanho or digito:
            tentativas+=1
      