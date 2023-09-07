
# Filter Functions
#     Muito utilizado com listas
#     Aplicat uma funcao a um iterable, filtrando os items. (Listas, Tuples, dict, etc).

valores = [10, 12, 34, 44, 57]

# def menor_vinte(x):
#     return x > 20

# print(list(filter(menor_vinte, valores)))

print(list(filter(lambda x: x > 20, valores)))