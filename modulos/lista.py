import json
import os            
base_dir=os.path.dirname(os.path.abspath(__file__))
ruta= os.path.join(base_dir,"hoteles.json") 
 

def lista():
    
    print("""==================================================================================================================
bienvenido a la lista de hoteles
=================================================================================================================
""")
    
    try:
        with open (ruta, "r") as f:
            datos=json.load(f)
    except FileNotFoundError:
        print("no hay hoteles registrados... ")
        return
    
    if len(datos) == 0:
        print("no hay hoteles guardados")
        return

    for hotel in datos:
        print(f"ID: {hotel['id']} | Nombre: {hotel['nombre del hotel: ']} | Ciudad: {hotel['ciudad del hotel']}")
