#Vamos a contar cuantas veces dentro del cuento se utiliza una palabra
def run():
    counter = 0
    with open("aleph.txt", "r", encoding="utf8") as f:
        for line in f:
            counter += line.count('Beatriz')
    print(f'Beatriz se encuentra {counter} en el texto')
if __name__ == '__main__':
    run()