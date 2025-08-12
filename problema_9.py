from typing import List

class GestorArchivos:
    def __init__(self, directorio: str):
        self.directorio = directorio

    def listar_archivos(self) -> List[str]:
        return self.directorio

    def crear_archivo(self):
        return None

    def eliminar_archivo(self):
        return None

    @staticmethod
    def obtener_extension(archivo: str) -> str:
        return None




class GestorArchivosAudio:
    def __init__(self):
        super().__init__()
