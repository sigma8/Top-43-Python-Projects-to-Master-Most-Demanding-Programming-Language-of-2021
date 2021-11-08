import time

print("Bienvenidos a este mad libs, la historia a continuacion sera creada por usted o ustedes, la trama es sobre los viajes de placer")
time.sleep(2)
adjetivo = []
sustantivo = []
sustantivo_plural = []
verbo = []
numero = 0
print("A continuacion se le o les pediran una cantidad de palabras(Vervos, sutantivos, adjetivos) que ayudaran a crear esta historia")
time.sleep(2)
print("A jugar!!!")
time.sleep(2)

print("Empecemos con los adjetivos")
time.sleep(1)
for i in range(3):
    adj = input(f"Ingresa el adjetivo numero {i + 1}: ")
    adjetivo.append(adj)
time.sleep(1)
print("Ahora sustantivos en singular")
for i in range(7):
    sus = input(f"Ingresa el sustantivo numero {i + 1}: ")
    sustantivo.append(sus)
time.sleep(1)
print("Que tal unos sustantivos en plural")
for i in range(4):
    susp = input(f"Ingresa el sustantivo plural numero {i + 1}: ")
    sustantivo_plural.append(susp)
time.sleep(1)
print("Unos cuantos verbos infinitivos")
for i in range(4):
    verb = input(f"Ingresa el vervo infinitivo numero {i + 1}: ")
    verbo.append(verb)
time.sleep(1)
print("Terminemos con un numero")
while True:
    try:
        numero = int(input("Ingresa un numero: "))
        break
    except ValueError:
        print("Debes ingresar un numero")
time.sleep(1)
print("Veamos que creaste o crearon: ")
time.sleep(2)
historia = f"""Las vacaciones son cuando viajas a algun {adjetivo[0]}
con tu {adjetivo[1]}(a) familia. Usualmente vas a algún lugar
que está cerca de un/una {sustantivo[0]} o arriba de un/una {sustantivo[1]}.
Un buen lugar de vacaciones es aquel en el que puedes montar {sustantivo_plural[0]}
jugar {sustantivo[2]} o ir a buscar {sustantivo_plural[1]}.
Me gusta dedicar mi tiempo {verbo[0]} o {verbo[1]}.
Cuando los padres se van de vacaciones, pasan su tiempo comiendo
tres {sustantivo_plural[2]} al día, los padres juegan al golf y las madres
sentarse alrededor {verbo[2]}. El verano pasado, mi hermanito
cayó en un/una {sustantivo[3]} y recibió veneno en su {sustantivo[4]} 
sobre su {sustantivo[5]}. Mi familia irá al {sustantivo[6]} y yo practicaré {verbo[3]}.
Padres necesitan vacaciones más que los niños porque los padres
siempre son muy {adjetivo[2]} y porque tienen que trabajar {numero}
horas todos los días durante todo el año ganando suficiente {sustantivo_plural[3]}
para pagar para las vacaciones"""

print(historia)
