print('-------- CALCULADORA------------\n')
print('1 = soma, 2 = subtração, 3 = multiplicação, 4 = divisão \n')
opcao = int(input('Digite uma opcao 1 / 2 / 3 /4 : '))
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite seu segundo numero'))

if opcao == 1:
    soma = n1 + n2
    print(soma)
elif opcao == 2:
    subtra = n1 - n2
    print(subtra)
elif opcao == 3:
    mult = n1 * n2
    print(mult)
else:
    div = n1 // n2
    print(div)
