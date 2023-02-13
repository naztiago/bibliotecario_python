def eliminar_usuario(dataset : dict) -> dict:
    """_Elimina un usuario seleccionado en caso de que este exista_

    Args:
        dataset (dict): recibe un diccionario
    
    Return: key and value dentro de el diccionario seleccionado  
        
    """
    
    try:
        name:str = str(input('ingresa el nombre: '))
        del dataset[name]
        input(f'se elimino el usuario {name}')
    except:
        input('ese usuario no existe')