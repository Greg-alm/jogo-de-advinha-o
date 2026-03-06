import random


lukas = list(["Velho", "Idoso", "pre-historico", "velha-guarda", "CPF de 2 digitos"])


total_lukas = len(lukas)

print(f"--- VOCE É : ({total_lukas} opções) ---")
print("Digite '1' para sortear ou '0' para sair.")

while True:
    
    comando = input("\nComando: ")

    if comando == "1":
        escolha = random.choice(lukas)
        
        print(f" PARABENS VOCÊ É : {escolha}")
    
    elif comando == "0":
        print("CABO")
        break
    else:
        print("Opção inválida! Digite apenas '1' ou '0'.")