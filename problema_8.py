class Usuario:
    total_usuarios = 0

    def __init__(self, nombre: str, clave: str):
        self.nombre = nombre
        self.clave = clave
        Usuario.total_usuarios += 1

    @classmethod
    def obtener_numero_usuarios(cls):
        return cls.total_usuarios


