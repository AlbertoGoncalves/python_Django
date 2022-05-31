def soma(nun1,nun2):
    res = nun1+nun2
    return res

retorno = soma(1,40)

#print(retorno)
#print(soma(1,40))


def Ler_Numeros():
    x = input('Digite Nun 1')
    c = input('Digite Nun 2')
    print(soma(int(x),int(c)))
    return

#er_Numeros()



def tem_sete_itens(obj):
    if len(obj) == 7:
        return True
    else:
        return False


print(tem_sete_itens('1234567ww'))

print(tem_sete_itens(['1','2','1','2','1','2','1']))




