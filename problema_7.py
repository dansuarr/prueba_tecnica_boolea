class Ordenador:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo


class Sobremesa(Ordenador):
    def __init__(self, marca: str, modelo: str, volumen_cpu: int):
        super().__init__(marca, modelo)
        self.volumen_cpu = volumen_cpu


class Portatil(Ordenador):
    def __init__(self, marca: str, modelo: str, duracion_bateria: float):
        super().__init__(marca, modelo)
        self.duracion_bateria = duracion_bateria

