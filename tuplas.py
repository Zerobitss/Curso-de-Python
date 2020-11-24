"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""
def first_not_repeating_char(char_sequence):
    seen_letters = {}#Diccionario
    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[1] + 1)
        """
        Todo esto lo que esta haciendo es:
        "abcabad"
        {
            'a': (0, 4)
            'b': (1, 2)
            'c': (3, 1)
        }
        El primero seria el indice de la letra
        El segundo seria cuantos veces lo hemos visto en la iteracion
        """
        final_letters = []
        for key, value in seen_letters.items():
            if value[1] == 1:
                final_letters.append((key, value[0]))
        """
        "abacabad"
        [('a', 0), ('d, 7)]
        """
        not_repeated_letters = sorted(final_letters, key = lambda value: value[1])
        if not_repeated_letters:
            return not_repeated_letters[0][0]
        else:
            return '_'
if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))
    result = first_not_repeating_char(char_sequence)
    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print(f'El primer caracter no repetido es: {result}')