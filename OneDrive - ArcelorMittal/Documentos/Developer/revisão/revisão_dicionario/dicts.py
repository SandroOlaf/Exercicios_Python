
# Nível 1: Básico (Manipulação e Acesso)
# Exercício 1: Criação e Acesso
# Crie um dicionário chamado aluno contendo as seguintes chaves e valores:

# "nome": "João"
# "idade": 22
# "curso": "Engenharia"

# Após criar, escreva o código para imprimir apenas o nome do aluno acessando a chave correspondente.

# aluno = { 
#     "nome": "Sandro",
#     "idade": 26,
#     "faculdade": "Engenharia de Software"
# }

# print(aluno["nome"]) #Pegando o nome do aluno acessando a chave corresponde "nome"

# Exercício 2: Adição e Modificação
# Usando o dicionário criado no Exercício 1:

# Adicione uma nova chave chamada "nota_final" com o valor 8.5.
# Altere o valor da chave "idade" para 23.
# Imprima o dicionário completo para verificar as mudanças.

# aluno["nota_final"] = 8.5
# aluno["idade"] = 23
# aluno["telefone"] = "3312-1231"
# print(aluno)
# Exercício 3: Verificação de Chaves
# Escreva um pequeno código que verifique se a chave "telefone" existe no dicionário aluno. Se existir, imprima o número. Se não existir, imprima "Telefone não cadastrado".

# if "telefone" in aluno:
#     print(f"Número do Aluno: {aluno['nome']} - {aluno['telefone']}")
# else:
#     print(f"Não possui número de telefone do {aluno['nome']}")

# telefone = aluno.get("telefone", "Telefone não cadastrado")
# print(f"Número: {telefone}")


# Nível 2: Intermediário (Iteração e Lógica)
# Exercício 4: Iterando pelo Dicionário
# Crie um dicionário com os preços de 4 produtos no supermercado (ex: {"maçã": 2.50, "banana": 1.80...}). Use um laço for para iterar sobre o dicionário e imprimir na tela a frase:
#  "O produto [nome do produto] custa R$ [preço]".
# supermercado = {
#     "maça": 2.50,
#     "banana": 1.80,
#     "batata": 8.90
# }

# for chave, valor in supermercado.items():
#     print(f"O produto:{chave} custa:R${valor:.2f}")
# Dica: Lembre-se do método .items() para pegar a chave e o valor ao mesmo tempo no for.

# Exercício 5: Frequência de Palavras
# Dada a string abaixo, crie um script que conte quantas vezes cada palavra aparece na frase, armazenando o resultado em um dicionário onde a chave é a palavra e o valor é a contagem.

# frase = "o rato roeu a roupa do rei de roma e o rato fugiu"

# contagem = {}

# for texto in frase.split():
#     contagem[texto] = contagem.get(texto, 0) + 1
    # print(texto)
    # if texto in contagem:
    #     contagem[texto] += 1
    # else: 
    #     contagem[texto] = 1

# print(contagem)

usuario = {
   "login":"sandrodev",
   "senha": 567123    
}

# print(usuario.get("senha_1", "Valor não encontrado" ))

# keys_use = usuario.keys()

# value_use = usuario.values()

# for chave, valor in usuario.items():
#     print(f"{chave}: {valor} está cadastrado!!!")


# print(list(value_use))
# print(list(keys_use))

guarda_volumes = {"porta_01": "mochila azul", "porta_05": "guarda-chuva"}
novas_bagagens = {"porta_02": "casaco", "porta_05": "botas", "porta_10": "vestido" } # porta_05 vai sobrescrever
guarda_volumes.update(novas_bagagens)
guarda_volumes.pop("porta_10")
print(guarda_volumes)
# Saída: {'porta_01': 'mochila azul', 'porta_05': 'botas', 'porta_02': 'casaco'}