import sys

argumentos = sys.argv # arg1 = metod // arg2 = n1 // arg3 = n2

print(argumentos)

def soma(nun1,nun2):
    res = nun1+nun2
    return res

def sub(nun1,nun2):
    res = nun1-nun2
    return res

if argumentos[1] == "soma":
    resp = soma(float(argumentos[2]),float(argumentos[3]) )
else:
    resp = sub(float(argumentos[2]),float(argumentos[3]) )

print(resp)