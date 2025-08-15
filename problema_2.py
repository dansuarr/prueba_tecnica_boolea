numero = int(input('Introduce un número entero positivo: '))


def tiene_digitos_unicos(n: int) -> bool:
    if not isinstance(n, int) or n <= 0:
        raise ValueError('El número debe ser entero positivo.')

    n_str = str(n)
    n_distintos = set(n_str)
    return len(n_str) == len(n_distintos)


resultado = tiene_digitos_unicos(numero)

if resultado:
    print(f'Todos los dígitos del número {numero} son diferentes.')
else:
    print(f'El número {numero} tiene dígitos repetidos.')