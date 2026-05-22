# ☕ DESAFIO: Sistema de Cafeteria (Caixa Rápido)
# O Cenário:
# Você é o programador responsável pelo sistema do caixa de uma cafeteria. 
# Você precisa controlar os preços dos produtos (cardápio), a quantidade de itens na vitrine (estoque) e 
# processar o pedido de um cliente.

# Dicionário com os preços dos produtos
cardapio = {
    "cafe": 5.00,
    "pao_de_queijo": 4.50,
    "bolo": 7.00
}

# Dicionário com a quantidade disponível na vitrine
estoque = {
    "cafe": 10,
    "pao_de_queijo": 5,
    "bolo": 2
}

# O valor que o caixa começa no dia
caixa_total = 0.00

cardapio["suco"] = 6.00
estoque["suco"] = 8

pedido_cliente = ["cafe", "bolo", "bolo", "bolo", "coxinha"]

for pedido in pedido_cliente:
    if pedido in cardapio:
        if estoque[pedido] > 0: 
                estoque[pedido] -= 1
                caixa_total += cardapio[pedido]
                print(f"Vendido: {pedido}")
        else:
             print(f"⚠️ Desculpe, o item '{pedido}' acabou!")
    else:
            # Cai aqui se o item nem sequer existir no dicionário cardapio
            print(f"❌ Erro: O item '{pedido}' não existe no cardápio.")

# --- EVENTO 3: O FECHAMENTO ---
print("\n--- RELATÓRIO DE FECHAMENTO ---")
# Usamos :.2f para formatar o número com duas casas decimais (ex: 19.00)
print(f"💰 Valor total no caixa: R$ {caixa_total:.2f}")
print(f"📦 Estoque final: {estoque}")