def fatorial(n):
    produto=1
    if n==0:
        return produto
    elif n<0:
        return "O fatorial não se aplica a numeros negativos"
    else:
        for i in range(1, n+1):
            produto= produto*i
    return produto

def NumBinom (n,k):
    combinacoes = fatorial(n)/(fatorial(k)*fatorial(n-k))
    return combinacoes

def TriangPas (a):
    temp=0
    while temp<=a :
        for i in range (0, temp+1):
            y=int(NumBinom (temp,i))
            print(y, end="\t")
        print()
        temp+=1
