# Apresentação do programa
print('=' * 62)
print('VALOR DA HORA'.center(62))
print('=' * 62)

# Entrada dos valores informados pelo usuario 
salario_input = input('Informe o salario: R$')

# Substituinfo a , por .

salario_input = salario_input.replace(',', '.')

# Transformando a str em float

salario = float(salario_input)


print('-' * 62)
horas_mensais = float(input('Quantia de horas mensais: '))

print('-' * 62)
dias_trabalhados = int(input('Quantos dias trabalhados no mês: '))

# Calculo para descobrir quantas horas ele trabalha por dia 
horas_por_dia = (horas_mensais / dias_trabalhados)

# Calculo para descobrir o valor diario com base no salario e nos dias trabalhaos por mes 
valor_dia = (salario / dias_trabalhados)

# Calculo para descobrir o valor da hora com base no seu valor diario e horas trabalhadas por dia 
salario_Hora = (valor_dia / horas_por_dia)

# Mostra o resultado dos calculos com o valor correto da hora do funcionario
print('¬' * 62)
print(f'O valor da hora é de R${salario_Hora:.2f}')
print('¬' * 62)
