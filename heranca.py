#Administrador e o funcionário, o administrador vai poder fazer tudo o que o funcionário faz e mais um pouco, ele terá mais funcionalidades.

#self -> a instância, objeto
class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salário': self.salario}

fabio = Funcionario('Fábio', 7000)
print(fabio.dados())

#Classe Admin é do tipo Funcionario, ou seja, ela herda todas as funcionalidades que um funcionário tem.
class Admin(Funcionario):
    def __init__(self, nome, salario):
        #Referenciar a classe funcionário através da palavra super.
        super().__init__(nome, salario)

    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados()
        
fernando = Admin('Fernando', 14000)
print(fernando.dados())

fernando.atualizar_dados('Fernandinho')
print(fernando.dados())