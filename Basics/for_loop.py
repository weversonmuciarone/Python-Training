from datetime import date

# todayDate = date.today().year
# birth_year = int(input("Please enter the year you were born: "))
# age = todayDate - birth_year
# print(f'{age}, years old')

# for n in range(6):
#     print(n)

# fruits = ['Banana, Apple, Grapes']
# for n in fruits:
#     print(n)

# word = 'Weverson'
# for w in word:
#     print(f'{w} is in the word {word}')

# purchase_confirmed = True
# purchase_data = 'Purchase of 12.50 successfull'
#
# for send in range(3):
#     if purchase_confirmed:
#         print(purchase_data)
#         print('Details has been sent to your email')
#         break
# else:
#     print('Purchase has failed')

# for num1 in range(1, 11):
#     print('Produto ' + str(num1))
#     for num2 in range(5):
#         print(num1, num2)

# word = 'separando'
# for w in word:
#     print(f'{w} ', end='')

# rows = 6
# columns = 6
# simbol = '@'
#
# for a in range(rows):
#     for b in range(columns):
#         print(f'{simbol}', end='')
#     print()
'''
print('For loop com break')
for n in range(1, 11):
    if n > 5:
        break
    print(n)
    continue
print('\nFor loop com continue')
for n in range(1, 11):
    if n != 5:
        print(n)
'''
'''
numeros = range(1, 11)

for numero in numeros:
    if numero % 2 == 0:
        print(f' O Numero {numero} e par.\n', end='')
    else:
        print(f' O numero {numero} e impar.')
    
'''
'''
try:
    num = int(input('Digite um numero para calcular o fatorial: '))
except ValueError:
    print('Favor digitar um numero inteiro!')
else:
    print('---------------------------------------------------')

    res = 1
    for n in range(1, num + 1):
        res *= n
    print(f'O fatorial de {num} e {res}')
'''

numeros = range(1, 11)
quadrado = lambda x: x ** 2
res = []
for i in numeros:
    res.append(quadrado(i))
print(f'O quadrado dos numeros {numeros} e {res}')
