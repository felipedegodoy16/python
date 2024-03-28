# Mostrará a letra 'X' caso o valor do item da lista seja 4 ou 8

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in range (0,10):
    if lista[item] == 4 or lista[item] == 8:
        lista[item] = "X"
    print (lista[item])