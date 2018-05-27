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
        
limite=int(input("Digite limite para impressão dos primos: "))

i=1
lista_primos=[]
while i<=limite:
    if TestePrimalidade (i):
        print(i, end=", ")
        lista_primos.append(i) #guarda os primos desejados numa array
    i+=1
    
    
