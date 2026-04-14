from modulos.lista import lista
from modulos.habitaciones import habitaciones_hotel
from modulos.crear import crear

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
