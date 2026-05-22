# 🎬 DESAFIO: Bilheteria do Cinema
# O Cenário:
# Você precisa controlar as vendas de ingressos para a sessão de estreia de um filme muito aguardado.
# O sistema deve validar  se o tipo de ingresso existe, se ainda há poltronas daquele tipo e 
# registrar o dinheiro arrecadado.

# Dicionário com os preços de cada tipo de ingresso
tabela_precos = {
    "comum": 30.00,
    "estudante": 15.00,
    "vip": 60.00
}

# Dicionário com a quantidade de poltronas livres para cada tipo
poltronas_livres = {
    "comum": 50,
    "estudante": 20,
    "vip": 2  # A sala VIP é bem exclusiva e só tem 2 lugares!
}

# O valor arrecadado na sessão
faturamento_sessao = 0.00

# 2. Suas Missões (Escreva a lógica para cada evento)
# Evento 1: Promoção Relâmpago!
# O gerente decidiu criar um ingresso especial de última hora.

# Sua lógica deve: Adicionar o item "promocional" à tabela_precos custando 10.00. 
# Em seguida, adicionar o item "promocional" às poltronas_livres com a quantidade 5.

tabela_precos["promocional"] = 10.00
poltronas_livres["promocional"] = 5

# Evento 2: Processando a Fila do Caixa
# Uma fila de clientes se formou e eles pediram os seguintes ingressos em sequência:
fila_clientes = ["comum", "estudante", "vip", "vip", "vip", "camarote"]

# Sua lógica deve: Usar um laço for para passar por cada item da lista fila_clientes.

# Para cada pedido, cheque estas três coisas na ordem:

# Esse tipo de ingresso existe na tabela? (O cliente pediu "camarote", mas não existe esse setor. 
# Imprima: "Erro: Ingresso [camarote] inválido").

# Ainda tem poltrona livre para esse tipo? (Repare que pediram 3 ingressos VIPs, mas o cinema só 
# tem 2 poltronas VIPs. No terceiro pedido, deve imprimir: "Desculpe, o setor [vip] está esgotado!").

# Se o ingresso é válido e tem poltrona livre: Diminua 1 das poltronas_livres daquele tipo, 
# pegue o valor dele na tabela_precos e some na variável faturamento_sessao. 
# Imprima: "✅ Ingresso [tipo] vendido!".

for item in fila_clientes:
    if item in tabela_precos:
        if poltronas_livres[item] > 0:
            poltronas_livres[item] -= 1
            faturamento_sessao += tabela_precos[item]
            print(f"✅ Ingresso {item} vendido!")
        else:
            print(f"Desculpe, o setor {item} está esgotado!")
    else:
        print(f"Erro: Ingresso {item} inválido")

print(faturamento_sessao)
print(poltronas_livres)