import re


class Usuario:
    total_usuarios = 0

    def __init__(self, nombre: str, clave: str):
        self.nombre = nombre  # atributo público
        self.__clave = self._validar_clave(clave)  # privada
        Usuario.total_usuarios += 1

    @classmethod
    def numero_usuarios(cls) -> str:
        return f'El número de usuarios creados es {cls.total_usuarios}.'

    @staticmethod
    def _validar_clave(clave: str) -> str:
        """
        Comprueba que la contraseña tenga:
        - Al menos 8 caracteres.
        - Al menos una letra mayúscula.
        - Al menos un número.
        - Al menos un caracter especial.
        """
        if len(clave) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres.')
        if not re.search(r'[A-Z]', clave):
            raise ValueError('La contraseña debe contener al menos una letra mayúscula.')
        if not re.search(r'\d', clave):
            raise ValueError('La contraseña debe contener al menos un número.')
        if not re.search(r'[_\W]', clave):
            raise ValueError('La contraseña debe contener al menos un caracter especial.')

        return clave


# Ejemplo:
u1 = Usuario('Dani', 'QAer1243_')
print(Usuario.numero_usuarios())
u2 = Usuario('Alex', 'fD4m3na*v')
print(Usuario.numero_usuarios())
