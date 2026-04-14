import json
import os
base_dir=os.path.dirname(os.path.abspath(__file__))
ruta= os.path.join(base_dir,"hoteles.json")

#no se que hacwer
def cuenta():
    usuario= "juandavidperezanaya@gmail.com"
    clave= "holaquehace12"
    while True:
        print("""================================================================================================================
bienvenido al sistema de holteles de colombia 
====================================================================================================================

1. iniciar sesion 
2. salir""")
        
        try:
            opcion=int(input("ingresa un opcion: "))
        except ValueError:
            print("accion no valida debe ser numerica")
            return
        if opcion==1:
                usuario1=input("correo electronico: ")
                clave1=input("ingresa la clave: ")
    
                if usuario1 == usuario and clave1 != clave:
                    print("el correo esta bien no obstante la clave es incorrecta vuelve a intentar...")
                    continue
                elif usuario1 != usuario and clave1==clave:
                    print("la clave esta correcta no obstante el correo electronico es incorrecto... intenta de nuevo... ")
                    continue
                elif usuario1!= usuario and clave1!= clave:
                    print("correo y clave incorrectas intenta de nuevo...")
                    continue
                elif usuario1==usuario and clave1==clave:
                    print("acceso permitido bienvenido :3")
                    menu()
        elif opcion==2:
            print("saliendo...")
            break




def menu():
    while True:
        print("""======================================================================
        sistema de reserva de hoteles
=========================================================================
opociones disponibles:

1. Crear hotel
2. Agregar habitación a hotel
3. Listar hoteles
4. cerrar sesion""")
    
        try:
            opcion= int(input("ingresa una opcion: "))
        except ValueError:
            print("accion no valida debe ser numerica: ")
            continue
        if opcion==1:
            crear()
        elif opcion==2:
            habitaciones_hotel()
        elif opcion==3:
            lista()
        elif opcion==4:
            opcion1=input("esta seguro de cerrar sesion ? s/n")
        
            if opcion1.lower()== "s":
                print("saliendo del progragma...")
                break
            elif opcion1.lower()=="n":
                print("entendido regresando al menu principal...")
                continue
            else:
                print("la accion es invalida...")
                return
        else:
            print("accion no valida")    
            
            
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

    
    

cuenta()
