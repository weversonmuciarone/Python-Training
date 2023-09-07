
# Dicionarios
#     Utiliza index no formato de keys and values
#     Aceita string, integer, float, etc..

'''
aluno = {'nome': 'Ana', 'Idade': 16, 'nota_final': 'A', 'Aprovacao': True}
aluno.update({'nome': 'Jose', 'Idade': 20, 'endereco': 'Rua A'})

print(aluno.get('endereco', 'Nao existe'))
'''
'''
aluno = {'nome': 'Ana',
         'Idade': 16,
         'nota_final': 'A',
         'Aprovacao': True
        }
print(aluno)

for x in aluno.items():
    print(x)

for x in aluno.values():
    print(x)

for a, b in aluno.items():
    print(a, b)
    '''
lista = {'Brasil': 'Brasilia',
        'Italia': 'Roma',
        'Espanha': 'Madrid',
        'Egito': 'Cairo'
        }
pais = input('Digite o nme de um pais: ').capitalize()

if pais in lista:
        print(f'A capital do(a) {pais} e {lista[pais]}')
else:
        print('Desculpe, nao temos informacoes deste pais.')