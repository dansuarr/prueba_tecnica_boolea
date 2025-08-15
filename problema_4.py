class CustomString:
    # Solo letras de la a-z mayúsculas y minúsculas (excluyendo la ñ) y espacios
    caracteres_permitidos = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

    def __init__(self, texto):
        self.texto = self._filtrar(texto)

    def _filtrar(self, texto):
        return ''.join(i for i in texto if i in self.caracteres_permitidos)

    def __str__(self):
        # Hacemos que el objeto se comporte como un string al hacer un print
        return self.texto

    def __add__(self, texto_adicional):
        return CustomString(self.texto + self._filtrar(texto_adicional))


mensaje = input('Introduce un texto: ')
mensaje_filtrado = CustomString(mensaje)
mensaje_adicional = input('Añade un texto adicional: ')
mensaje_filtrado += mensaje_adicional
print(f'Texto filtrado: {mensaje_filtrado}')
