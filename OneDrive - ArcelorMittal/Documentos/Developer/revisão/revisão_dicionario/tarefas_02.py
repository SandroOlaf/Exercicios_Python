# Combinado! Vamos dar um passo atrás e focar no **básico bem feito**. Nada de dicionários dentro de dicionários ou lógicas 
# complexas de jogos.

# Aqui está um mini projeto de **Nível Básico**, focado apenas nas operações fundamentais: criar, ler, atualizar, deletar e iterar.

# ---

# ## 📒 MINI PROJETO: Agenda de Contatos

# **O Cenário:**
# Você está criando a lógica de um aplicativo de agenda telefônica simples. Cada contato tem apenas um nome (a chave) e
#  um número de telefone (o valor).

# **O Ponto de Partida:**
# Inicie seu código com este dicionário:

# ```python
agenda = {
    "Ana": "9999-1111",
    "João": "8888-2222"
}

# ```

# ### 🎯 Suas Tarefas (Escreva o código em sequência):

# **Tarefa 1: Novo Contato**
# Adicione um novo contato chamado `"Carlos"` com o número `"7777-3333"` na agenda.
agenda["Carlos"] = "7777-3333"
# **Tarefa 2: Atualização**
# A Ana mudou de número. Atualize o valor da chave `"Ana"` para `"9999-0000"`.
agenda["Ana"] = "9999-0000"
# **Tarefa 3: Busca Segura**
# Escreva uma lógica que tente buscar o número da `"Maria"`. Se ela existir na agenda, imprima o número. Se não existir,
#  imprima a mensagem: *"Contato não encontrado"*. (Lembre-se do melhor método para evitar erros de chave que não existe!).
busca = agenda.get("Maria", "Contato não encontrado!")
print(busca)
# **Tarefa 4: Exclusão**
# O João perdeu o celular e você precisa apagar o contato dele. Remova a chave `"João"` da agenda.
agenda.pop("João")
# **Tarefa 5: Listagem Final**
# Crie um laço `for` que passe por todos os contatos que restaram na sua agenda e imprima cada um neste exato formato:
# *"Nome: [NOME] | Telefone: [NUMERO]"*
for chave, valor in agenda.items():
    print(f"Nome: {chave} | Telefone: {valor}")
# ---

# Pode ir escrevendo e testando. Quando terminar, cole seu código aqui!