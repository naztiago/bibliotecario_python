

def agregar_usuario(dataset : dict):
    """_Agregar o actualiza un usuario y un libro a un Diccionario_

    Args:
        dataset (dict): Recibe un diccionario
    
    Return: dict   
        
    """
    
    try:
        name:str = str(input('ingresa el nombre: '))
        book:str = str(input('ingresa el libro que se va a prestar: '))
        dataset.update({name:book})
    except:
        print('no se puede realizar esta accion')