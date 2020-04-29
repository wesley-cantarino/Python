class dataBase:
    def clearDB(self):
        file = open("dataBase.txt", "w") #apaga tudo

    def writeDB(self):
        file = open("dataBase.txt", "a") #escrita obs: se nao existir sera criado
        return file

    def readDB(self):
        file = open("dataBase.txt", "a") #leitura

def main():
    print("\n\n\n\n\n\n\n\nHello old friend. This is phoneBook :D\n")
    print("Available services:\n")
    print("Create user _____ 1")
    print("Search __________ 2")
    print("Exit ____________ 3")
    print("Clear dataBase___ 9")
    op = int(float(input("                > ")))

    if(op == 1):
        createContact()
    elif(op == 2):
        search()
    elif(op == 3):
        sair = int(input("Exit? 1 for YES. 2 for NO: "))
        if(sair == 1):
            print("Goodbye")
        else:
            main()
    elif(op == 9):
        sair = int(input("!!!ATTENTION!!!\n"
                         "CLEAR DATABASE ? 1 for YES. 2 for NO: "))
        if (sair == 1):
            file = open("dataBase.txt", "w")
            file.close()
            print("Cleaned")
            main()
        else:
            print("Not Cleaned")
            main()

def createContact():
    op = 1
    while (op == 1):
        nome = input("Full name: ")
        phone = input("Phone: ")

        print("\nName: ", nome, " phone: ",phone)
        rig = int(input("Right? 1 for YES. 2 for NO :"))
        while(rig == 2):
            nome = input("Full name: ")
            phone = input("Phone: ")
            print("\nName: ", nome, " phone: ", phone)
            rig = int(input("Right? 1 for YES. 2 for NO :"))

        file = open("dataBase.txt", "a")
        file.write(nome.title() + ", ")
        file.write(phone + "\n")
        print("Success :D")

        op = int(input("\nOver again? 1 for YES. 2 for NO "))

    file.close()
    main()

def search():
    file = open("dataBase.txt", "a")
    print("\n   Search")
    decisao = int(input("1 = Full \n2 = Single\n3 = main\n"))

    if(decisao == 1):
        print("\n*****start*****\n")
        file = open("dataBase.txt").readlines()
        #file = [str(x).rstrip() for x in file]
        for linha in file:
            print(linha, end='')

        print("\n******END******")
        search()

    elif(decisao == 2):
        op = 1
        while (op == 1):
            name_contact = input("Name Search: ")
            print("")

            file = open("dataBase.txt").readlines()
            righ = 0
            #file = [str(x).rstrip() for x in file]
            for linha in file:
                lista = linha.split(",")
                if name_contact.title() in lista:
                    print("     Here:")
                    print("Name: " + lista[0] + "\nphone:" + lista[1])
                    righ = 1 + righ

            if(righ == 0):
                print("Not found :/")
            else:
                print("items found: ", righ)
            op = int(input("over again?\n1-YES\n2-NO\n"))

        search()

    else:
        main()
        file.close()

main()