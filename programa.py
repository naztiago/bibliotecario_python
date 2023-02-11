from agregar_usuario import *
from eliminar_usuario import *
from ver_libro_usuario import *
from os import system


def programa_base(personas:dict):
    """_Imprimir menu_
    
    tambien dentro del menu llama a las funciones correspondientes de cada opcion
    
    Args:
        dataset (dict): recibe un diccionario
    
    Return: no se que imnprime :v  
        
    """
    while True:
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
        
        if seleccion == "1" or seleccion == "2":
            system("clear")
            agregar_usuario(personas)
        
        if seleccion =="3":
            menu_eliminar(personas)
            
        if seleccion == "4":
            menu_visualizacion(personas)
        
        if seleccion == "x":
            break
        print("-"*50)
        
        
def menu_eliminar(personas:dict):
    """_Imprimir menu_
    tambien dentro del menu llama a las funciones correspondientes de cada opcion
    Args:
        dataset (dict): recibe un diccionario
    
    Return: no se que imnprime :v 
    """
    while True:
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
            eliminar_usuario(personas)
             
        if seleccion =="2":
            personas.clear()
            print('\nLa lista de usuarios se ha borrado completamente')
            print(personas)
        
        if seleccion == "x":
            break
        print("-"*50)
        
def menu_visualizacion(personas:dict):
    """_Imprimir menu_
    tambien dentro del menu llama a las funciones correspondientes de cada opcion
    Args:
        dataset (dict): recibe un diccionario
    
    Return: no se que imnprime :v 
    """
    while True:
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
            ver_libro_usuario(personas)
             
        if seleccion =="2":
            print('\nLa lista de usuarios es la siguiente')
            print(personas)
        
        if seleccion == "x":
            break
        print("-"*50)