#Desordenado e sem consulta pelo index
meu_set = {4, "valor", 3, "qualquer"}

#Assim podemos buscar informações que estão no set
meu_dicionario = {"nome": "Ana", "idade": 80}
meu_dicionario['nome'] # R: 'Ana'

meu_dicionario_list = [
    {"nome": "Ana", "idade": 80}, 
    {"nome": "Maria", "idade": 30}, 
    {"nome": "Lucas", "idade": 22}, 
    {"nome": "João", "idade": 45}
]

# Para buscar a Maria
print(meu_dicionario_list[1])

# Para buscar nome da Maria
print(meu_dicionario_list[1]['nome'])

loteria = {"nome": "Fulano", "numeros": (13, 4, 53, 67, 82)} #Os números foram colocados em tuplas pois são imutáveis

sum(loteria['numeros'])
loteria['nome'] = 'Ana'
print(loteria)

universidades = [
    {
        "nome": "Universidade Federal do Rio de Janeiro",
        "sigla": "UFRJ"
    },
    {
        "nome": "Universidade de São Paulo",
        "sigla": "USP"
    }
]

print(universidades)