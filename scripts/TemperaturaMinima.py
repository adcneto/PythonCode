# Queremos encontrar a menor temperatura de uma lista


def minima (temps):
    menor = temps[0]
    i=1
    while i<len(temps):
        if temps[i] < menor:
            menor=temps[i]
        i+=1
    return menor

def teste_pontual(temps,valor_esperado):
    valor_calculado= minima(temps)
    if valor_calculado!=valor_esperado:
        print("Valor errado para array ", temps)
        print("Valor esperado: ", valor_esperado, "valor calculado: ", valor_calculado)

def testa_minima():
    print("Iniciando os testes")
    teste_pontual([0], 0)
    teste_pontual([0,0,0,0,0,0], 0)
    teste_pontual([0,1,2,3,4,5,6,7,8,9,10], 0)
    teste_pontual([30, 27, 38, 12, 29, 45, 25, 19], 12)
    teste_pontual([-15,-12,0,20,30], -15)
    print("Finalizando os testes. ")
