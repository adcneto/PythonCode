a = int(input("digite um numero: "))
lista=[]
while a != 0:
    lista.append(a)
    a = int(input("digite um numero: "))
    
lista_impressa = []
for i in range((len(lista))-1,-1,-1):
    lista_impressa.append(lista[i])

print(lista_impressa)
    
    
