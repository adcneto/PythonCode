#POO
#exemplo de objeto: carro

def main():
    carro1 = Carro('Brasilia', 1968, 'amarela', 80)
    carro2 = Carro('Fuscão', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano = a
        self.cor = c
        self.vel = 0
        self.maxV = vm # velocidade máxima

    def imprima(self):
        if self.vel == 0: # parado dá para ver o ano
            print("%s %s, ano %d" %(self.modelo, self.cor, self.ano))
        elif self.vel < self.maxV: #carro numa velocidade baixa(não dá pra ver o ano)
            print("%s %s indo a %d km/h" %(self.modelo, self.cor, self.vel))
        else: # carro muito rapido (não da pra saber velocidade nem ano)
            print("%s %s indo muito raaaaaapido!" %(self.modelo, self.cor))

    def acelere(self,velocidade): # muda a velocidade
        self.vel = velocidade
        if self.vel > self.maxV:
            self.vel = self.maxV
        self.imprima()

    def pare(self): # para o carro
        self.vel = 0
        self.imprima()
                        
main()
