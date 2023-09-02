def choose_level(n_pregunta, p_level):
    # Construir lógica para escoger el nivel
    ##################################################
    if n_pregunta <= p_level:
        level = 'basicas'
    
    elif n_pregunta <= p_level*2:
        level = 'intermedias'
    
    else:
        level = 'avanzadas'

    return level    
    ##################################################
    
   

if __name__ == '__main__':
    # verificar resultados
    print('2 , 2 se espera básicas, se obtiene => ' + choose_level(2, 2)) # básicas
    print('3 , 2 se espera intermedias, se obtiene => ' + choose_level(3, 2)) # intermedias
    print('7 , 3 se espera avanzadas, se obtiene => ' + choose_level(7, 3)) # avanzadas
    print('4 , 3 se espera intermedias, se obtiene => ' + choose_level(4, 3)) # intermedias