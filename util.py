from random import randint

def tabuada(sinal):
    if sinal == "+":
        while True:
            mudarFinalizar = 0
            print("-" * 40)
            num = int(input("Qual número você que ver a tabuada?"))
            quantasPerguntas = int(input("Quantas perguntas? "))
            print("-" * 40)
            while True:
                for c in range(0, quantasPerguntas, 1):
                    a = randint(0, 10)
                    print("." * 40)
                    print(f"Quanto é {num} + {a}?")
                    resp = int(input("Sua resposta: "))
                    while resp != (num + a):
                        resp = int(input("Tente novamente! Sua resposta: "))
                    print(f"Você acetou! a resposta é {num + a}")
                    print("." * 40)
                print("[0]não [1]sim")
                continuar = int(input("Que acresentar mais perguntas?"))
                if continuar == 0:
                    print("[0]mudar [1]finalizar")
                    mudarFinalizar = int(input("Que mudar de Número ou finalizar?  "))
                    print("." * 40)
                    break
                else:
                    quantasPerguntas = int(input("Quantas perguntas? "))
                    print("-" * 40) 
            if mudarFinalizar > 0:
                break
    elif sinal == "-":
        while True:
            mudarFinalizar = 0
            print("-" * 40)
            num = int(input("Qual número você que ver a tabuada?"))
            quantasPerguntas = int(input("Quantas perguntas? "))
            print("-" * 40)
            while True:
                for c in range(0, quantasPerguntas, 1):
                    a = randint(0, 10)
                    print("." * 40)
                    print(f"Quanto é {num} - {a}?")
                    resp = int(input("Sua resposta: "))
                    while resp != (num - a):
                        resp = int(input("Tente novamente! Sua resposta: "))
                    print(f"Você acetou! a resposta é {num - a}")
                    print("." * 40)
                print("[0]não [1]sim")
                continuar = int(input("Que acresentar mais perguntas?"))
                if continuar == 0:
                    print("[0]mudar [1]finalizar")
                    mudarFinalizar = int(input("Que mudar de Número ou finalizar?  "))
                    print("." * 40)
                    break
                else:
                    quantasPerguntas = int(input("Quantas perguntas? "))
                    print("-" * 40) 
            if mudarFinalizar > 0:
                break
    elif sinal == "*":
         while True:
            mudarFinalizar = 0
            print("-" * 40)
            num = int(input("Qual número você que ver a tabuada?"))
            quantasPerguntas = int(input("Quantas perguntas? "))
            print("-" * 40)
            while True:
                for c in range(0, quantasPerguntas, 1):
                    a = randint(0, 10)
                    print("." * 40)
                    print(f"Quanto é {num} * {a}?")
                    resp = int(input("Sua resposta: "))
                    while resp != (num * a):
                        resp = int(input("Tente novamente! Sua resposta: "))
                    print(f"Você acetou! a resposta é {num * a}")
                    print("." * 40)
                print("[0]não [1]sim")
                continuar = int(input("Que acresentar mais perguntas?"))
                if continuar == 0:
                    print("[0]mudar [1]finalizar")
                    mudarFinalizar = int(input("Que mudar de Número ou finalizar?  "))
                    print("." * 40)
                    break
                else:
                    quantasPerguntas = int(input("Quantas perguntas? "))
                    print("-" * 40) 
            if mudarFinalizar > 0:
                break
    elif sinal == "/":
         while True:
            mudarFinalizar = 0
            print("-" * 40)
            num = int(input("Qual número você que ver a tabuada?"))
            quantasPerguntas = int(input("Quantas perguntas? "))
            print("-" * 40)
            while True:
                for c in range(0, quantasPerguntas, 1):
                    a = randint(0, 10)
                    print("." * 40)
                    print(f"Quanto é {num} / {a}?")
                    resp = int(input("Sua resposta: "))
                    while resp != (num / a):
                        resp = int(input("Tente novamente! Sua resposta: "))
                    print(f"Você acetou! a resposta é {num / a}")
                    print("." * 40)
                print("[0]não [1]sim")
                continuar = int(input("Que acresentar mais perguntas?"))
                if continuar == 0:
                    print("[0]mudar [1]finalizar")
                    mudarFinalizar = int(input("Que mudar de Número ou finalizar?  "))
                    print("." * 40)
                    break
                else:
                    quantasPerguntas = int(input("Quantas perguntas? "))
                    print("-" * 40) 
            if mudarFinalizar > 0:
                break
    elif sinal == "**":
        while True:
            mudarFinalizar = 0
            print("-" * 40)
            num = int(input("Qual número você que ver a tabuada?"))
            quantasPerguntas = int(input("Quantas perguntas? "))
            print("-" * 40)
            while True:
                for c in range(0, quantasPerguntas, 1):
                    a = randint(0, 10)
                    print("." * 40)
                    print(f"Quanto é {num} ^ {a}?")
                    resp = int(input("Sua resposta: "))
                    while resp != (num ** a):
                        resp = int(input("Tente novamente! Sua resposta: "))
                    print(f"Você acetou! a resposta é {num ** a}")
                    print("." * 40)
                print("[0]não [1]sim")
                continuar = int(input("Que acresentar mais perguntas?"))
                if continuar == 0:
                    print("[0]mudar [1]finalizar")
                    mudarFinalizar = int(input("Que mudar de Número ou finalizar?  "))
                    print("." * 40)
                    break
                else:
                    quantasPerguntas = int(input("Quantas perguntas? "))
                    print("-" * 40) 
            if mudarFinalizar > 0:
                break
    elif sinal == "*/":
        while True:
            mudarFinalizar = 0
            print("-" * 40)
            raiz = int(input("Qual Raiz você quer?"))
            quantasPerguntas = int(input("Quantas perguntas? "))
            print("-" * 40)
            while True:
                for c in range(0, quantasPerguntas, 1):
                    a = randint(0, 10)
                    print("." * 40)
                    print(f"Quanto é v^{raiz} de {a}?")
                    resp = int(input("Sua resposta: "))
                    while resp != (a ** 1/raiz):
                        resp = int(input("Tente novamente! Sua resposta: "))
                    print(f"Você acetou! a resposta é {a ** 1/{raiz}}")
                    print("." * 40)
                print("[1]sim [0]não")
                continuar = int(input("Que acresentar mais perguntas?"))
                if continuar == 0:
                    print("[0]mudar [1]finalizar")
                    mudarFinalizar = int(input("Que mudar de Número ou finalizar?  "))
                    print("." * 40)
                    break
                else:
                    quantasPerguntas = int(input("Quantas perguntas? "))
                    print("-" * 40)
            if mudarFinalizar > 0:
                break

    