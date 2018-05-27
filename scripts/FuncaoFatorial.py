
def FatFatorial():
    ContinuaLoopExterno=True
    while ContinuaLoopExterno:
        n = int(input("Digite um número: "))
        ContinuaLoopInterno=True
        while ContinuaLoopInterno:
            produto=1
            if n==0:
                print(produto)
            elif n<0:
                print("""O fatorial não se aplica a numeros negativos. 
O programa acaba aqui!!!""")
                ContinuaLoopExterno=False
            else:
                for i in range(1, n+1):
                    produto= produto*i
                print(produto)
            ContinuaLoopInterno=False

#Jeito Mais Fácil:
def SlimFatorial(n):
    if n>=0:
        while n >= 0:
            produto = 1
            while n > 1:
                produto = produto * n
                n-=1
            return produto
    else:
        return 0



import pytest

@pytest.mark.parametrize("entrada, esperado",[ 
                            (0,1),
                            (1,1),
                            (-10,0),
                            (4,24),
                            (5,120)
                            ])

def testa_fatorial(entrada, esperado):
    assert SlimFatorial(entrada) == esperado
    


                                
