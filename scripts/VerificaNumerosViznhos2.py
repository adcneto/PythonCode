#Outro jeito de verificar se há em um número (representado em base 10) dois dígitos adjacentes iguais
PrimeiroDigitoZero = True
while PrimeiroDigitoZero:
    num = input("Entre com um número inteiro que não comece com '0': ")
    if int(num)/(10**(len(num)-1)) < 1:
        PrimeiroDigitoZero = True
    else:
        PrimeiroDigitoZero = False
ExpoentePotenciaDez = len(num) - 1
SemVizinhosIguais = True
antecessor = 0
temp=int(num)
while ExpoentePotenciaDez >=0 and SemVizinhosIguais:
    ValorCasaDecimal = temp//(10**ExpoentePotenciaDez)
    print(ValorCasaDecimal)
    temp = temp - ValorCasaDecimal*(10**ExpoentePotenciaDez)
    ExpoentePotenciaDez -= 1
    if antecessor != ValorCasaDecimal:
        antecessor = ValorCasaDecimal
    else:
        SemVizinhosIguais = False
        print("Há números vizinhos iguais!")
if SemVizinhosIguais:
    print("O número que vc teclou não possui dígitos adjacentes iguais!")
