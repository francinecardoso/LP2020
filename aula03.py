# Como mostrar algo na tela para o usuário
print("hello")
print('hello')
# Declaração de variáveis e tipo de dados
numeroInteiro = 2
numeroDecimal = 2.1236
nome = "Francine"
sobrenome = 'Cardoso'
verdadeiroFalso = True
#Mostrando na tela os valores armazenados nas variáveis.
print(numeroInteiro)
print(numeroDecimal)
print(nome)
print(sobrenome)
print(verdadeiroFalso)
#Mostrando na tela o tipo de dado que a variável armazena
print(type(numeroInteiro))
print(type(numeroDecimal))
print(type(nome))
print(type(sobrenome))
print(type(verdadeiroFalso))
#Recursos para usar com dados do tipo String
#Função len = contar a quantidade de caractere de uma variável do tipo String
print(len(nome))
#Repetir valor da variável, usar * e colocar a quantide de vezes que gostaria de repetir
#devendo como dar espaço entre os itens
print((nome + ' ' ) * 3)
#Concatenando strings 
print(nome + '', sobrenome)
print(nome + ' Cardoso')
#Recursos para usar com dados do tipo float
print(numeroDecimal)
#A função round serve para arredondar e definir a quantidade de casas depois da vírgula(ponto)
print(round(numeroDecimal,3))
#Outra forma de arredondamento e definir a quantidade de casas depois da vírgula(pontos)
print('%.3f' % numeroDecimal)

