def forca():

    print("-------------------------------")
    print("\nBem vindo ao jogo da Forca")
    print("-------------------------------")


    arquivo = open("jogos/palavras.txt", "r")
    palavra = []

    palavra_secreta = "processador".upper()
    acertos = ["_" for letra in palavra_secreta]
    
    for linha in palavra:
        linha = linha.strip()
        palavra.append(linha)
    
    arquivo.close()
    
    
    perdeu = False
    acertou = False
    erros = 0


    while(not perdeu and not acertou ):
        chute =  input("escreva uma letra:  ")
        chute = chute.strip().upper()

        index = 0

        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    acertos[index] = letra
                index = index + 1  
        else:
            erros = erros + 1
        
                
        perdeu = erros==6
        acertou = "_" not in acertos
                
        print(acertou)
        print(erros)
        print(acertos)

if(__name__ == "__main__"):
    forca()