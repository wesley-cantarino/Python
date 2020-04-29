def calcFactorial (fac):
  facAux = fac
  facAux2 = fac - 1
  facEND = 1

  # 5! = 5x4x3x2x1 = 120
  while(facAux2 > 0):
    facEND = facEND * facAux * facAux2

    #print(facEND, facAux, facAux2)
    #print(facAux2)
    facAux = facAux - 2
    facAux2 = facAux2 - 2

  return facEND


print("\n\n\n\n\n\n\n\n\nEste programa eh capaz de calcular o fatorial de um numero inteiro :)\n")

fac = 0;

rep = 1
while(rep == 1):

    fac = float(input("escreva o numero: "))
    while(fac < 0):
        fac = float(input("Ops o numero nao pode ser negativo\n"
                        "por favor escreva o numero: "))

    fac = int(fac)
    print("fatorial de", fac,"eh: ", calcFactorial(fac))

    re = input("\nrepetir? \nr ou R para SIM. qualquer outra coisa para nao: ")
    if (re == 'r') or (re == 'R'):
        rep = 1
    else:
        rep = 0
