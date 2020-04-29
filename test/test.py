def descText(k):
    for read in text:  # var read varre text
        if read == chr(32):
            print(" ", end='')
        else:
            for i in range(97, 123):  # minusculo
                if read == chr(i):
                    if (i - k >= 97):
                        print(chr(i - k), end='')
                    else:
                        print(chr(i - k + 26), end='')

            for i in range(65, 91):  # maiusculo
                if read == chr(i):
                    if (i - k >= 65):
                        print(chr(i - k), end='')
                    else:
                        print(chr(i - k + 26), end='')


text = input("->")

k = 1
descText(k)