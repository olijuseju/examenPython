import random
def choose_secret():
    """Dado un nombre de fichero, esta funciÃ³n devuelve una palabra aleatoria de este fichero transformada a mayÃºsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayÃºsculas. Ej. "CREMA"
    """

    f = open("palabras_reduced.txt", mode="rt", encoding="utf-8")

    listaPalabras = []
    
    for linea in f:
      listaPalabras.append(f.readline())
    f.close()

    num = random.randint(0, len(listaPalabras) - 1)

    return listaPalabras[num]
    
    


    
def compare_words(word, secret):
    """Dadas dos palabras en mayÃºsculas (word y secret), esta funciÃ³n calcula las posiciones de las letras de word que aparecen en la misma posiciÃ³n en secret, y las posiciones de las letras de word que aparecen en secret pero en una posiciÃ³n distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posiciÃ³n en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras estÃ¡n en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    word2 = word.upper()
    secret2 = secret.upper()
    same_position=[]
    same_letter=[]
    for plword in range(len(word2)):
      for plsecret in range(len(secret2)):
        if(word2[plword] == secret2[plsecret]):
          if(plword==plsecret):
            same_position.append(plword)
          else:
            same_letter.append(plword)

    return same_position, same_letter
          


def print_word(word, same_letter_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta funciÃ³n crearÃ¡ un string donde aparezcan en mayÃºsculas las letras de la palabra que ocupen las posiciones de same_position, en minÃºsculas las letras de la palabra que ocupen las posiciones de same_letter y un guiÃ³n (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    word2 = word.upper()
    deng = ["-","-","-","-","-"]
    for i in same_letter_position:
      deng[i] = word2[i]
    for i in same_letter:
      minus = word2[i].lower()
      deng[i] = minus
    
    transformed = ""

    for i in deng:
      transformed += i

    return transformed
    
def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta funciÃ³n filtra solo las palabras de 5 letras que no tienen acentos (Ã¡,Ã©,Ã­,Ã³,Ãº). De estas palabras, la funciÃ³n devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayÃºsculas
    """

    f = open(filename, mode="rt", encoding="utf-8")

    listaPalabras = []
    
    for linea in f:
      fi = f.readline()
      listaPalabras.append(fi[0:5])
    f.close()
    
    selected =[]
    for palabra in listaPalabras:
      if len(palabra) == 5:
        repetida=False
        for seleccionada in selected:
            if palabra == seleccionada:
              repetida = True
                    
        if(repetida == False):
          selected.append(palabra)

    num = random.randint(0, len(selected))

    return selected,selected[num]



 
def check_valid_word(selected):
    """Dada una lista de palabras, esta funciÃ³n pregunta al usuario que introduzca una palabra hasta que introduzca una que estÃ© en la lista. Esta palabra es la que devolverÃ¡ la funciÃ³n.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que estÃ¡ en la lista.
    """
    estaDentro=False
    while (estaDentro==False):
      word = input("Introduce una nueva palabra: ")
      for palabra in selected:
        if(word==palabra):
          estaDentro=True

    return word





if __name__ == "__main__":
    selected,secret=choose_secret_advanced("palabras_extended.txt")
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = check_valid_word(selected)
        same_position, same_letter = compare_words(word,secret)
        resultado=print_word(word,same_position,same_letter)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   