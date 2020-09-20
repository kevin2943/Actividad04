def getSigno(mes, dia):
    if(mes>12 or mes<1):
        raise Exception("Mes fuera del rango")
    if(dia>31 or dia<1):
        raise Exception("Dia fuera del rango")

    signos = ["Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo",
              "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"]
    if(mes == 1):
        return signos[9 + dia//21]
    if(mes == 2):
        return signos[10 + dia//19]
    if(mes <= 5):
        return signos[mes-4 + dia//21]
    if(mes == 6):
        return signos[2 + dia//22]
    if(mes <= 11):
        return signos[mes-4 + dia//23]
    return signos[8 + dia//22]

mes = int(input("Ingrese su mes de nacimiento: "))
dia = int(input("Ingrese su dia de nacimiento: "))
print("Su signo es: {}".format(getSigno(mes,dia)))
