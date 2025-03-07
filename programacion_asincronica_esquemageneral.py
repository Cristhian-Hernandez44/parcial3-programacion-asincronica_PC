!pip install nest_asyncio 
import asyncio
import nest_asyncio

nest_asyncio.apply()  

async def fetch_data_1():
    await asyncio.sleep(2)  # Simulamos una operación que toma tiempo
    return "Data 1 fetched"

async def fetch_data2():
    await asyncio.sleep(1)  # Simulamos una operación que otro tiempo
    return "Data 2 fetched"

async def main():
    
   tarea_1 = asyncio.create_task(fetch_data_1())
   tarea_2 = asyncio.create_task(fetch_data2())

   resultado1 = await tarea_1
   resultado2 = await tarea_2

   print(resultado1)
   print(resultado2)

asyncio.run(main()) 
