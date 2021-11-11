while True:
    email = input("Cual es tu correo electronico?: ").strip()
    if "@" not in email or email== "":
        print("Use un email valido")
    else:
        break

slicer = email.split("@")

print(f"Tu nombre de usario es: {slicer[0]}")
print(f"Tu dominio es: {slicer[1]}")
