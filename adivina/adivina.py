import random
import time

p = 0
chance = 0


print('BIENVENIDO AL JUEGO: ADIVINAR EL NUMERO!!!')
time.sleep(2)
print("Las reglas son muy sencillas")
time.sleep(2)
print("1. El numero a elegir debe estar entre el numero 1 y el numero 99 incluyendo a ambos")
time.sleep(1)
print("2. Tienes tres oportunidades para adivinar el numero")
time.sleep(1)
print("3. Si el numero que eliges es incorrecto perderas 10 puntos, y si aciertas ganaras 10 puntos")
time.sleep(1)
print("4. Los puntos son acumulados hasta que decidas terminar de jugar.")
time.sleep(3)
print("A jugar!!!")

def primo(n):
    x = "es un numero primo"
    for i in range(2, n):
        if n%i==0:
            x = "no es un numero primo"
            break
    return x

def par_impar(n):
    if n%2==0:
        x = "es un numero par"
    else:
        x = "no es un numero par"
    return x

def mayor_que(n):
    if n > 70:
        x = "el numero es mayor a 70"
    elif n > 50:
        x = "el numero es mayor a 50"
    elif n > 30:
        x = "el numero e mayor a 30"    
    elif n >= 10:
        x = "el numero es de dos digitos"
    else:
        x = "el numero es de un solo digito"
    return x

def pistas(n, i):
    if i == 0:
        pista_uno = par_impar(n)
        ayuda = f"Aqui va la ayuda numero {i+1}: {pista_uno}"
    elif i == 1:
        pista_dos = primo(n)
        ayuda = f"Aqui va la ayuda numero {i+1}: {pista_dos}"
    else:
        pista_tres = mayor_que(n)
        ayuda = f"Aqui va la ayuda numero {i+1}: {pista_tres}"
    return ayuda


while True:
    num_maquina = random.randint(1, 99)
    while chance < 3:
        print(pistas(num_maquina, chance))
        time.sleep(1)
        adivinar = int(input("Intenta adivinar, di un numero: "))
        
        if num_maquina != adivinar:
            chance += 1
            p = p - 10
            print(f"no acertaste, tu puntuacion es: {p}")
        else:
            p = p + 10
            print(f"acertaste, tu puntuacion es: {p}")
            break
    print(f"el numero era: {num_maquina}")
    time.sleep(2)
    seguir = input("Deseas seguir jugando si/no: ")
    if seguir == "no":
        print(f"Tu puntuacion final es: {p}")
        break
    else:
        chance = 0
