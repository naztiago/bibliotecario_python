def actualizar_usuario(dataset : dict) -> dict:
    """Actualiza un usuario y un libro a un Diccionario_

    Args:
        dataset (dict): Recibe un diccionario
    
    Return: dict   
        
    """
    
    try:
        name:str = str(input('ingresa el nombre: '))
        if name in dataset:
            book:str = str(input('ingresa el nuevo libro que se va a prestar: '))
            dataset.update({name:book})
            if len(dataset[name]) == 0:
                del dataset[name]
                print('no has ingresado ningun valor')
                input('')
            else:    
                input(f'se ha actualizado el usuario: {name} \nque ha prestado el libro: {book}')
        else:
            print('ese usuario no existe')
            input(' ')
    except:
        input('no se puede realizar esta accion')