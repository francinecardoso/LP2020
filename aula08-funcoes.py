#sintaxe de uma função em python.
def inicio():
    print("Minha primeira função em python!")

inicio()

#Passando parâmetro definido.
def passandoParametro(nome, sobrenome):
    print("Meu nome é", nome)

passandoParametro(True, "Francine")
passandoParametro("Francine", "Cardoso")
passandoParametro(1.50, 1)

#Passando parâmetro indefinido. Geralmente o parâmetro com * se chama *args
#Tupla é sequencial ex: 0,1,2,3,4
def passandoParamentroIndefinido(*nome):
    print("Meu nome é", nome[0], nome[1], nome[2])

passandoParamentroIndefinido("Fracine", "Cardoso", "Nunes")

#Passando parâmetro definido com chave.(Não importa a ordem dos parâmetros e argumentos) kwargs
def passandoParametroChave(idade, nome, cpf):
    print("Meu nome é", nome, idade, cpf )

passandoParametroChave(nome="Francine", idade="26", cpf="00000000000")

#Passando parâmetro indefinido com chave **kwargs
#Dicionário não é sequencial, ele encontra o valor pela chave, não importa a sequência.
def passandoParamentroIndefinidoChave(**dados):
    print("Informações pessoais", dados["idade"], dados["nome"] )

passandoParamentroIndefinidoChave(nome="Francine", idade="26", cpf="00000000000")

#Passagem de parâmetro com valor padrão
def passandoParametroComPadrao(nome= "Sem nome"):
    print("Bem-vindo, ", nome)

passandoParametroComPadrao("Francine")
passandoParametroComPadrao()

#Passando lista por parâmetro
def passandoListaPorParametro(lista):
    for i in lista:
        print(i)
    
minhaLista = ['Francine', 'Cardoso']

passandoListaPorParametro(minhaLista)

#Se criar uma função vazia
def funcaoVazia():
    pass

#função com retorno
def retornaValor(nome):
    if nome =="Francine":
        return True
    return False

#chamada da função com retorno direto no if
if retornaValor("Francine") == True:
    print("Correto")
else:
    print("Incorreto")

#Recursividade: é recurso onde podemos chamar a função dentro dela mesma.
def funcaoRecursiva(numero):
    if numero > 0:
        resultado = numero + funcaoRecursiva(numero - 1)
    else:
        resultado = 0
    return resultado

funcaoRecursiva(5)
    
    




