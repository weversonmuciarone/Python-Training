import boto3
from datetime import datetime

'''
class Funcionarios:
    nome = 'Weverson'
    Sobrenome = 'Muciarone'

usuario = Funcionarios()

print(usuario.nome)
'''
'''
# cria a classe
class Funcionarios:
    pass # passa a classe vazia
# cria o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# criar os parametros do usuario1
usuario1.nome = 'Weverson'
usuario1.sobrenome = 'Muciarone'
usuario1.dob = '16/08/1984'

# criar os parametros do usuario2
usuario2.nome = 'Luana'
usuario2.sobrenome = 'Cristina'
usuario2.dob = '16/08/1992'

print(usuario1.nome)
print(usuario2.nome)
'''
'''
class Funcionarios:
    def __init__(self, nome, sobrenome, dob):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dob = dob

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome + ' ' + self.dob

usuario1 = Funcionarios('Weverson', 'Muciarone', '16/08/1984')
usuario2 = Funcionarios('Luana', 'Soares', '16/08/1992')

# print(usuario1.nome)
# print(usuario2.nome)

print(Funcionarios.nome_completo(usuario1))
'''
class Funcionarios:
    def __init__(self, nome, sobrenome, yob):
        self.nome = nome
        self.sobrenome = sobrenome
        self.yob = yob

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def yobirth(self):
        return self.yob

    def idade_func(self):
        ano_atual = datetime.now().year
        return ano_atual - self.yob

# usuario1 = Funcionarios('Weverson', 'Muciarone', 1984)
# usuario2 = Funcionarios('Luana', 'Soares', 1992)

# print(Funcionarios.nome_completo(usuario1))
# print(Funcionarios.idade_func(usuario1))
# print(f'O Funcionario {Funcionarios.nome_completo(usuario1)} nasceu em {str(Funcionarios.yobirth(usuario1))} portanto ele tem'
#       f' {Funcionarios.idade_func(usuario1)} anos '
#       f'de idade!')


