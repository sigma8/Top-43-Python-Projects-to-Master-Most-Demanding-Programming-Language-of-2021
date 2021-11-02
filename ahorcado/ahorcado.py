import random


volver_jugar = True
while volver_jugar == True: # ciclo while para jugar nuevamente o no
    palabras = [ "mexico", "colombia", "canada", "venezuela", "uruguay", "argentina", "guatemala",
                 "panama", "ecuador", "ford", "audi", "nissan", "renault", "chevrolet", "mitsubishi", "cadillac", "suzuki"]
    palabra = random.choice(palabras)
    pista = list("-"*len(palabra)) # sustituyo la palabra con "-" para esconder la palabra y es lista para ser modificable
    print("")
    print("".join(pista))
    print("")

    count = 0
    letras_usadas = []
    while count < 5:
        letra = input("Dame una letra: ").lower()
        if letra.isalpha() == True and len(letra) == 1: # verifico que no sea un numero, simbolo o una elemento distinto a 1 sola letra
            if letra in letras_usadas:
                print("Ya usaste esa letra, intenta una diferente")
            elif palabra.find(letra)!= -1:
                for indice, caracter in enumerate(palabra):
                    if letra == caracter:
                        pista[indice] = letra
                if "".join(pista) == palabra:
                    print("Felicidades, GANASTE")
                    break
                else:
                    letras_usadas.append(letra)
                    print("Es correcto, sigamos\n")
                    print("".join(pista))
                    print("")
            else:
                letras_usadas.append(letra)
                count +=1
                if count == 5:
                    print(f"Lo siento, has perdido, la palabra correcta era: {palabra}")
                else:
                    print("incorrecto, intente nuevamente\n")
                    print("".join(pista))
                    print("")
        else:
            print("Introduzca una letra\n")

    print(f'Estas son las letras usadas: {" - ".join(letras_usadas)}')
    respuesta = True
    while respuesta == True: # ciclo while para asegurarse que la respuesta sea "yes" o "no", "y" o "n"
        jugar = input("Quieres volver a jugar: (y/n)").lower()
        if jugar.isalpha()== True:
            if jugar == "yes" or jugar == "y":
                print("Venga, juguemos de nuevo\n")
                respuesta = False
            elif jugar == "no" or jugar == "n":
                volver_jugar = False # hace que el ciclo while de volver a jugar no se vuleva a ejecutar, es decir, termine el juego
                print("Gracias por jugar")
                respuesta = False 
        else:
            print("introduzca una respuesta valida")
            
