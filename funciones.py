import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta funciÃ³n devuelve la lista de palabras que empiezan por una letra que alfabÃ©ticamente estÃ¡ antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    """ 
    PARA SOLUCIONAR EL ERROR EN EL TEST HE DECLARADO EL ARRAY RESULTADO AL PRINCIPIO DE LA FUNCIÓN PARA QUE NO SE INICIALICE VAÍO CADA VEZ
    QUE ENCUENTRE UNA PALABRA
    """
    resultado=[]
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                resultado.append(palabra)
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta funciÃ³n inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """

    """ 
    PARA SOLUCIONAR EL ERROR EN EL TEST HE CREADO EL OBJETO CLIENTE APARTE Y LO HE AÑADIDO AL DICCIONARIO USANDO LA FUNCIÓN UPDATE
    """
    cliente = {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        }
    clients_list.update({nif: cliente})
        

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un nÃºmero de repeticiones, esta funciÃ³n selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales
        cartas_repe=[]
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            cartas_repe.append(carta)
            cartas_aleatorias.remove(carta)
        
        combinaciones.update({"repeticion"+str(i): cartas_repe})

    print(combinaciones)
    return combinaciones

    