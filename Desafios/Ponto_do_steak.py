
'''
Criar um programa que dependendo da temperatura do steak ele retorma o ponto de cozimento. O usuario devra fornecer a temperatura.

Temperatura - Cozimento
48              Rare
54              Medium rare
60              Medium
65              Medium well
71              Well done
'''

rare = 48
medium_rare = 54
medium = 60
medium_well = 65
well_done = 71

try:
    ponto = int(input('Qual a temperatura da carne? '))
except ValueError:
    print('Favor digitar um numero inteiro')
else:
    # if ponto < rare:
    #     print('Steak undercooked! Cook further until it reaches the minimum temperature.')
    # elif ponto < medium_rare and ponto >= rare:
    #     print('rare')
    # elif ponto < medium and ponto >= medium_rare:
    #     print('Medium rare')
    # elif ponto < medium_well and ponto >= medium:
    #     print('Medium')
    # elif ponto <= well_done and ponto >= medium_well:
    #     print('Well done')
    # else:
    #     print('Steak overcooked')

    if ponto < rare:
        print('Steak undercooked! Cook further until it reaches the minimum temperature.')
    elif ponto in range(rare, medium_rare):
        print('rare')
    elif ponto in range(medium_rare, medium):
        print('Medium rare')
    elif ponto in range(medium, medium_well):
        print('Medium')
    elif ponto in range(medium_well, well_done):
        print('Well done')
    else:
        print('Steak overcooked')









