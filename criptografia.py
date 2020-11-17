KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}
def cypher(message):
    words = message.split(" ") # Dividir palabras con un espacio
    cypher_message = []
    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]
        cypher_message.append(cypher_word)
        return ''.join(cypher_message) #Agregar espacios a las palabras
def decypher(message):
    words = message.split(' ')
    decypher_message = []
    for word in words:
        decypher_word = ''
        for letter in word:
            for key, value in KEYS.items():
                if value == letter:
                    decypher_word += key
        decypher_message.append(decypher_word)
    return ' '.join(decypher_message)
def run():
    while True:
        menu = str(input('''--- * --- * --- * --- * --- * --- * --- * ---
            Bienvenido a criptografía. ¿Qué deseas hacer?
            1.- Cifrar mensaje
            2.- Decifrar mensaje
            3.- Salir
        '''))
        if menu == '1':
            mensaje = str(input("Escribe un mensaje: "))
            cypher_message = cypher(mensaje)
            print(cypher_message)
        elif menu == '2':
            mensaje = str(input("Escribe tu mensaje cifrado: "))
            decypher_message = decypher(mensaje)
            print(decypher_message)
        elif menu == '3':
            print('Salir')
            return False
        else:
            print('¡Comando no encontrado!')
if __name__ == '__main__':
    run()