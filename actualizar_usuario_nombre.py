def actualizar_usuario_nombre(dataset : dict) -> dict:
    """_Elimina un usuario seleccionado en caso de que este exista_

    Args:
        dataset (dict): recibe un diccionario
    
    Return: key and value dentro de el diccionario seleccionado  
        
    """
    try:
        name:str = str(input('ingresa el nombre: '))
        book:str = dataset.get(name)
        if name in dataset:
            del dataset[name]
            new_name:str = str(input('ingresa el nuevo nombre: '))
            dataset.update({new_name:book})
            if len(dataset[new_name]) == 0:
                print('no has ingresado ningun valor')
                input('')
            else:    
                input(f'se ha actualizado el usuario: {name} ahora es : {new_name} \nque ha prestado el libro: {book}')
        else:
            print('ese usuario no existe')
            input(' ')
    except:
        input('no se puede realizar esta accion')

        