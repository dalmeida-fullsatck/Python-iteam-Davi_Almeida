# Lista 01 — Questão 07: Progressão e Análise
# Aluno: (Davi Almeida de Oliveira)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

notas = []

for i in range(0,11):



    while True: 
        try:
            nota = float(input(f'Digite a nota {i}: ')) 
            if nota < 0.0 or nota > 10.0:
                raise ValueError('Valor deve ser positivo e menor do que 10.0 ') 
            notas.append(nota)
            break
        except ValueError as e: 
            print(f'Entrada Inválida! {e}');

maiorNota = max(notas)
menorNota = min(notas)
media = sum(notas)/ len(notas)

aprovado =0
recuperacao = 0
reprovado = 0

acima_media=0
for nota in notas:
    if nota > media:
        acima_media+=1

for nota in range(0,10):
    if nota >= 7:
       aprovado+=1
    elif nota >=5.0:
        recuperacao+=1
    else:
        reprovado+=1
print("RELAÇÃO APROVADOS, REPROVADOS E MAIOR E MENOR NOTA\n_____________________________________")
print(f"Maior nota: {maiorNota:.1f}")
print(f"Menor nota: {menorNota:.1f}")
print(f"Média da turma: {media:.1f}")
print(f"Quantidade acima da média: {acima_media}")
print(f"Quantidades de aprovados: {aprovado}")
print(f"Quantidades de reprovados: {reprovado}")
print(f"Quantidades de recuperação: {recuperacao}")
