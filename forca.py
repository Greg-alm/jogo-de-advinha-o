import random as rd

def mensagem_inicial():
    print("-"*26)
    print("\nBem Vindo ao Jogo da Forca\n")
    print("-"*26)

def selec_palavra_aleatoria():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    posicao = rd.randrange(0,len(palavras))

    palavra_secreta = palavras[posicao].upper()
    return palavra_secreta

def letras_corretas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def entrada_de_dados():
    chute = input("Escreva uma Letra: ")
    chute = chute.strip().upper()
    return chute

def chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def jogar_forca():
    
    mensagem_inicial()
    palavra_secreta = selec_palavra_aleatoria()
    letras_acertadas = letras_corretas(palavra_secreta)

    perdeu = False
    acertou = False
    erros = 0

    while(not perdeu and not acertou):
        chute = entrada_de_dados()

        #Index define a posição da letra
        
        if(chute in palavra_secreta):
            chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros = erros + 1  
            perdeu = erros == 8
            acertou = "_" not in letras_acertadas

        print(erros)
        print(letras_acertadas)
        
if(__name__ == "__main__"):
    jogar_forca()