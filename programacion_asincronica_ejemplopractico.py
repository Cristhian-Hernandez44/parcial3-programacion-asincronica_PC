!pip install nest_asyncio

import asyncio
import random
import nest_asyncio

nest_asyncio.apply()

# Simulación de un agente del call center atendiendo una solicitud
async def atender_solicitud(agente_numero, solicitud):
    print(f"Agente {agente_numero} está atendiendo la solicitud: {solicitud}")
    tiempo_atencion = random.randint(1, 5)  # Generacón de un tiempo aleatorio para la solicitud
    await asyncio.sleep(tiempo_atencion)  # Tiempo de esppera para solucionar solicitud
    print(f"Agente {agente_numero} ha podido solucionar la solicitud: {solicitud}")

# Función principal que simula la recepción y atención de solicitudes
async def main():
    agentes = ["1", "2", "3"]

    solicitudes = [
        "Solicitud 1: Problema con factura",
        "Solicitud 2: Cambio de dirección",
        "Solicitud 3: Consulta de saldo",
        "Solicitud 4: Reporte de falla técnica",
        "Solicitud 5: Solicitud de soporte"
    ]

    # Creamos una lista de tareas para atender las solicitudes
    tareas = []
    for i, solicitud in enumerate(solicitudes):
        agente = agentes[i % len(agentes)]  
        tarea = atender_solicitud(agente, solicitud)  # Creamos la tarea para atender la solicitud
        tareas.append(tarea)  

    await asyncio.gather(*tareas)

asyncio.run(main())