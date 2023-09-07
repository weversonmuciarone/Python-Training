from array import array

# estados = ['Minas Gerais', 'Sao Paulo', 'Rio de Janeiro', 'Bahia']
# minas = [['Minas Gerais = ' 'PC', 'PA', 'BH'], ['Sao Paulo = Mogi Guacu, Mogi Mirim, Campinas']]
# print(minas[0] [0])
'''
Unpacking Variables

products = ['Rice', 'Beans', 'Orange', 'Banana', 1, 2, 3]

# item1 = products[0]
# item2 = products[1]
# item3 = products[2]
# item4 = products[3]

# item1, item2, item3, item4 = products
item1, item2, item3, *others = products

print(item1)
print(item2)
print(item3)
print(others)
'''
'''
stock = ['Red', 'Green', 'Blue', 'Yellow']
colour = input('Please digit a colour: ').capitalize()

if colour in stock:
    print('Sim')
else:
    print('Nao')

'''

# name = 'Weverson'
# print(list(name))

'''
#Using ZIP

colour = ['Red', 'Green', 'Blue', 'Yellow']
value = [10, 20, 30, 40]

join_list = zip(colour, value)
print(list(join_list))
'''


'''
Criar uma lista de frutas a partir do input fornecido pelo usuario.abs

frutas_usuario = input('Digite o nome das frutas separados por virgula: ').capitalize()
frutas_lista = frutas_usuario.split(', ')

print(frutas_lista)
'''

'''
Tuples

Armazenar mais de uma informacao em variaveis
Mater a seqiencia dos dados
Nao podm ser alteradas (Immutable) nao se pode alterar, append as an example

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(cores_list)
print(cores_tuple)

'''
'''
Array needs to be imported as from array import array

similar to lists but has a better performance

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd']) # the 'u', 'i', and 'f' in these examples are the types 'u' stands for str whereas 'i' integer
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)

'''
'''
frutas = ['maca', 'maca', 'maca', 'laranja', 'abacate', 'banana']

contador = 0

for fruta in frutas:
    if fruta == 'maca':
        contador += 1
print(contador)
'''
'''
num = 10
try:
    num_usuario = int(input('Favor digite um numero: '))
except ValueError:
    print('Favor digitar um numero inteiro!')
else:
    if num_usuario >= num:
        print(f'O Numero {num_usuario} que voce digitou e maior ou igual a {num}')
    else:
        print(f'O Numero {num_usuario} que voce digitou e menor do que {num}')
'''
'''
carros = ['BMW X6', 'BMW I5', 'BMW I8']
try:
    stock = input('Qual o carro que voce deseja comprar? ').upper()
except ValueError:
    print('Favor digitar o nome do veiculo!')
else:
    if stock in carros:
        print('Este carro esta disponivel!')
    else:
        print('Este carro nao esta disponivel!')
'''
'''
fruta = 'Abacate'

try:
    nome = input('Digite o nome de uma fruta e tente acertar: ').capitalize()
except ValueError:
    print('Favor digitar um nome valido!')
else:
    while nome != fruta:
        nome = input('Digite o nome de uma fruta e tente acertar: ').capitalize()
    print('Parabens! Voce digitou a fruta correta.')
'''
# Pais = [['Brazil = ' 'Brasilia'], ['Inglaterra = ' 'Londres'], ['Italia = ' 'Roma'], ['Espanha = ' 'Madrid'], ['Portugal = ' 'Lisboa']]
# capital = []
#
# paizes = input('Digite o nome de uma Pais: ').capitalize()

pais = ['Brazil', 'Italia', 'Espanha']
capital = ['Brasilia', 'Roma', 'Madrid']
try:
    cliente = input('Digite um Pais para saber sua capital: ').capitalize()
except ValueError:
    print('Favor digitar o nome de um pais.')
else:
    join_list = zip(pais, capital)
    if cliente == pais[0]:
        print(f'A capital do {pais[0]} e {capital[0]}')
    elif cliente == pais[1]:
        print(f'A capital da {pais[1]} e {capital[1]}')
    elif cliente  == pais[2]:
        print(f'A capital da {pais[2]} e {capital[2]}')
    else:
        print('Desculpe, nao temos informacoes sobre a capital deste pais.')