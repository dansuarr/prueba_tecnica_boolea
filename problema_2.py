a = 123


def tiene_digitos_unicos(numero: int) -> bool:
    numero_str = str(numero)
    numeros_distintos = set(numero_str)
    len_numero = len(numero_str)
    len_numeros_distintos = len(numeros_distintos)

    if len_numero == len_numeros_distintos:
        return True
    else:
        return False


b = tiene_digitos_unicos(a)
print(b)