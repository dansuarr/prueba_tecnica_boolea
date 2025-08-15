def suma_digitos(n: int) -> int:
    return sum(int(i) for i in str(n))


def funcion_personalizada(n: int) -> str:
    if n <= 100:
        raise ValueError('El número debe ser mayor que 100.')

    suma = suma_digitos(n)
    while suma > 9:
        suma = suma_digitos(suma)

    resultado = str(suma) + str(n)

    return resultado


numero = int(input('Introduce un número entero positivo mayor que 100: '))
resultado = funcion_personalizada(numero)
print(f'El resultado es: {resultado}')
