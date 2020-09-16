#for é um laço ou estrutura de iteração

#Percorrer uma lista
minhaLista = ['Java', 'JS', 'Dart', 'Ruby', 'Python']
for x in minhaLista:
    print("Minha Linguagem: ", x)

#Percorrer uma palavra
for x in 'Python':
    print("Letras da palavra: ", x)
 
#Parar de percorrer a lista(sair do loop) quando encontrar a palavra Dart.
for x in minhaLista:
    print("Minhas linguagens: ", x)
    if x=='Dart':
        break

#Usando função range para percorrer o for
for x in range(5):
    print("Usando função range(): ",x)
else:
    print("Acabou a execução do loop for! :) ")

#Usando função range definindo intervalo
for x in range(2,6):
    print("Usando função range() definindo início e fim: ",x)

#Usando função range com incremento personalizado
for x in range(5,50,10):
    print("Usando função range() definindo início, fim e incremento personalizado: ",x)

#Se criar for sem bloco de código, tem que usar o pass, se não vai dar erro de sintaxe.
for x in minhaLista:
    pass