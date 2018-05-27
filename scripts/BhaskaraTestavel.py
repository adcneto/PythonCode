# Bhaskara testvel e orientado a objetos

import math
          
class Bhaskara:
# Não foi necessario utlizar o metodo construtor __init__

    def main(self):
        Adigitado = float(input("Digite o valor do numero a: "))
        Bdigitado = float(input("Digite o valor de b: "))
        Cdigitado = float(input("Digite o valor de c: "))
        print(self.CalculaRaizes2Grau(Adigitado, Bdigitado, Cdigitado))

    def delta (self, a, b, c):
        return (b**2) - 4*a*c
        
    def CalculaRaizes2Grau (self, a,b,c):
        d = self.delta(a,b,c)
        if d >= 0 and a!=0:
            raiz_1 = ((-1*b) + math.sqrt(d))/(2*a)
            if d == 0:
                return 1, raiz_1
            else:
                raiz_2 = ((-1*b) - math.sqrt(d))/(2*a)
                return 2, raiz_1, raiz_2
        else:
            return 0

if __name__ == '__main__':
    Minha_Equacao = Bhaskara()
    Minha_Equacao.main()
