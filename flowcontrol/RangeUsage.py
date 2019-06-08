



import random


duracionContrato = random.randrange(1,25)
print(duracionContrato)
print(type(duracionContrato))

if duracionContrato != 12:
    ahorro = 700000 * duracionContrato
    print(ahorro)

else:
    ahorro = 700000 * duracionContrato - 350000
    print(ahorro)
