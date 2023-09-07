import math
# Calculo de IMC - Indice de massa corporal

'''
Qual e a sua altura em cm?
Qual e o seu peso?

MENOR QUE 18,5  MAGREZA
ENTRE 18,5 E 24,9  NORMAL
ENTRE 25,0 E 29,9  SOBREPESO
ENTRE 30,0 E 39,9 OBESIDADE
MAIS QUE 40,0 OBESIDADE GRAVE
'''

magro = 18.5
normal = 25
sobrepeso = 29.9
obeso = 39.9


try:
    altura = float(input('Qual a sua altura em cm? '))
    peso = float(input('Qual o seu peso? '))
except ValueError:
    print('Favor digitar valor numerico.')
else:
    def calc_imc():
        imc = peso / (altura / 100) ** 2
        if imc < magro:
            print(f'O seu IMC e {imc:.2f}. Voce esta abaixo do peso!')
        elif imc >= magro and imc < normal:
            print(f'O seu IMC e {imc:.2f}.Voce esta no peso normal!')
        elif imc > normal and imc <= sobrepeso:
            print(f'O seu IMC e {imc:.2f}.Voce esta com sobrepeso!')
        elif imc > sobrepeso and imc <= obeso:
            print(f'O seu IMC e {imc:.2f}.Voce esta obeso(a)')
        else:
            print(f'O seu IMC e {imc:.2f}.Voce esta com obesidade morbida!')
    calc_imc()
