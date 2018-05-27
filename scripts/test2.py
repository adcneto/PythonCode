#content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def calc_imc(altura, peso):
    assert altura>0 and peso>0
    imc= (peso/(altura**2))
    return imc
import TrianguloPascal
