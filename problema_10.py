class Catalogo:
    def __init__(self):
        self.articulos = {}

    def agregar_producto(self, producto):
        nombre_producto = producto.producto
        self.articulos[nombre_producto] = producto

    def obtener_producto(self, nombre_producto: str):
        return self.articulos.get(nombre_producto)

    def mostrar_catalogo(self):
        for producto in self.articulos.values():
            print(producto)


class Producto:
    def __init__(self, producto: str, precio: float, n_unidades: int, catalogo):
        self.producto = producto
        self.precio = precio
        self.n_unidades = max(0, n_unidades)
        catalogo.agregar_producto(self)

    def actualizar_unidades_disponibles(self, cantidad: int):
        if cantidad < 0 and abs(cantidad) > self.n_unidades:
            print(f'No hay suficientes unidades disponibles de {self.producto}. '
                  f'Queda(n) {self.n_unidades} unidad(es) en stock.')
        else:
            self.n_unidades += cantidad

    def __str__(self):
        return f'Producto: {self.producto}, Precio: {self.precio} € por unidad, Unidades disponibles: {self.n_unidades}'


class Carrito:
    def __init__(self, catalogo):
        self.catalogo = catalogo
        self.articulos = {}

    def agregar_producto(self, nombre_producto: str, cantidad: int):
        producto = self.catalogo.obtener_producto(nombre_producto)
        if producto is None:
            print(f'El producto {nombre_producto} no está en el catálogo.')
            return None
        if cantidad <= 0:
            print('La cantidad debe ser positiva.')
            return None
        if cantidad > producto.n_unidades:
            print(f'No hay suficientes {nombre_producto}. '
                  f'Solo queda(n) {producto.n_unidades} unidad(es) en stock.')
        else:
            producto.actualizar_unidades_disponibles(-cantidad)
            if nombre_producto in self.articulos:
                self.articulos[nombre_producto] += cantidad
            else:
                self.articulos[nombre_producto] = cantidad
            print(f'Se ha añadido {cantidad} {nombre_producto} al carrito.')

    def eliminar_producto(self, nombre_producto: str, cantidad: int):
        if nombre_producto not in self.articulos:
            print(f'El producto {nombre_producto} no está en el carrito.')
            return None

        if cantidad >= self.articulos[nombre_producto]:
            cantidad_a_eliminar = self.articulos[nombre_producto]
            del self.articulos[nombre_producto]
            print(f'El producto {nombre_producto} se ha eliminado del carrito.')
        else:
            cantidad_a_eliminar = cantidad
            self.articulos[nombre_producto] -= cantidad

        producto = self.catalogo.obtener_producto(nombre_producto)
        producto.actualizar_unidades_disponibles(cantidad_a_eliminar)
        print(f'Se han eliminado {cantidad_a_eliminar} {nombre_producto} del carrito.')

    def mostrar_carrito(self):
        if not self.articulos:
            print('El carrito está vacío.')
            return None

        print('Contenido:')
        total = 0
        for nombre, cantidad in self.articulos.items():
            producto = self.catalogo.obtener_producto(nombre)
            coste = producto.precio * cantidad
            total += coste
            print(f'- {nombre}: {cantidad} unidad(es) x {producto.precio} € = {coste} €')
        print(f'Total: {total} €')


# Creamos el catálogo
catalogo = Catalogo()

# Creamos productos y los añadimos al catálogo
camisetas = Producto('Camisetas', 20.0, 10, catalogo)
gorras = Producto('Gorras', 10.0, 5, catalogo)
sudaderas = Producto('Sudaderas', 35.0, 7, catalogo)

print('\nDisponible en el catálogo:')
catalogo.mostrar_catalogo()
print('\n')

# Creamos un carrito vacio asociado al catálogo y añadimos algunos productos al carrito
mi_carrito = Carrito(catalogo)
mi_carrito.mostrar_carrito()
print('\n')

mi_carrito.agregar_producto('Camisetas', 2)
mi_carrito.agregar_producto('Gorras', 2)
mi_carrito.agregar_producto('Sudaderas', 1)

# Intentamos añadir más de lo que hay en stock
mi_carrito.agregar_producto('Camisetas', 20)

# Mostramos el contenido del carrito tras haber añadido los productos
print('\nCarrito tras añadir productos:')
mi_carrito.mostrar_carrito()
print('\n')

# Eliminamos algunos de ellos del carrito
mi_carrito.eliminar_producto('Gorras', 1)
mi_carrito.eliminar_producto('Sudaderas', 2)

# Mostramos el contenido del carrito de nuevo
print("\nCarrito tras eliminar productos:")
mi_carrito.mostrar_carrito()
print("\n")

# Mostramos el catálogo actualizado con el stock restante
print("Catálogo actualizado:")
catalogo.mostrar_catalogo()
