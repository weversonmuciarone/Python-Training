'''
Criar um programa que calcula a quantidade de tinta necessaria para pintar uma parede. O usuario devera fornecer as seguintes informacoes: Rendiment,
altura e largura.

O programa deve mostrar na tel a mensagem "Voce necessita de x latas de tinta".
'''

try:
    rendimento = float(input('Qual e o rendimento da lata? '))
    altura = float(input('Qual a altura da parede? '))
    largura = float(input('Qual a altura da parede? '))
except ValueError:
    print('O valor deve ser numerico')
else:
    # resultado = altura * largura / rendimento
    # print(f'Voce precisa de {resultado:.2f} latas de tinta.')
    def calc_tinta():
        area = altura * largura
        total = area / rendimento
        print(f'Voce precisa de {total:.2f} latas de tinta.')
    calc_tinta()