def ver_libro_usuario(dataset : dict) -> dict:
    """_visualiza el value correspondiente a una key en especifico_
    - si no existe, da el mensaje de su inexistencia 

    Args:
        dataset (dict): recibe un diccionario
    
    Return: key and value dentro de el diccionario seleccionado  
        
    """
    
    try:
        name:str = str(input('ingresa el nombre: '))
        print(f'el usuario {name} tiene el libro: ',dataset[name])
        input(' ')
    except:
        input('ese usuario no existe')