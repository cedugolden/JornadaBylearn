numero1 = 0
numero2 = 0
oper = ''  
resultado = 0

while True:
    numero1 = int(input('Digite um numero: '))
    print('Essas sao as operações: +, -, x, /.')
    oper = input('Digite a operacao: ')
    numero2 = int(input('Digite o outro numero: '))

    if oper == '+':
        resultado = numero1 + numero2
    elif oper == '-':
        resultado = numero1 - numero2
    elif oper == 'x':
        resultado = numero1 * numero2
    elif oper == '/':
        resultado = numero1 / numero2
    else:
        print('Operacao invalida. :( ')
    print(str(numero1) + '' + str(oper) + '' + str(numero2) + '=' + str(resultado))
