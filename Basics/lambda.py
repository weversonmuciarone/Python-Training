
# Lambda function
#     E uma funcao pequena sem nome portanto deve se iniciar sempre com lambda
#     pode ter varios argumentos mas so uma expressao
#     Muiti utilizado dentro de outras funcoes
#     Codigo mais clean

# def somar(x):
#     return  x + 10
#
# print(somar(2))

# somar10 = lambda x, y: x + 10 * y # Antes dos dois pontos sao os argumentos e apos sao as expressoes
# print(somar10(2, 2))

#lambda dentro de uma funcao

# def somar(x):
#     func2 = lambda x: x + 10
#     return func2(2) * 4
# print(somar(2))

# Map Functions
#     Muito utilizado com listas
#     Aplicar uma funcao a um iterabe por item. (list, tuple, dic, etc..)
'''
lista1 = [1, 2, 3, 4]
#
# def multi(x):
#     return x * 2
#
# lista2 = map(multi, lista1)
# print(list(lista2))

print(list(map(lambda x: x * 2, lista1)))
'''

num = int(input('Digite um numero inteiro: '))

cubo = lambda x: x ** 3

print(f'O cubo de {num} e {cubo(num)}')

