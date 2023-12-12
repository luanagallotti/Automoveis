from automoveis import Autonomies



chevette = Autonomies('prata', 'GM', 1978, 84, 'hatch')


print('cambio auto? ',chevette.cambioAuto)


print('Ligado? ',chevette.ligado)
chevette.ligar()
print('ligado? ',chevette.ligado)


for acel in range(10):
    chevette.acelerar()
    print('Marcha atual: ',chevette.acelerar())
    print('velocidade = ',chevette.velo)
    input('qq tecla p continuar...')


chevette.ligar()    
print('Ligado? ',chevette.ligado)


for freiar in range(10):
    chevette.frear()
    print('velocidade atual = ',chevette.velo)
    input('qq tecla p continuar...')




chevette.ligar()    
print('Ligado? ',chevette.ligado)




