import time 
import random
print("O Combate Sagrado")
time.sleep(2)
print("seja bem vindo ao jogo, coloque seu nome e sua idade")
time.sleep(2)
nome_jogador = input("Insira seu nome!:")
time.sleep(2)
idade = int(input("insira sua idade!:"))
time.sleep(2)
if idade >= 16:
    print("Idade aceita! ")
    time.sleep(2)
else:
    print("Idade recusada! ")
    time.sleep(2)
    exit() #Encerra o programa se for menor de 16

# --- TELA INICIAL ---
 
print("==============================")
print("       O COMBATE SAGRADO      ")
print("==============================")
print("O jogo começa coma tela inicial")
input("Aperte ENTER (Play) para começar...\n")

print("o jogo começa!")
print("os jogadores ficam de frente.")
print("eles lutam!\n")
time.sleep(2)

# --- CONFIGURAÇÃO DOS PERSONAGENS ---
Kael_HP = 100
Nyx_HP = 100

# Variáveis para armazenar a proteção ativa dos escudos

Kael_escudo = 0
Nyx_escudo = 0

print(f"narrador: {nome_jogador}, você controlará as escolhas deste duelo sagrado!")
print(f"HP de Kael: {Kael_HP} | HP de Nyx {Nyx_HP}\ n")
time.sleep(2)

# --- LAÇO DEREPETIÇÃO: AS TRÊS RODADAS
for rodada in range (1, 4):
    print(f"=== RODADA {rodada} ===")
    time.sleep(1)

    # Reseta os escudos temporários do turo anterior
    Kael_escudo = 0
    Nyx_escudo = 0

    # 1. TURNO DE NYX (ATACA PRIMEIRO)
    print("turno de Nyx! escolha  ataque:")
    print("1 Espada das Sombras")
    print("2 Furto de Vida Sombria")
    print("3 Escudos das Trevas")
    escolha_nyx = input("Digite o número do ataque: ")
    print("\nNyx se ove rapidamente!")
    time.sleep(1)

    if escolha_nyx == "1":
        print("Nyx usa: Espada das Sombras!")
        print("Sai um monte de bixo das trevas ao  redor de Kael...")
        dano_nyx = random.randint(30,40)

        # Aplica o dano considerando se Kael tiha escudo residual (caso aplique futuramente)
        Kael_HP -= dano_nyx
        print(f"Os bixos tirão vida de Kael! Kael sofreu {dano_nyx} de dano.")

    elif escolha_nyx == "2":
        print("Nyx usa: Furto de Vida Sombria!")
        print("uma energia drena as forças colonias de Kael...")
        dano_nyx = random.randint(15, 25)
        Kael_HP -= dano_nyx
        # Nyx se cura com parte do dano causado
        nyx_HP = min(100, Nyx_HP + dano_nyx)
        print(f"nyx causou {dano_nyx} de dano e recuperou a mesma quantidade em HP!")
    elif escolha_nyx == "3":
        print("Nyx usa: Escudo das Trevas!")
        print("uma barreira escura proteje nyx de ataques iminentes.")
        Nyx_escudo = random.randint(20, 30)
        print(f"Nyx gerou um escudo de proteção de {Nyx_escudo} pontos.")
    else :
        print("Nyx hesitou e perdeu a chance de atacar!")

    print(f"HP atual de Kael: {max(0, Kael_HP)}\n")
    time.sleep(2)
    # verificar se Kael morreu antes de contra-atacar
    if Kael_HP <= 0:
        break