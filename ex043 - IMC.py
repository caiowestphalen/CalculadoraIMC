# programa que calcula o IMC

peso = float(input('Qual é seu peso: (Kg) '))
altura = float(input('Qual é sua altura: (m) '))
imc = peso / (altura ** 2)
print('O IMC desta pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS! Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('ATENÇÃO! Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('CUIDADO! Você está com obesidade.')
else:
    print('CUIDADO! Você está com obesidade mórbida.')

