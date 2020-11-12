def palindrome1(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False
def palindrome(word):
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0, letter)
    reversed_word = ''.join(reversed_letters)#Palabra alrevez
    if reversed_word == word:
        return True
    else:
        return False
if __name__ == "__main__":
    word = str(input("Escribe una palabra: "))
    result = palindrome1(word)
    if result is True:
        print(f'La palabra {word}, es un palindromo')
    else:
        print(f'La palabra {word}, no es un palindromo')