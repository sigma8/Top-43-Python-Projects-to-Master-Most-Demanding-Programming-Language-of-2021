from notifypy import Notify
import requests
from bs4 import BeautifulSoup


#requets a la pagina de github para obtener los datos de los repositorios
r = requests.get('https://github.com/sigma8?tab=repositories').text
soup = BeautifulSoup(r, 'lxml')

#con esta funcion obtengo el primer repositorio
def repositorio(bsdatos): # type bsdatos: class 'bs4.element.Tag'
    titulo = bsdatos.h3.a.text.strip()
    descripcion = bsdatos.p.text.strip()
    fecha = bsdatos.find('relative-time').text.strip()
    datos = [titulo, descripcion, fecha]
    return datos # type datos: list[str]
#con esta funcion obtengo todos los repositorios
def repositorios_total():
    informacion =[]
    for elemento in soup.find_all('li', class_="public"):
        resultado = repositorio(elemento)
        informacion.append(resultado)
    return informacion # type informacion: list[list[str]]

#variable para almacenar la lista de los repositorios
repo = repositorios_total()
#aqui determino cuantos repositorios existen
total_repos = len(repo)

#crear y enviar la notificacion
notificacion = Notify()
notificacion.tittle = "Repositorios github"
notificacion.message = f"Los repositorios son {total_repos}, y  el ultimo repositorio actualizado es: {repo[0][0]}, fecha: {repo[0][2]}"

notificacion.send(block=False)



