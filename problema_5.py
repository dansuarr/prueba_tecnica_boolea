from typing import List, Tuple


def subsecuencia_suma_maximal(lista: List[int]) -> Tuple[List[int], int]:
    if all(x <= 0 for x in lista):
        valor_maximo = max(lista)
        return ([valor_maximo], valor_maximo)

    subsecuencia = [x for x in lista if x > 0]
    suma = sum(subsecuencia)
    return (subsecuencia, suma)


lista = input('Introduce una lista de números enteros separados por comas: ')
lista = [int(x) for x in lista.split(',')]
resultado = subsecuencia_suma_maximal(lista)
print(f'El resultado es: {resultado}')
