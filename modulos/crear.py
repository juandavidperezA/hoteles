import json
import os            
base_dir=os.path.dirname(os.path.abspath(__file__))
ruta= os.path.join(base_dir,"hoteles.json")   

def crear():
    print("""==========================================================================
bienvenido a la creacion de hoteles
==================================================================================
ingresa los siguientes datos para realizar la creacion del hotel:

-nombre del hotel
-ciudad que pertenece el hotel
""")
    while True:
        
        nombre=input("ingrese el nombre del hotel:")
        seguro=input("esta bien escrito el nombre? s/n (obligatorio responder por seguridad)")
            
    
    
        if seguro.lower()=="s":
            print("entendido")
            break
        elif seguro.lower()=="n":
            nombre=input("entendido... vuelve a escribir el nombre correcto del hotel ")
            continue

    while True:
        ciudad=input("ingresa el nombre de la ciudad: ")
        seguro1=input("estas seguro que esa es la ciudad del hotel?")


        if seguro1.lower()=="s":
            print("entendido")
            break
        elif seguro1.lower()=="n":
            ciudad=input("entendido... vuelve a escribir la ciudad correcto del hotel ")
            continue

    try:
        with open (ruta, "r") as f:
            datos=json.load(f)
    except FileNotFoundError:
        datos=[]
        
    if len(datos)==0:
        nuevo_id=1
    else:
        nuevo_id=max(hotel["id"] for hotel in datos)+1
    hotel={
                "id" : nuevo_id,
                "nombre del hotel: ": nombre,
                "ciudad del hotel": ciudad   
            }
    datos.append(hotel)
            
    with open (ruta, "w") as f:
        json.dump(datos, f, indent=4)
            
    print(f"hotel creado con ID {nuevo_id}")
