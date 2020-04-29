def contText ():
  for iy in range(65, 91, 1):
    if char[it] == chr(iy):
      alf [iy - 65] = alf[iy - 65] + 1

    if char[it] == chr(iy + 32):
      alf [iy - 65] = alf[iy - 65] + 1

  """      #TESTE
  for iy in range(65, 91, 1):
    if (char[it] == chr(iy)) or (char[it] == chr(iy + 32)):
      print("char " + chr(iy) + " ENCONTRADO")
    else:
      print("char " + chr(iy) + " nao encontrado")

  print("---------------------")
 """

def prinText ():
  for it in range(0, len(alf)):
    #print(alf[it])  #imprime tudo com \n
    print(alf[it], end="")

    """
    150 caracteres alf[it]
    15  caracteres alf[it]
    5   caracteres alf[it]
    """
    if (alf[it] < 10):
      print("   caracteres ", chr(it + 65), end="")
    elif (alf[it] < 100):
      print("  caracteres ", chr(it + 65), end="")
    else:
      print(" caracteres ", chr(it + 65), end="")

    print(" ", end="")

    if (alf[it] < 80):
      for it in range(0, alf[it]):
        print("|", end="")
    else:
      for it in range(0, 72):
        print("|", end="")
      print("max de |", end="")

    print("")

def curiosidades ():
  number = [0]
  carac = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
           -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
           -1, -1, -1, -1, -1, -1]
  for it in range(0, len(alf)):
    if (alf[it] > number[0]):
      number[0] = alf[it]
      carac[0] = it
  for it in range(0, len(alf)):
    if (alf[it] == number[0]) and (it != carac[0]):
      carac[it] = it

  print("\nA(s) letra(s) mais usada(s) foi(foram): ", end="")
  for pr in range(0, len(carac)):
    if(carac[pr] != -1):
      print(chr(carac[pr] + 65) + ", ", end="")
  print(" com uso ", number[0], "veze(s)")





alf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0]

re = 1
reAUX = 1
while re == 1:
  char = input("digite o texto: ")

  for it in range(0, len(char)):
    contText()

  print("\n")
  prinText()
  curiosidades()

  re = input("\nrepetir? \nr ou R para SIM. qualquer outra coisa para nao: ")
  if (re == 'r') or (re == 'R'):
    re = 1
    reAUX = input("\nresetar as veriaveis? \nr ou R para SIM. qualquer outra coisa para nao: ")
    if (reAUX == 'r') or (reAUX == 'R'):
      alf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0]
  else:
    re = 0

"""  #ASCII code
for i in range(32,128):
    print("Caracter '%s' tem código ASCII %d"%(chr(i), i))
"""
