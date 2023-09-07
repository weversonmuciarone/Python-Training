
def somar():
    print('Esta funcao vai somar valores')


def multi():
    print('Esta funcao vail multiplicar valores')

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1