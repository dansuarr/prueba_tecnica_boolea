def es_primo(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    # Probamos a dividir n entre todos los números enteros entre 3 y raiz de n.
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def es_primo_circular(n: int) -> bool:
    n_str = str(n)
    for i in range(len(n_str)):
        n_rotado = int(n_str[i:] + n_str[:i])
        if not es_primo(n_rotado):
            return False
    return True


numero = int(input('Introduce un número entero positivo: '))
if numero <= 0:
    raise ValueError('El número debe ser entero positivo.')

resultado = es_primo_circular(numero)

if resultado:
    print(f'El número {numero} es primo circular.')
else:
    print(f'El número {numero} no es primo circular.')
