def MAIN ():
  global main

  print("\n________Welcome___________\n"
        "this is program arithmetic\n")

  print("MAIN:               write")
  print("sum:________________1")
  print("subtraction:________2")
  print("multiplication:_____3")
  print("division:___________4")
  print("table:______________5")
  print("factorial:__________6")
  print("percentage:_________7")
  print("\nexit:_______________8")

  main = float(input("                  > "))
  main = int(main)

  if (main == 0):
    print("Main select")
  elif (main == 1):
    print("function sum select")
    sum()
  elif (main == 2):
    print("function subtraction select")
    subtraction()
  elif (main == 3):
    print("function multiplication select")
    multiplication()
  elif (main == 4):
    print("function division select")
    division()
  elif (main == 5):
    print("function table select")
    table()
  elif (main == 6):
    print("function factorial select")
    calcFactorial()
  elif (main == 7):
    print("function percentage select")
    percentage()
  elif (main == 8):
    main = 8
  else:
   print("invalid number. return main")
   main = 0


def sum():
  resetFunction = 1
  while (resetFunction == 1):
    numberA = float(input("write first number: "))
    numberB = float(input("write second number: "))

    print(numberA, "+", numberB, "=", numberA + numberB)

    retr = int(input("\nreturn main:__________________0\n"
                     "return function sum___________1\n"
                     "exit__________________________2\n"
                     "                            > "))
    global main
    if (retr == 0):
      main = 0
      resetFunction = 0  # autoriza sair da funcao
    elif (retr == 1):
      resetFunction = 1  # continua na funcao
    else:
      main = 100  # sair da funcao para depois parar o aplicativo
      resetFunction = 0


def subtraction():
    resetFunction = 1
    while (resetFunction == 1):
        numberA = float(input("write first number: "))
        numberB = float(input("write second number: "))

        print(numberA, "-", numberB, "=", numberA - numberB)

        retr = int(input("\nreturn main:__________________0\n"
                         "return function name__________1\n"
                         "exit__________________________2\n"
                         "                            > "))
        global main
        if (retr == 0):
            main = 0
            resetFunction = 0  # autoriza sair da funcao
        elif (retr == 1):
            resetFunction = 1  # continua na funcao
        else:
            main = 100  # sair da funcao para depois parar o aplicativo
            resetFunction = 0


def multiplication():
  resetFunction = 1
  while (resetFunction == 1):
    numberA = float(input("write first number: "))
    numberB = float(input("write second number: "))

    print(numberA, "*", numberB, "=", numberA * numberB)

    retr = int(input("\nreturn main:_____________________0\n"
                     "return function multiplication___1\n"
                     "exit_____________________________2\n"
                     "                               > "))
    global main
    if (retr == 0):
      main = 0
      resetFunction = 0  # autoriza sair da funcao
    elif (retr == 1):
      resetFunction = 1  # continua na funcao
    else:
      main = 100  # sair da funcao para depois parar o aplicativo
      resetFunction = 0


def division():
  resetFunction = 1
  while (resetFunction == 1):
    numberA = float(input("write first number: "))
    numberB = float(input("write second number: "))
    while(numberB == 0):
      numberB = float(input("ops, write second number: "))

    print(numberA, "/", numberB, "=", numberA / numberB)

    retr = int(input("\nreturn main:_____________  0\n"
                     "return function division___1\n"
                     "exit_______________________2\n"
                     "                         > "))
    global main
    if (retr == 0):
      main = 0
      resetFunction = 0  # autoriza sair da funcao
    elif (retr == 1):
      resetFunction = 1  # continua na funcao
    else:
      main = 100  # sair da funcao para depois parar o aplicativo
      resetFunction = 0


def table():
  resetFunction = 1
  while (resetFunction == 1):
    numberA = float(input("write first number: "))
    ope = input("* or /: ")
    while ((ope != '*') and (ope != '/')):
      ope = input("* or /: ")

    numberB = float(input("write lim number: "))
    while(numberB < 0):
        numberB = float(input("ops. write lim number: "))

    print("")
    if(ope == '*'):
      i = 0
      while(i <= numberB):
        print(numberA, "*", i, "=", numberA * i)
        i= i + 1
    else:
      i = 1
      while(i <= numberB):
        print(numberA, "/", i, "=", numberA / i)
        i = i + 1


    retr = int(input("\nreturn main:__________________0\n"
                     "return function table_________1\n"
                     "exit__________________________2\n"
                     "                            > "))
    global main
    if (retr == 0):
      main = 0
      resetFunction = 0  # autoriza sair da funcao
    elif (retr == 1):
      resetFunction = 1  # continua na funcao
    else:
      main = 100  # sair da funcao para depois parar o aplicativo
      resetFunction = 0


def calcFactorial():
  resetFunction = 1
  while (resetFunction == 1):
    fac = float(input("write a number: "))
    while (fac < 0):
      fac = float(input("invalid number\n"
                        "please, write a number: "))
    fac = int(fac)

    #calcFactorial
    facAux = fac
    facAux2 = fac - 1
    facEND = 1

    # 5! = 5x4x3x2x1 = 120
    while (facAux2 > 0):
        facEND = facEND * facAux * facAux2

        # print(facEND, facAux, facAux2)
        # print(facAux2)
        facAux = facAux - 2
        facAux2 = facAux2 - 2

    print("factorial", fac, "is", facEND)
    retr = int(input("\nreturn main:__________________0\n"
                       "return function factorial_____1\n"
                       "exit__________________________2\n"
                       "                            > "))
    global main
    if(retr == 0):
      main = 0
      resetFunction = 0 #autoriza sair da funcao
    elif (retr == 1):
      resetFunction = 1 #continua na funcao
    else:
      main = 100          #sair da funcao para depois parar o aplicativo
      resetFunction = 0


def percentage():
  resetFunction = 1
  while (resetFunction == 1):
    numberA = float(input("write first number: "))
    numberB = float(input("write % number: "))

    porcent = numberA * numberB
    porcent = porcent / 100

    print(numberA, "*", numberB, "% =", porcent)

    retr = int(input("\nreturn main:__________________0\n"
                     "return function percentage____1\n"
                     "exit__________________________2\n"
                     "                            > "))
    global main
    if (retr == 0):
      main = 0
      resetFunction = 0  # autoriza sair da funcao
    elif (retr == 1):
      resetFunction = 1  # continua na funcao
    else:
      main = 100  # sair da funcao para depois parar o aplicativo
      resetFunction = 0


#exemple
'''
def name():
  resetFunction = 1
  while (resetFunction == 1):



    retr = int(input("\nreturn main:__________________0\n"
                     "return function name__________1\n"
                     "exit__________________________2\n"
                     "                            > "))
    global main
    if (retr == 0):
      main = 0
      resetFunction = 0  # autoriza sair da funcao
    elif (retr == 1):
      resetFunction = 1  # continua na funcao
    else:
      main = 100  # sair da funcao para depois parar o aplicativo
      resetFunction = 0
'''


main = 0
while (main == 0):
  MAIN()
