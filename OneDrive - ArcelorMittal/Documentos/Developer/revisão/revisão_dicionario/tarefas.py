# Exercício 1: O Objeto
# Crie um dicionário vazio chamado livro. Em seguida, em linhas separadas (sem recriar o dicionário), 
# adicione as chaves "titulo", "autor" e "paginas", atribuindo valores de sua escolha.

livro = {}

livro["titulo"] = "O vinho novo é melhor"
livro["autor"] = "Thommas"
livro["paginas"] = 200

print(livro)

# Exercício 2: O Cirurgião
# Dado o dicionário 
perfil = {"username": "admin", "email": "admin@site.com", "ativo": False, "tentativas": 3}
atualizar_perfil = {"ativo": True, "tentativas": 0, "ultimo_login": "hoje"}
perfil.update(atualizar_perfil)

del perfil["email"]
# Imprima o dicionário final.
print(perfil)

# 🟡 Nível 2: Domínio dos Métodos
# Exercício 3: Explique e Prove
servidor = {"ip": "192.168.1.1", "porta": 8080}
# Abaixo dele, escreva comentários no seu código explicando com as suas palavras o que os métodos .get(), .update() e .pop() fazem.
# Em seguida, escreva uma linha de código real para cada método aplicando-os 
# no dicionário servidor para provar que sua explicação está certa.

#Método:
# .get() é um metodo que retorna uma chave especifica ou um valor padrão informado
print(servidor.get("ip", "IP não encontrado"))
#.update() é um método que nos utilizamos para atualizar um dicionario com novos intens, ou atualizamos os itens que estão contidos dentro de um dicionario
servido_atualizado = {"ip": "192.168.1.2", "ip_2": "192.168.1.3", "porta_2":8081 }
servidor.update(servido_atualizado)
#.pop() remove uma determinada chave dentro do dicionario e logo após retorna qual valor foi removido.
remover = servidor.pop("porta")
print(f"REMOVIDO: {remover}")
print(servidor)
