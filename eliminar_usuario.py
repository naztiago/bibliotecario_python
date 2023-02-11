def eliminar_usuario(dataset : dict):
    """_Elimina un usuario seleccionado_

    Args:
        dataset (dict): recibe un diccionario
    
    Return: key and value dentro de el diccionario seleccionado  
        
    """
    
    try:
        name:str = str(input('ingresa el nombre: '))
        del dataset[name]
        print(f'se elimino el usuario {name}')
    except:
        print('ese usuario no existe')