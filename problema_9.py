import os


class GestorArchivos:
    def __init__(self, directorio: str):
        if not os.path.isdir(directorio):
            raise ValueError(f"{directorio} no es un directorio válido.")
        self.directorio = directorio

    def listar(self):
        archivos = [
            f for f in os.listdir(self.directorio)
            if os.path.isfile(os.path.join(self.directorio, f))
        ]
        for archivo in archivos:
            print(archivo)

    def crear(self, nombre_archivo: str):
        ruta = os.path.join(self.directorio, nombre_archivo)
        with open(ruta, 'w') as f:
            pass
        print(f'El archivo {nombre_archivo} ha sido creado.')

    def eliminar(self, nombre_archivo: str):
        ruta = os.path.join(self.directorio, nombre_archivo)
        if os.path.exists(ruta):
            os.remove(ruta)
            print(f'El archivo {nombre_archivo} ha sido eliminado.')
        else:
            print(f'El archivo {nombre_archivo} no existe.')

    @staticmethod
    def obtener_extension(nombre_archivo: str) -> str:
        return os.path.splitext(nombre_archivo)[1]


class GestorArchivosAudio(GestorArchivos):
    _extensiones_permitidas = ['.mp3', '.wav']

    def listar(self):
        archivos = [
            f for f in os.listdir(self.directorio)
            if os.path.isfile(os.path.join(self.directorio, f))
            and self.obtener_extension(f).lower() in self._extensiones_permitidas
        ]
        for archivo in archivos:
            print(archivo)

    def crear(self, nombre_archivo: str):
        extension = self.obtener_extension(nombre_archivo).lower()
        if extension in self._extensiones_permitidas:
            super().crear(nombre_archivo)
        else:
            print(f'Solo se pueden crear archivos de audio (.mp3, .wav).')

    def eliminar(self, nombre_archivo: str):
        extension = self.obtener_extension(nombre_archivo).lower()
        if extension in self._extensiones_permitidas:
            super().eliminar(nombre_archivo)
        else:
            print(f'Solo se pueden eliminar archivos de audio (.mp3, .wav).')
