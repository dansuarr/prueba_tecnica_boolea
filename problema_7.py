class Ordenador:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}'


class Sobremesa(Ordenador):
    def __init__(self, marca: str, modelo: str, volumen_cpu: int):
        super().__init__(marca, modelo)
        self.volumen_cpu = volumen_cpu  # [L]

    def __str__(self):
        return f'{super().__str__()}, Volumen: {self.volumen_cpu} L'


class Portatil(Ordenador):
    def __init__(self, marca: str, modelo: str, duracion_bateria: float):
        super().__init__(marca, modelo)
        self.duracion_bateria = duracion_bateria  # [h]

    def __str__(self):
        return f'{super().__str__()}, Batería: {self.duracion_bateria} h'


# Ejemplo:
o = Ordenador('ASUS', 'TUF Gaming A13')
s = Sobremesa('ASUS', 'TUF Gaming A14', 4)
p = Portatil('ASUS', 'TUF Gaming A15', 8)
print(o)
print(s)
print(p)
