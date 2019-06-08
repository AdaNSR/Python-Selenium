"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""



ahorro = 700000
meses =  1
while ahorro < 10000000:
    print("El ahorro acumumulado es: " + str(ahorro), "y van" + " " + str(meses) + " " + "meses")
    meses = meses + 1
    ahorro = 700000 *meses


    if meses == 12:
        print("Hay que sacar dos semanas de vacaciones no pagas")
        continue