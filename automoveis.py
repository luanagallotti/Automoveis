class Autonomies:
    global ACELERACAO
    ACELERACAO = 10
       
    def __init__(self, cores, fabricante, data, max, mod, cambio = True ):      
    
        self.cor = cores        
        self.marca = fabricante
        self.modelo = mod
        self.ano = data
        self.veloMax = max
        self.ligado =  False
        self.cambioAuto = cambio
        self.__velo = 0 
       
    def velo(self):
        return self.__velo
   
    def setVelo(self, valor):
        if self.veloMax >= valor:
            self.__velo = valor
            return True




    def ligar(self):
        if self.ligado and self.__velo == 0:
            self.ligado = False 
            return True
        elif not self.ligado:
            self.ligado = True
            return False


    def mostrarMarcha(self):
        if self.__velo <= 40:
            return '1ª marcha'
        elif self.__velo <= 65:
            return '2ª marcha'
        elif self.__velo <= 75:
            return '3ª marcha'
        else:
            return '4ª marcha'


    def acelerar(self):        
        if (self.veloMax) >= (self.__velo + ACELERACAO): 
            self.__velo = self.__velo + ACELERACAO            
        else:
            self.__velo = self.veloMax
       
        if self.cambioAuto:


            return str(Autonomies.mostrarMarcha(self))
             




    def frear(self):
        if (self.__velo - ACELERACAO) >= 0:
            self.__velo -= ACELERACAO
        else:
            self.__velo = 0


   
       






