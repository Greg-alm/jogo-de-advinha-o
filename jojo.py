import random as rd

print("-------------------------------")
print("\nBem vindo ao jogo da prestigitação!\n")
print("-------------------------------")

n_secreto = rd.randrange(1,100)
n_tentativas = 0
rodada = 1
pontos = 1000

print("niveis de dificuldade")
print("\n(1)facil (2) medio (3) dificil (4) aleatorio")
nivel = int(input("defina um numero:"))
if(nivel == 1):
    n_tentativas = 12
elif(nivel==2):
    n_tentativas = 8  
elif(nivel==3):
    n_tentativas = 3
else:
    n_tentativas =rd.randrange(1,50)


for rodada in range(1,n_tentativas + 1):
    print(f"Rodada {rodada} de {n_tentativas}")
    entrada = int(input("Digite um número entre 1 e 100: "))
    acertou = entrada == n_secreto
    entrada_maior = entrada > n_secreto
    entrada_menor = entrada < n_secreto

    if(entrada > 100 or entrada < 1):
        print("o valor digitado nao é permitido")

    print(f"\nVocê digitou o número: {entrada}")

    #Verificação de acerto/erro#
    if(acertou):
        print("Parabéns, você acertou o número secreto")
        break
    else:
        if(entrada_maior):
            print("Você errou! O número digitado foi maior que o secreto")
        if(entrada_menor):
            print("Você errou! O número digitado foi menor que o secreto")
   
pontos_perdidos =n_secreto - entrada  
pontos = pontos - pontos_perdidos
rodada = rodada + 1
    
print("\nFim de jogo")

# começa com 1000 pontos
#ela vai perder pontos
#n_secreto = 40-20 =20
#n_secreto = 40-80 = -40