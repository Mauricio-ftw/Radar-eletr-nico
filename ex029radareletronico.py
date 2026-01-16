velocidade=int(input('Qual a velocidade do carro?: '))
multa=float((velocidade-80)*7)
if velocidade <81:
    print('Muito bem, você está dentro do limite')
else:
    print('Você foi multado, excedeu o limite permitido de 80km/h')
    print(f'Tera de paga uma multa de R${multa:.2f}')