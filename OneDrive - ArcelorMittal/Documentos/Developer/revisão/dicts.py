
# Nível 1: Básico (Manipulação e Acesso)
# Exercício 1: Criação e Acesso
# Crie um dicionário chamado aluno contendo as seguintes chaves e valores:

# "nome": "João"
# "idade": 22
# "curso": "Engenharia"

# Após criar, escreva o código para imprimir apenas o nome do aluno acessando a chave correspondente.

aluno = { 
    "nome": "Sandro",
    "idade": 26,
    "faculdade": "Engenharia de Software"
}

# print(aluno["nome"]) #Pegando o nome do aluno acessando a chave corresponde "nome"

# Exercício 2: Adição e Modificação
# Usando o dicionário criado no Exercício 1:

# Adicione uma nova chave chamada "nota_final" com o valor 8.5.
# Altere o valor da chave "idade" para 23.
# Imprima o dicionário completo para verificar as mudanças.

aluno["nota_final"] = 8.5
aluno["idade"] = 23
aluno["telefone"] = "3312-1231"
# print(aluno)
# Exercício 3: Verificação de Chaves
# Escreva um pequeno código que verifique se a chave "telefone" existe no dicionário aluno. Se existir, imprima o número. Se não existir, imprima "Telefone não cadastrado".

# if "telefone" in aluno:
#     print(f"Número do Aluno: {aluno['nome']} - {aluno['telefone']}")
# else:
#     print(f"Não possui número de telefone do {aluno['nome']}")

telefone = aluno.get("telefone", "Telefone não cadastrado")
print(f"Número: {telefone}")