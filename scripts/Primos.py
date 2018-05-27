def DecomposicaoPrimos():
    n = int(input("Digite um número inteiro >1: "))
    fator=2
    print("n = ", end="")
    while n>1 :
        multiplicidade=0
        while n%fator == 0:
            n=n/fator
            multiplicidade+=1
        if multiplicidade>0:
            if n>=2:
                print("%d^%d * " %(fator,multiplicidade), end="")
            else:
                print("%d^%d" %(fator,multiplicidade))
        fator+=1
        
def TestePrimalidade (n):
    if n<0:
        return "O conceito de primalidade ñ se aplica a n<0"
    elif n==0:
        return False
    else:
        fator =2
        while fator<n:
            teste=n%fator
            if teste==0:
                return False
            else:
                fator+=1
        if fator>=n:
            return True



