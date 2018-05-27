import BhaskaraTestavel
import pytest
class TestBhaskara:
    @pytest.fixture # indicamos que vamos definir uma fixture
    def b(self):
        return BhaskaraTestavel.Bhaskara()
    @pytest.mark.parametrize("coefA,coefB,coefC,num_raizes, raiz1, raiz2", [
         (1,0,0,1,0,0),
         (1,-5,6,2,3,2),
         (10,20,10,1,-1,-1),
         (10,10,10,0,0,0),
         (10,20,10, 1,-1, -1),
         (0,1,2,0,0,0)
        ])
    def testa_uma_raiz(self, b, coefA,coefB,coefC,num_raizes, raiz1, raiz2):
        if raiz2 == raiz1 and num_raizes!=0 and coefA!=0:
            assert b.CalculaRaizes2Grau(coefA,coefB,coefC) == (num_raizes, raiz1)
        elif num_raizes!=0 and coefA!=0:
            assert b.CalculaRaizes2Grau(coefA,coefB,coefC) == (num_raizes, raiz1, raiz2)
        else:
            assert b.CalculaRaizes2Grau(coefA,coefB,coefC) == num_raizes
