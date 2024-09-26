# Calculadora simples em python

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador. Está dispopnivel (+, -, * e /): ')

    numero_valido = None

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numero_valido = True
    except:
        numero_valido = None

    if numero_valido is None:
        print('Número(s) estão invalidos')
        continue

    operador_valido = '+-*/'

    if operador not in operador_valido:
        print('Digite um operador válido')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 operador')
        continue

    if operador == '+':
        soma = num_1_float + num_2_float
        print(f'O valor da soma é {soma}')
    if operador == '-':
        subtracao = num_1_float - num_2_float
        print(f'O valor da subtração é {subtracao}')
    if operador == '*':
        multiplicacao = num_1_float * num_2_float
        print(f'O valor da multiplicação é {multiplicacao}')
    if operador == '/':
        divisao = num_1_float * num_2_float
        print(f'O valor da divisão é {divisao}')

    sair = input('Deseja sair? [S]im: ').lower().startswith('s')
    if sair:
        break