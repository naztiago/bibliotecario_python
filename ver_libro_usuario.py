def ver_libro_usuario(dataset : dict):
    """_visualiza el value correspondiente a una key en especifico_

    Args:
        dataset (dict): recibe un diccionario
    
    Return: key and value dentro de el diccionario seleccionado  
        
    """
    
    try:
        name:str = str(input('ingresa el nombre: '))
        print(f'el usuario {name} tiene el libro: ',dataset[name])
    except:
        print('ese usuario no existe')