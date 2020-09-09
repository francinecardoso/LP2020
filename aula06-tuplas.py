#sintaxe de criação da tupla
minhaTupla = ("Açai","Leite Ninho","Nutella", "tupla" )
print("Mostrar a tupla: ", minhaTupla)
print("Mostrar um item em posição específica: ", minhaTupla[2])
print("Mostrar o último item da tupla (indexação negativa): ", minhaTupla[-1])
print("Mostrar um intervalo de itens: ", minhaTupla[1:2])

#tentando alterar item da tupla
#minhaTupla[1]= "Leite em Pó"
#print(minhaTupla)

#Burlando alteração de dados na tupla 
listaClandestina = list(minhaTupla)
print("Lista Clandestina: ", listaClandestina)
listaClandestina[2] = "Leite Condensado"
print("Lista Clandestina com dado alterado: ", listaClandestina)
minhaTupla = tuple(listaClandestina)
print("Minha tupla clandestina: ", minhaTupla)

#Criar a tupla com apenas um item (TEM QUE TER A VÍRGULA)
minhaTuplaDois = ('tupla',)
print("Verificando o tipo de dado:  ", type(minhaTuplaDois))
print("Acessando pela posição ordenada: ", minhaTuplaDois[0])
print("Acessando indexação negativa: ", minhaTuplaDois[-1])

#Excluir a tupla completamente
#del minhaTuplaDois
#print("tentando", minhaTuplaDois)

#Juntando tuplas
minhaTuplaTres = minhaTupla + minhaTuplaDois
print("Juntando tuplas: ", minhaTuplaTres)

#Função count() serve para contar a quantidade de vezes que se repete o item
quantidadeQueRepete =  minhaTuplaTres.count('tupla')
print("Usando função count: ", quantidadeQueRepete)

#Função index() serve para retornar primeira ocorrência do item
posicaoDoItem = minhaTuplaTres.index('tupla')
print("Usando função index (Retorna primeira posição): ", posicaoDoItem)