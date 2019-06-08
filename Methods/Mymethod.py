import random

rest = ['letreros','eneldo', 'mesitas casa', 'delis', 'trucha']
ruleta = random.randrange(len(rest))
# aca habia metido el intervalo (1,6), pero los indices de una lista comienzan desde cero, entocnes el intervalo correcto era (0,5). Al meter este len quedo mas dinamica porque puedo aumentar la lista
# sde restaurantes sin problema

print(ruleta)
print(type(ruleta))


def ruletarest():
    print(rest[ruleta])

ruletarest()
