#Sintaxe de uma lista(array) em python 
minhaLista = ["Eduardo", "Julia", "Ana", 10]
print(minhaLista)

#Acesso ao item por posição
print("Acesso por posição: ",minhaLista[0])

#Acesso indexado negativo por posição, -1 é a ultima posição da lista
print("Acesso indexado negativo: ", minhaLista[-1])

#Intervalo de itens
print("Intervalo de itens: ",minhaLista[1:3])
print("Intervalo de itens sem o item de início: ",minhaLista[:2])
print("Intervalo de itens sem o item de final: ",minhaLista[1:])

#Intervalo de itens indexação negativo 
print("Intervalo de itens: ",minhaLista[-3:-1])

#Alterando valor do item
minhaLista[3] = "Francine"
print("Lista com valor do item alterado: ",minhaLista)

#Percorrer lista
for i in minhaLista:
    print("Item da lista: ",i)

#Verificar se o item está na lista
if "Julia" in minhaLista:
    print("Sim, está na lista!")
else:
    print("Não está na lista")

#Retorna quantidade de itens na lista 
print("Quantidade de itens na lista: ", len(minhaLista))

#Adiciona item ao final da lista
minhaLista.append("Henrique")
print("minha lista com novo item no final: ", minhaLista)

#Adiciona item na posição escolhida
minhaLista.insert(2, "Madu")
print("minha lista com item em posição específica: ", minhaLista)

#Remover item específico
minhaLista.remove("Francine")
print("minha lista com item removido: ", minhaLista)

#Remove o índice especificado
minhaLista.pop(4)
print("minha lista com índice removido: ", minhaLista)

#Se usar o pop sem passar o parâmetro, vai remover o último da lixta
minhaLista.pop()
print("minha lista com índice removido: ", minhaLista)

#Deleta item na posição específica
del minhaLista[1]
print("minha lista com item removido com o del ", minhaLista)

#deleta a lista toda APAGA TUDO.
#del minhaLista

#Limpa a lista mas não deleta ela.
minhaLista.clear()
print("minha lista vazia com o método clear ", minhaLista)

#Inserindo valores novamente
minhaLista.insert(0, "hello")
minhaLista.insert(1, "opa")
print("Minha lista com novos itens ", minhaLista)

#Copia dados de uma lista para outra lista
minhaSegundaLista = minhaLista.copy()
print("Lista que copiou a outra: ", minhaSegundaLista)

#Copia dados de uma lista para outra lista
minhaTerceiraLista = list(minhaSegundaLista)
print("Lista que copiou a outra: ", minhaTerceiraLista)

#Adicionando novos valores nas listas a seguir: 
minhaSegundaLista.append("eae")
minhaTerceiraLista.insert(0, "hello")
print("Adicionando novos amiguinhos na segunda lista: ", minhaSegundaLista)
print("Adicionando novos amiguinhos na terceira lista: ", minhaTerceiraLista)

#função count serve para contar a quantidade de vezes que o item se repete na lista
print("quantidade de vezes que repete hello: ", minhaTerceiraLista.count("hello"))

#Juntando listas
minhaQuartaLista = minhaSegundaLista + minhaTerceiraLista
print("Juntando listas: ", minhaQuartaLista)

#Encontrando a posição de um item na lista
print("Encontrando a posição de um item na lista: ", minhaQuartaLista.index("hello"))
