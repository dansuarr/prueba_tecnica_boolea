from typing import List

lista = [1, 1, 0]


def ordenar_ceros_y_unos(lista: List[int]) -> List[int]:
    numeros_validos = {0, 1}
    if not set(lista).issubset(numeros_validos):
        raise ValueError('La lista debe contener solo 0 y 1.')
    return sorted(lista)


b = ordenar_ceros_y_unos(lista)
print(b)