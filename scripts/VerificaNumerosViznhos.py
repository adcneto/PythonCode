#Este programa verifica se há em um número (representado em base 10) dois dígitos adjacentes iguais
PrimeiroDigitoZero = True
while PrimeiroDigitoZero:
    num = input("Entre com um número inteiro que não comece com '0': ")
    if int(num)/(10**(len(num)-1)) < 1:
        PrimeiroDigitoZero = True
    else:
        PrimeiroDigitoZero = False
ExpoentePotenciaDez=1
SemVizinhosIguais = True
antecessor = 123456
temp=0
while ExpoentePotenciaDez <= len(num) and SemVizinhosIguais:
    ValorCasaDecimal = ((int(num)%(10**ExpoentePotenciaDez))-temp)/(10**(ExpoentePotenciaDez-1))
    print(int(ValorCasaDecimal))
    temp = int(num)%(10**ExpoentePotenciaDez)
    ExpoentePotenciaDez += 1
    if antecessor != ValorCasaDecimal:
        antecessor = ValorCasaDecimal
    else:
        SemVizinhosIguais = False
        print("Há números vizinhos iguais!")
if SemVizinhosIguais:
    print("O número que vc teclou não possui dígitos adjacentes iguais!")
