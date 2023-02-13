from agregar_usuario import *
from actualizar_usuario import *
from actualizar_usuario_nombre import *
from eliminar_usuario import *
from ver_libro_usuario import *
from os import system


def programa_base(personas:dict) -> str:
    """_Imprimir menu_
    
    tambien dentro del menu llama a las funciones correspondientes de cada opcion
    
    Args:
        dataset (dict): recibe un diccionario
    
    Return: no se que retorna :v  
        
    """
    while True:
        system("clear")
        print("-"*50)
        print('\033[3m'
        """
        Seleccione una acción.
        1. registrar usuario.
        2. actualizar.
        3. eliminar 
        4. visualizar
        (x) salir
        """
        )
        seleccion = input("selección: ")
        
        if seleccion == "1":
            system("clear")
            agregar_usuario(personas)
        
        if seleccion == "2":
            system("clear")
            if len(personas) == 0:
                input('No existen usuarios todavia')
            else:  
                menu_actualizar(personas)
        
        if seleccion =="3":
            system("clear")
            if len(personas) == 0:
                input('No existen usuarios todavia')
            else:    
                menu_eliminar(personas)
            
        if seleccion == "4":
            system("clear")
            if len(personas) == 0:
                input('No existen usuarios todavia')
            else:  
                menu_visualizacion(personas)
        
        if seleccion == "x":
            break
        print("-"*50)
        

def menu_actualizar(personas:dict) -> str:
    """_Imprimir menu de eliminacion_
    tambien dentro del menu llama a las funciones correspondientes de cada opcion
    Args:
        dataset (dict): recibe un diccionario
    
    Return: no se que retorna :v 
    """
    while True:
        system("clear")
        print("-"*50)
        print(
        """
        Seleccione una acción.
        1. Actualizar libro prestado.
        2. Actualizar nombre de usuario ya existente.
        (x) salir
        """
        )
        seleccion = input("selección: ")
        
        if seleccion == "1":
            system("clear")
            actualizar_usuario(personas)
             
        if seleccion =="2":
            system("clear")
            actualizar_usuario_nombre(personas)
        
        if seleccion == "x":
            break
        print("-"*50)

def menu_eliminar(personas:dict) -> str:
    """_Imprimir menu de eliminacion_
    tambien dentro del menu llama a las funciones correspondientes de cada opcion
    Args:
        dataset (dict): recibe un diccionario
    
    Return: no se que retorna :v 
    """
    while True:
        system("clear")
        print("-"*50)
        print(
        """
        Seleccione una acción.
        1. Eliminar un usuario en especifico.
        2. Eliminar todos los usuarios.
        (x) salir
        """
        )
        seleccion = input("selección: ")
        
        if seleccion == "1":
            system("clear")
            eliminar_usuario(personas)
             
        if seleccion =="2":
            system("clear")
            personas.clear()
            print('\nLa lista de usuarios se ha borrado completamente')
            input(personas)
        
        if seleccion == "x":
            break
        print("-"*50)
        
def menu_visualizacion(personas:dict) -> str:
    """_Imprimir menu de visualizacion_
    tambien dentro del menu llama a las funciones correspondientes de cada opcion
    Args:
        dataset (dict): recibe un diccionario
    
    Return: no se que retorna :v 
    """
    while True:
        system("clear")
        print("-"*50)
        print(
        """
        Seleccione una acción.
        1. Ver libro prestado por un usuario en especifico.
        2. Ver todos los usuarios.
        (x) salir
        """
        )
        seleccion = input("selección: ")
        
        if seleccion == "1":
            system("clear")
            ver_libro_usuario(personas)
             
        if seleccion =="2":
            system("clear")
            print('\nLa lista de usuarios es la siguiente')
            print(f' {personas}')
            input(' ')
        
        if seleccion == "x":
            break
        print("-"*50)