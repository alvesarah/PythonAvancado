#Classes (Modelo ou representação de um objeto)

#Método init(padrão) serve para instanciar um objeto
#Self -> Ele mesmo
class JogadorLoteria:
    def __init__(self, nome):
        self.nome = nome
        self.numeros = (13, 4, 52, 23, 67, 82)

    def total(self):
        return sum(self.numeros)

#Objetos (São uma instância de uma classe)

#Objeto 1
jogador_1 = JogadorLoteria('Ana')
#Acessar o nome
print(jogador_1.nome)
#Acessar função
print(jogador_1.total())

#Objeto 2
jogador_2 = JogadorLoteria('Felipe')

jogador_1 == jogador_2 # R: False

#{
#Não é um objeto, é um dicionário, se fosse um objeto, a comparação entre os dois, por mais que fossem iguais, daria false. Cada um é individual, e os objetos tem potencial muito maior, podem ter funções, executar ações...

jogador_loteria_1 = {
    'nome': 'Pedro',
    'numeros': (13, 4, 52, 23, 67, 82)
}

jogador_loteria_2 = {
    'nome': 'Pedro',
    'numeros': (13, 4, 52, 23, 67, 82)
}

jogador_loteria_1 == jogador_loteria_2 # R: True
#}