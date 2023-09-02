
def validate(opciones, eleccion):
    while eleccion not in opciones:
            eleccion = input(f'Opción no válida, ingrese una de las opciones válidas: {opciones}\n')

    return eleccion
    ##########################################################################
   


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    valid_option = validate(numeros, eleccion)
    print(f'TEST: Opción valida = {valid_option}')

    
    
