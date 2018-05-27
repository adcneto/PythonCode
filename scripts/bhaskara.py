import math
def delta (a, b, c):
    return (b**2) - 4*a*c

def main():
    a_digitado = float(input("Digite o valor de a: "))
    b_digitado = float(input("Digite o valor de b: "))
    c_digitado = float(input("Digite o valor de c: "))
    ImprimeRaizes2Grau (a_digitado,b_digitado,c_digitado)
    
     
def ImprimeRaizes2Grau (a,b,c):
    d = delta(a,b,c)
    if d >= 0 and a!=0:
        raiz_1 = ((-1*b) + math.sqrt(d))/(2*a)
        if d == 0:
            print("A única raiz é %f" %raiz_1)
        else:
            raiz_2 = ((-1*b) - math.sqrt(d))/(2*a)
            print("A primeira raiz é %f e a segunda raiz é %f" %(raiz_1, raiz_2))
    elif a==0:
        print("A coeficiente 'a' não pode ser nulo!")
    else:
        print("A equação não possui coeficientes reais")

if __name__ == '__main__':
    main()
