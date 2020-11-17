def binary_search(numbers, number_to_find, low, high):
    if low > high: #Caso donde aplicamos la comparacion del indice bajo al indice alto y ya paso todos los indices es decir no lo encontro
        return False
    mid = (low + high) / 2
    if numbers[mid] == number_to_find: #Caso donde comparamos el numero de la mitad con el numero a buscar
        return True
    elif numbers[mid] > number_to_find:#Caso en el que el numero del medio sea mas grande que el numero, que deseamos buscar ya el final no sera el ultimo numero por ente el final cambiaria a mid -1
        return binary_search(numbers, number_to_find, low , mid -1)
    else: #Caso de que el numero de la mitad sea menor al numero buscado
        return binary_search(numbers, number_to_find, mid + 1, high)
if __name__ == '__main__':
    numbers = [1, 3 ,4 ,5 ,6 ,9, 10, 11, 25, 28, 34, 36, 49, 51]
    number_to_find = int(input("Ingresa un numero: "))
    result = binary_search(numbers, number_to_find, 0, len(numbers) -1)
    if result is True:
        print("El numero si esta en la lista")
    else:
        print("El numero no esta en la lista")
