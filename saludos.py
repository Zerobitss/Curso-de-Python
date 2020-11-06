# name = input("Cual es tu nombre: ")
# print("Bienvenido: "+ name+ "!")
import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave)

    turtle.mainloop()

def make_square(dave):
    length = int(input('Tamaño de cuadrado: '))

    for i in range(4):
        make_line_and_turn(dave, length)

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)

if __name__ == '__main__':
    main()