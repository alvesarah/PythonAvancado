[x for x in range(5)]

#Com o "x" na frente seria o mesmo que pegar o loop a baixo e faze-lo da seguinte forma:

#Forma estendida
numeros_pares = list(range(0, 11, 2))
for numero in numeros_pares:
    print(numero ** 3)

#Forma em uma linha só
[n ** 3 for n in range(0, 11, 2)]

#Pegando números pares
print([n for n in range(11) if n % 2 == 0])

#Pegando números ímpares
print([n for n in range(11) if n % 2 == 1])

#Escrever nomes da mesma forma
pessoas = [" Ana ", "manuela", "FELIPe", "PedrO "]

ana = " Ana "
ana.strip() #Retira os espaços
ana.lower() #Deixa em minúsculo
ana.upper() #maiúsculo
ana.capitalize() #fica maiúsculo

pessoas_normalizadas = [pessoa.strip().capitalize() for pessoa in pessoas] # R: ['Ana', 'Manuela', 'Felipe', 'Pedro']