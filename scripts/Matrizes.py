"""(int, int, valor) -> matriz(lista de listas)
Cria e retorna uma matriz 'com num_linhas' linhas
e 'num_colunas' colunas, em que cada elemento é igual
ao valor dado
"""

def cria_matriz(num_linhas, num_colunas, valor):
    matriz=[] # lista vazia
    for i in range(num_linhas):
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha) #adiciona linha à matriz
    return matriz

def imprime_matriz(matriz):
    for i in range(0, (len(matriz))):
        print(matriz[i])

"""Cria e retorna uma matriz 'com num_linhas' linhas
e 'num_colunas' colunas, em que cada elemento é igual
ao input do usuário
"""
def cria_matriz_manual(num_linhas, num_colunas):
    matriz=[] # lista vazia
    for i in range(num_linhas):
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append(int(input("Tecle um valor para o elemento %dx%d da matriz:" %(i+1,j+1))))
        matriz.append(linha) #adiciona linha à matriz
    return matriz

if __name__ == "__main__":
    print (__name__)
