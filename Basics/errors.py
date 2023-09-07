
# Erros
#     Excelente para testes
#     Nao realiza o stop do programa
#     Mensagens custmizadas quando encontra um erro

'''
try:
    letras = ['a', 'b', 'c']
    print(letras[3])

except IndexError:
    print('Index nao existe')
'''

try:
    valor = int(input('Digite o valor do seu produto: '))
except ValueError:
    print('Favor digitar um numero inteiro')
else:               # Else permite voce executar um codigo caso o primeiro passe se nao passar o else nao sera executado
    result = valor * 2
    print(result)
# finally:
#     result2 = result * 2  finally executa o possimo codiso mesmo que o try tenha falhado
#     print(result2)
