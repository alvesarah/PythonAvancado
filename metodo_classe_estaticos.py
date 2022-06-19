class Funcionario():
    aumento = 1.04
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salário': self.salario}

    def aplicar_aumento(self):
        self.salario *= self.aumento

    #método de classe -> Função da classe, que a afeta como um todo
    @classmethod #Diferente dos que recebem self, ele recebe 'cls'
    def definir_novo_aumento(cls, novo_aumento):
        cls.aumento = novo_aumento #Pegando a classe toda para determinar a mudança em todos os objetos que foram criados a partir de então.

    #Método Estático -> Tem relação com o funcionário, mas não existe nenhum argumento da função funcionário (sem self, não precisa de nada de um funcionário).
    @staticmethod
    def dia_util(dia):
        #segunda-feira = 0
        #domingo = 6
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True

fabio = Funcionario('Fábio', 7000)
fabio.aplicar_aumento() # R:7280.0

#Para apicar o aumento na classe, no modelo e não em um objeto específico, é chamada a classe.
Funcionario.definir_novo_aumento(1.05)
fabio.aplicar_aumento() # R:7.644.0

import datetime
minha_data = datetime.date(2022, 6, 19) #domingo

Funcionario.dia_util(minha_data) # R:False