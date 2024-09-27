print('Calculadora')

#Lista para salvar os resultados
results = []

# Setei uma variável com valor default 's' para iniciar.
iniciar = 's'

# Aqui dei início ao laço de repetição, onde enquanto a variável estiver
# com o valor de 's', o loop continuará.
while iniciar == 's':

  # Primeiro input pedindo para iniciar a calculadora, dando a opção de
  # encerrar a aplicação.
  iniciar = input('Para iniciar digite s, para sair digite n: ')

#Encerra a aplicação de acordo com a opção escolhida pelo user.
#Limpa a lista caso a escolha seja 'sair'.
  if (iniciar == 'n'):
      results.clear
      break

#Valida se a opção escolhida é válida.
  while iniciar != 's':
    iniciar = input('Digite uma opção válida: ' )

  else:
#Input para setar os números.
    num1 = int(input('Para começar, digite um número: '))
    num2 = int(input('Digite outro número: '))

#input para setar a opreção desejada.
    op = input('Qual operação deseja fazer: +, -, *, /: ')

#Caso a escola for SOMA.
    if (op == "+"):
      soma = num1 + num2
      results.append(soma)
      print('O resultado da sua conta é: ', soma)

#SUBTRAÇÃO.
    elif (op == '-'):
      subt = num1 - num2
      results.append(subt)
      print('O resultado da sua conta é: ', subt)

#MULTIPLICAÇÃO.
    elif(op == '*'):
      multp = num1 * num2
      results.append(multp)
      print('O resultado da sua conta é: ', multp)

#DIVISÃO.
    elif(op == '/'):
      divid = num1 / num2
      results.append(divid)
      print('O resultado da sua conta é: ', divid)

#Iniciando a variável que mostra os resultados.
  mostraResultados = 's'

#Início do laço de repetição.
  while mostraResultados == 's':

#Input para mostrar resultados.
    mostraResultados = input('Deseja ver os resultados das contas?')

#Caso o user não queira ver, o laço é interrompido.
    if mostraResultados == 'n':
      break

#Caso ele opte por ver, os resultados são mostrados.
    else:
      print(results)
