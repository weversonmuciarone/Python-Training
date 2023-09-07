import math
# def welcome():
#     print('Welcome Weverson')
#     print('We have 5 laptops')
#
# welcome()

# def welcome(name, quantity):
#     print(f'Welcome {name}')
#     print(f'We have {str(quantity)} laptops')
#
# welcome('Weverson', 5)

# def sum(*numbers):
#     result = 0
#     for num in numbers:
#         result += num
#     return result
#
# x = sum(2, 3, 5)
# print(x)
'''
def agency(**car):
    return car
print(agency(Branch = 'GOL', Colour = 'Blue', Engine = 1.4))
print(agency(Branch = 'GOL', Colour = 'Blue', Engine = 1.4, Plate = 1234))
print(agency(Branch = 'GOL'))
'''
'''
try:
    num = float(input('Por favor digite um numero para saber seu valor em quadrado: '))
except ValueError:
    print('Favor digitar um valor numerico')
else:
    def quadrado(numero):
        return numero ** 2

    print(f'O quadrado de {num} e {quadrado(num)}')
'''
'''
try:
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite o segundo numero: '))
except ValueError:
    print('Favor digitar um valor numerico!')
else:
    def somar(numero1, numero2):
        result = numero1 + numero2
        print(f'A soma de {num1} + {num2} e igual a {result}')
    somar(num1, num2)
'''

print('Encontrar a potencia de um numero')
print('---------------------------------')

base_usuario = int(input('Digite o valor da base: '))
pot_usuario = input('Digite o vaalor da potencia: ')

'''
def potencia(base, pot=2):
    return base ** pot
if pot_usuario:
    print(f'A potencia de {base_usuario} e {potencia(base_usuario, int(pot_usuario))}')
else:
    print(f'A potencia de {base_usuario} e {potencia(base_usuario)}')
'''