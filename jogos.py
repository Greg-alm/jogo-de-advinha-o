import advinhacao
import forca

print("----------------")
print("Escolha seu jogo")
print("----------------")

print("(1) Advinhação (2) forca")

opcao_jogo = int(input("Escolha seu jogo"))

if(opcao_jogo == 1):
 print("Escolhendo Advinhaçao")
 advinhacao.advinhacao()
elif(opcao_jogo == 2):
 print("Escolhendo Forca")
forca.forca()