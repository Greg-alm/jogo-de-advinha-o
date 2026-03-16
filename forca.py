def forca():

    print("-------------------------------")
    print("\nBem vindo ao jogo da Forca")
    print("-------------------------------")

    palavra_secreta = "processador"
    perdeu = False
    acertou = False

    while(not perdeu and not acertou ):
        chute =  input("escreva uma letra:  ")
        chute = chute.strip()

        for letra in palavra_secreta: 
            if(chute == letra):
                print(letra)

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f"A letra {chute} está na posição {index}")
            index = index + 1


if(__name__ == "__main__"):
    forca()