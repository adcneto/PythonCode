Lista_Numeros=[]
num=1


while num!=0:
    num= int(input("Digite um nº terminado em zero, ou zero para acabar a execução: "))
    if num!=0:
        Lista_Numeros.append(num)



comprimento = len(Lista_Numeros)

i=0

while i<comprimento:
    print(Lista_Numeros[comprimento - 1 -i], end=" ")
    i+=1
