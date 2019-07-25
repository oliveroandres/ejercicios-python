edad = int(input(" Digite su edad " ))
genero = input(" Digite sexo, H para hombre, M para mujer " )
if edad>=18:
    if genero=='H':
        print("Señor usted es mayor de edad " )
    else:
        print("Usted es mayor de edad " )
else:
    if genero=='M':
        print("Señora usted es menor de edad " )
    else:
        print("Señor, usted es menor de edad " )
    

