cordenadax = float (input('escolha a cordenada x:'))
cordenaday = float (input('escolha a cordenada y:'))

if (cordenadax > 0) and (cordenaday > 0):
    print('primeiro quadrante')
elif (cordenadax < 0) and (cordenaday > 0):
    print('segundo quadrante')
elif (cordenadax < 0) and (cordenaday < 0):
    print ('terceiro quadrante')
elif (cordenadax > 0) and (cordenaday < 0):
    print ('quarto quadrante')
else:
    print('o ponto esta no eixo de origem')