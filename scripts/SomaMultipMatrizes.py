import Matrizes
def SomaMatriz (A, B):
    num_linhas = len(A)
    num_colunas = len(A[0])
    C = Matrizes.cria_matriz (num_linhas, num_colunas, 0)
    for i in range(num_linhas):
        for j in range(num_colunas):
            C[i][j] = A[i][j] + B[i][j]
    return C

#Multiplicação de uma matriz A(m x p) por uma B(p x n)
def MultiplicaMatriz(A, B):
    linhas_final = len(A) # nº de linhas de A e de C
    colunas_final = len(B[0]) # nº de colunas de B e de C
    assert len(A[0]) == len(B)
    condicao_multiplicação= len(B) # nº de colunas de A e de linhas de B
    C = Matrizes.cria_matriz (linhas_final, colunas_final, 0)
    for m in range (linhas_final):
        for n in range(colunas_final):
            for p in range (condicao_multiplicação):
                C[m][n] += A[m][p] * B[p][n] 
    return C

if __name__ == '__main__':
    A = [[1,2,3], [4,5,6]]
    B = [[1,2], [3,4], [5,6]]
    print(Matrizes.imprime_matriz(MultiplicaMatriz(A,B)))
