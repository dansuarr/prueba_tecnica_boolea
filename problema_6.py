from typing import List


def ordenar_ceros_y_unos(lista: List[int]) -> List[int]:
    numeros_validos = {0, 1}
    if not set(lista).issubset(numeros_validos):
        raise ValueError('La lista debe contener solo ceros y unos.')
    return sorted(lista)


lista = input('Introduce una lista de ceros y unos separados por comas: ')
lista = [int(x) for x in lista.split(',')]
resultado = ordenar_ceros_y_unos(lista)
print(f'Lista ordenada: {resultado}')
