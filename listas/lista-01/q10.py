# Lista 01 — Questão 10: Análise Crítica de Código
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q10.py: reescreva a função corrigindo os 3 problemas encontrados.
# 
#   def processar_alunos(alunos=[]):
#       aprovados = []
#       for i in range(len(alunos)):
#           if alunos[i]['nota'] >= 7.0:
#               aprovados = aprovados + [alunos[i]['nome']]
#       print(aprovados)
# 
# Em q10_resposta.txt: identifique cada problema e explique por que é um problema.
# Dica: há um problema em: (1) definição da função, (2) como o loop é escrito, (3) como a lista é construída.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
def processar_alunos(alunos={}):
    aprovados = {}
    for nome, nota in alunos.items():
        try:   
            if nota<0.0 or nota>10.0:
                raise ValueError(f'Nota: {nota} Incorreta! Valores menores que 0 e maiores que 10 serão desconsiderados.') 
            if nota >=7:   
                aprovados[nome] = nota
        except ValueError as erro:
            print(f'AVISO: não foi possivel processar {nome}. Motivo: {erro}')
    return aprovados
    

turma = {
     'José': -2,
     'João' : 9.3,
     'Jr': 10.11,
     'Nayara': 10000
}


print(processar_alunos(turma))
