num = input("Entre com um número inteiro: ")
comprimento = len(num)
ExpoentePotenciaDez=1
temp=0
SomaDosDigitos=0
while ExpoentePotenciaDez <= comprimento:
    ValorCasaDecimal = ((int(num)%(10**ExpoentePotenciaDez))-temp)/(10**(ExpoentePotenciaDez-1))
    print(int(ValorCasaDecimal))
    temp = int(num)%(10**ExpoentePotenciaDez)
    ExpoentePotenciaDez += 1
    SomaDosDigitos = SomaDosDigitos + ValorCasaDecimal
print(SomaDosDigitos)
