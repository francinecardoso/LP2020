#Operadores Relacionais que podemos usar com if 
# a==b  igual
# a!=b  diferente
# a<b   menor             12345 b=6
# a<=b  menor igual       123456  b=6
# a>b   maior 
# a>=b  maior igual 

a=2
b=4
c=1
# if com o uso de um operador relacionais, aninhamento (if dentro de if)
if a<b:
    print("Sim é menor")
    c=a
    print("Valor de c:", c)
    if c==b:
        print("Sim é igual")
    else:
        print("Não é!")
else:
    print("Não é menor")

#if ternário ou operador ternário, se dentro do bloco do if tiver apenas uma linha 
if a<b: print("É menor!")

#if else ternário ou operadores ternários, se dentro do bloco do if e else tiver apenas uma linha
print("b é maior") if a < b else print ("o b não é maior")

#if para fazer mais de uma verificação, com operadores lógicos
if a<b and c!=a:
    print("valor de a: ", a)
    print("valor de b: ", b)
    print("valor de c: ", c)
    print("(and) Isso é verdade!")
elif a<b or c!=a:
    print("(or) Isso é verdade!")

# não podemos criar if, elif ou else vazio, se precisar criar assim, use o pass.
if a<b:
    pass






