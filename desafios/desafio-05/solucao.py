# Desafio 05 — Gerenciador de Compras
# Aluno: (Davi Almeida de Oliveira)
# Data:  (25/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
produtos = []
continuar  = True
while continuar==True:
    
    add_item  = str(input('Escreva o nome do produto que quer adicionar no carrinho:'))
    add_item.strip();
    if add_item.upper() == 'FIM' :
        continuar = False
    
    else:

        produtos.append(add_item)
        print(f"{add_item} adicionado ao carrinho")
        print(f"CARRINHO ATÉ AGORA\n{produtos} ")
if produtos == []:
    print(f'Carrinho fechado com nenhum produto!')
else : 
    print(f'Então carrinho fechado em:\n{produtos}')