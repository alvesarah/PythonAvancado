#Decoradores => classmethod e staticmethod, eles utilizam a biblioteca chamada functools. Ele tem o poder de transformar uma função e entregar diferente. Exemplos da onde são usadas: autenticação de usuário, a questão de método de clase e estático.

import functools

def meu_decorador(funcao):
    @functools.wraps(funcao) #embrulhe minha função.
    def func_que_roda_funcao():
        print("********Embrulhando função no decorador!********")
        funcao()
        print("**********Fechando embrulho!************")
    return func_que_roda_funcao

@meu_decorador
def  minha_funcao():
    print("Eu sou uma função")

minha_funcao()

# R:********Embrulhando fun��o no decorador!********
#           Eu sou uma fun��o
#   ********Fechando embrulho!************
