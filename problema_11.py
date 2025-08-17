import asyncio
import aiohttp
import time


async def hacer_peticion(cliente, url):
    async with cliente.get(url) as respuesta:
        await respuesta.text()


async def lanzar_peticiones(url):
    async with aiohttp.ClientSession() as cliente:
        peticiones = [
            hacer_peticion(cliente, url) for _ in range(1000)
        ]
        await asyncio.gather(*peticiones)


# Ejemplo:
url = 'https://es.wikipedia.org/wiki/Covadonga'
t_inicial = time.time()
asyncio.run(lanzar_peticiones(url))
t_final = time.time()
delta_t = round(t_final - t_inicial, 2)
print(f'¡Hecho! Tiempo total: {delta_t} segundos.')
