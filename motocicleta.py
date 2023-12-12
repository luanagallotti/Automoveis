from automoveis import Autonomies


class Motocicletas(Autonomies):
    def Empinar(self):
        print('Empinando!!')


CG160 = Motocicletas('Azul', 'Honda', 2020, 120, 'CG', False)
print('cambio auto? ', CG160.cambioAuto)
print('Ligado? ',CG160.ligado)
CG160.ligar()
print('Ligado? ',CG160.ligado)
CG160.acelerar()
print('velocidade = ',CG160.velo())
print('marcha = ',CG160.mostrarMarcha())
CG160.acelerar()
CG160.acelerar()
CG160.acelerar()
CG160.acelerar()
CG160.acelerar()
print('marcha = ',CG160.mostrarMarcha())

