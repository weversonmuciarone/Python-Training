from sys import getsizeof
# List comprehension
#     Mais simples de se escrever
#     Utilizado quando voce precisa criar nova lista a partir de uma existente

'''
frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = []

# for item in frutas1:
#     if 'b' in item:
#         frutas2.append(item)

frutas2 = [item for item in frutas1 if 'b' in item]

print(frutas2)
'''

'''
# valores = []

# for x in range(6):
#     valores.append(x * 10)
#
# print(valores)

valores = [x * 10 for x in range(6)]
print(valores)
'''

# Lista e generator expressions

numeros = [x * 10 for x in range(100)]
print(getsizeof(numeros))
print(numeros)

print('============')

numeros = (x * 10 for x in range(100)) # Generator object has parenteses instead of square brackets, this also shows the output instead of keeping in memory
print(getsizeof(numeros))
print(numeros)

