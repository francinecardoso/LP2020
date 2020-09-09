#Sintaxe do dicionário
# Chave: Valor 
meuDicionario = {
    "nome": "francine",
    "idade": 26
}
print("Mostrando o dicionário: ", meuDicionario)

#Acessando valor pela chave 
print("Mostrando valor pela chave: ", meuDicionario['nome'])

#Acessando valor pelo método get()
print("Mostrando valor pela chave usando get(): ", meuDicionario.get('idade'))

#Alterando valor de um item específico
meuDicionario['nome'] = 'Fran'
print("Novo valor da chave nome: ", meuDicionario['nome'])

#Percorrendo um dicionário para retornar as chaves
for x in meuDicionario:
    print("Percorrendo o dicionário para retornar chaves: ", x)

#Percorrendo um dicionário para retornar os valores
for x in meuDicionario:
    print("Percorrendo o dicionário para retornar o valor: ", meuDicionario[x])

#Percorrendo um dicionário para retornar o valor com values()
for x in meuDicionario.values():
    print("Percorrendo o dicionário para retornar o valor com values(): ", x)

#Percorrendo dicionário, mostrando chave e valor.
for x in meuDicionario:
    print(x, meuDicionario[x])

#Verificar se existe a chave no dicionário
if 'idade' in meuDicionario:
    print("Sim tem a chave idade no dicionário") 

print("tamanho do dicionário: ",len(meuDicionario))

#Adicionando novo item no dicionário
meuDicionario['cpf'] = '22222222222'
print("Adicionando novo item: (chave e valor) ", meuDicionario)

#Removendo item com a função pop()
meuDicionario.pop('cpf')
print("Removendo item com função pop(): ", meuDicionario)

#Deletando item com a função pop()
del meuDicionario['idade']
print("Deletando item pela chave usando del: ", meuDicionario)
