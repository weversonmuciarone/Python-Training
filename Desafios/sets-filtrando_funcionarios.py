
'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

List1 = Funcionarios que tem carro e trabalha a noite
Lista2 = Funcionarios que tem carro e trabalha durante o dia
Lista3 = Funcionarios que nao tem carro
'''
'''
funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sofia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sofia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

list1 = set(turno_dia).intersection(tem_carro)
print(list1)

list2 = set(turno_noite).intersection(tem_carro)
print(list2)

list3 = set(funcionarios).difference(tem_carro)
print(list3)
'''
nome1 = {'Pingo', 'Tiago', 'Ricardo', 'Leandro'}
nome2 = {'Pingo', 'Tiago', 'Jose', 'Joao', 'Roberto'}

res = nome1.intersection(nome2)
print(res)
