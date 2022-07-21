import util

while True:
    resp = 0
    print("=" * 40)
    print("[1]Adição [2]Subtração [3]Multiplicação")
    print("[4]Divisão [5]Potenciação [6]Radiciação")
    print("Qual tabuada você quer treinar?")
    print("=" * 40)
    resp = int(input("Sua resposta? [EM NÚMEROS] [0 -> terminar]:"))
    if resp == 0:
        break
    elif resp == 1:
        util.tabuada("+")
    elif resp == 2:
        util.tabuada("-")
    elif resp == 3:
       util.tabuada("*")
    elif resp == 4:
       util.tabuada("/")
    elif resp == 5:
       util.tabuada("**")
    elif resp == 6:
       util.tabuada("*/")
    else:
        print("Opção invalida, tente novamente.")
