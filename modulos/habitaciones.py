import json
import os            
base_dir=os.path.dirname(os.path.abspath(__file__))
ruta= os.path.join(base_dir,"hoteles.json") 
 
          
def habitaciones_hotel():
    print("""============================================================================
bienvenido a agregar habitacion al hotel
=================================================================================
ingresa los siguientes datos:

-ingresa la id del hotel
-ingresa el numero de la habitacion para agregar""")
    try:
        ids=int(input("ingresa el numero de id del hotel: "))
    except ValueError:
        print("no valido debe ser numerico: ")
        return
    try:
        with open(ruta,"r") as f:
            datos=json.load(f)
    except FileNotFoundError:
        print("no encontrado...")
        return 
        
    encontrado= False
    for g in datos:
        if ids==g["id"]:
            encontrado=True
            print(f"id del hotel encontrado es: {g['nombre del hotel: ']}")

            
            if "habitaciones" not in g:
                g["habitaciones"]= []
                
            habitaciones =g["habitaciones"]
            
            if len(habitaciones) == 0:
                id_habitacion= 1
            else:
                id_habitacion=max(h["id"] for h in habitaciones)+1
            

            numero=(input("ingresa el nombre de la habitacion: "))
            
            habitacion={
                "id": id_habitacion,
                "numero": numero,
                "disponible": True
            }
            
            habitaciones.append(habitacion)
            
            with open (ruta, "w") as f:
                json.dump(datos, f, indent=4)
                
            print(f"habitacion agregada con la id {id_habitacion}")
            
        
    if not encontrado:
        print("hotel no encontrado")    
