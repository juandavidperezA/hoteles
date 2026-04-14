import os
from menup import menu
base_dir=os.path.dirname(os.path.abspath(__file__))
ruta= os.path.join(base_dir,"hoteles.json")


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