import requests
from bs4 import BeautifulSoup
import urllib.request
def run():
    for i in range(1, 6):#Iteracion para la pagina web
        response = requests.get(f'https://xkcd.com/{i}')#Obtener informacion de la pagina 1 a 5
        soup = BeautifulSoup(response.content, 'html.parser') #Parsear el documento
        image_container = soup.find(id = 'comic')
        image_url = image_container.find('img')['src']#Acceder a la imagen mediante a su etiqueta y atributo src
        image_name = image_url.split('/')[-1]#Obtener el nombre del ultimo elemento despues del /
        print(f'Descargando la imagen {image_name}')
        urllib.request.urlretrieve(f'https:{image_url}', image_name)#Guardar la imagen
if __name__ == '__main__':
    run()