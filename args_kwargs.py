#args => abreviação de argumentos
#kwargs => keyword arguments (argumentos de palavras-chave)

def soma(arg1, arg2):
    return arg1 + arg2

soma(5, 6)

def soma_varios(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5

soma_varios(1, 2, 3, 4, 5)

def lista_somada(lista):
    return sum(lista)

lista_somada([1, 2, 3, 4, 5])

#ARGS
#Não sabe quantos elementos vai receber mas é essencialmente uma lista, só que sem o formato de lista [].
def soma_simplificada(*args):
    return sum(args)

soma_simplificada(1, 2, 3, 4, 5) # R: 15

#KWARGS
#Geralmente os métodos genéricos possuem args e kwargs
def metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

metodo_kwargs(3, 'saaa', 4, 'qualquer', nome='Ana', idade=25)

# R: (3, 'saaa', 4, 'qualquer')
#    {'nome': 'Ana', 'idade': 25}
#Recebe os args em uma tupla e os kwargs em um dicionário
#Sempre colocar os args antes dos kwargs