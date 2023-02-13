

def agregar_usuario(dataset : dict) -> dict:
    """_Agregar un usuario y un libro a un Diccionario_
    si no se ha escrito ningun valor tambien devuelve error

    Args:
        dataset (dict): Recibe un diccionario
    
    Return: dict   
        
    """
    
    try:
        name:str = str(input('ingresa el nombre: '))
        book:str = str(input('ingresa el libro que se va a prestar: '))
        dataset.update({name:book})
        if len(dataset[name]) == 0:
            del dataset[name]
            print('no has ingresado ningun valor')
            input('')
        else:    
            input(f'se ha agregado el usuario: {name} \nque ha prestado el libro: {book}')
    except:
        input('no se puede realizar esta accion')