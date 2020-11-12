import random
IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
    'computadora',
    'teclado',
    'mouse',
    'lavadora',
    'secadora',
    'cama',
    'almohada',
    'platzi'
]
def random_word():
    idx = random.randint(0, len(WORDS) -1)#Ingresar a una palabra aleatoriamente
    return WORDS[idx]#Retorna el valor de la palabra
def display_board(hidden_word, lives):
    print(IMAGES[lives])#Indice de imagenes
    print('')
    print(hidden_word)
    print(' ---- * ---- * ---- * ---- * ---- * ---- *')
def run():
    word = random_word()
    hidden_word = ['-'] * len(word)#Espacios en blancos para las palabras
    lives = 0 #Intentos o vidas del juego
    while True:
        display_board(hidden_word, lives)
        current_letter = str(input("Escribe una letra: "))#Letras que se comparara con la palabra oculta
        letter_index = []#Guardara los indices de las palabras ingresadas para comprarlo con la palabra oculta
        for i in range(len(word)):
          if word[i] == current_letter:
            letter_index.append(i)#Ingresar la letra mediante al indice en caso de que hagan match
        if len(letter_index) == 0:#Si no existe ninguna letra pierdes 1 vida
          lives +=1
          if lives == 7:#Caso de perdida
            display_board(hidden_word, lives)
            print("")
            print(f"Lo siento haz llegado al maximo de todos los intentos, la palabra correcta era ({word})")
            break
        else:
          for i in letter_index:
            hidden_word[i] = current_letter#Cambiar la letra al espacio en blanco del interfaz de letras
          letter_index = []#Vaciar el valor de las letras para empezar de nuevo la iteracion
        try:
          hidden_word.index('-')#Busca si hay un espacio en blanco
        except ValueError:
            print("")
            print(f"Felicidades ganaste!, la palabra era, ({word})")
            break
if __name__ == '__main__':
    print("🐱‍👓 Bienvenidos al juego del ahorcado 🐱‍🏍")
    run()