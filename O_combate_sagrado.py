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
print(f"HP de Kael: {Kael_HP} | HP de Nyx {Nyx_HP}\n")
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
    print("\nNyx se move rapidamente!")
    time.sleep(1)

    if escolha_nyx == "1":
        print("Nyx usa: Espada das Sombras!")
        print("Sai um monte de bixo das trevas ao  redor de Kael...")
        dano_nyx = random.randint(15,20)

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
        Nyx_escudo = random.randint(15, 25)
        print(f"Nyx gerou um escudo de proteção de {Nyx_escudo} pontos.")
    else :
        print("Nyx hesitou e perdeu a chance de atacar!")

    print(f"HP atual de Kael: {max(0, Kael_HP)}\n")
    time.sleep(2)
    # verificar se Kael morreu antes de contra-atacar
    if Kael_HP <= 1:
        break

    #2. turno de Kael (contra-ataca)
    print("turno de Kael! escolha o contra-ataque:")
    print("1 fogo divino")
    print("2 cajado da luz")
    print("3 escudo divino")

    escolha_Kael = input("digite o número de ataque: ")
    print("\nKael concentra para reponder!")
    time.sleep(1)

    if escolha_Kael =="1":
            print("Kael usa: Fogo Divino!")
            print("cria uma roda de fogo em torno de Nyx.")
            print("esse fogo causa dano em área e fica tirando vida...")
            dano_Kael = random.randint(30, 40)
            # Se Nyx usou escudo, reduz o dano recebido
    if Nyx_escudo > 0:
            dano_absorvido = min(Nyx_escudo, dano_Kael)
            Nyx_escudo -= dano_absorvido
            dano_Kael -= dano_absorvido
            print(f"O Escudo das Trevas de Nyx absorveu {dano_absorvido} de dano!")
            Nyx_HP -= dano_Kael
            print(f"O Fogo queima Nyx! Nyx sofreu {dano_Kael} de dano direto")
    elif escolha_Kael =="2":
            print("Kael usa: Cajado da Luz!")
            print("um feixe de luz atinge Nyx diretamente.")
            dano_Kael = random.randint(30, 40)
            if Nyx_escudo > 0:
                dano_absorvido = min(Nyx_escudo, dano_Kael)
                Nyx_escudo -= dano_absorvido
                dano_Kael -= dano_absorvido
                print(f"O escudo das trevas de Nyx absorveu {dano_absorvido} de dano!")

                nyx_HP -= dano_Kael
                print(f"A luz atinge o alvo! Nyx sofreu {dano_Kael} de dano direto.")
            elif escolha_Kael == "3":
                print("Kael usa: Escudo Divino!")
                print("uma aura sagrada surge defendê-lo no próximo turno.")
                Kael_escudo = random.randint(30, 40)
                # Como Kael usa o escudo DEPOIS de já ter tomado dano do Nyx nesta rodada,
                # o valor do escudo será aplicado para mitigar o dano na proxima rodada.
                print(f"Kael ativou uma barreira protetora de {Kael_escudo} pontos para o proximo turno")
            else:
                print("Kael falhou no comando e perdeu a oportunidade!")
                print(f"HP atual de Nyx: {max(0, nyx_HP)}")
                print("=" * 30 + "\n")
                time.sleep(3)
            # Aplica o escudo de Kael retroativamente caso a rodada continue
            if Kael_escudo > 0 and rodada < 3:
                Kael_HP = min(100, Kael_HP + Kael_escudo)
                print(f"o Escudo Divino se converteu em proteção extra para a vida de Kael!")
                Kael_escudo = 0
            # Verifica se Nyx morreu
            if Nyx_HP <= 0: 
                break
    # --- FIM DAS TRÊS RODADAS / RESULTAO FINAL ---
    print("Fim das três rodadas ou um dos guerreiros caiu!")
    print("\n=== RESULTADO FINAL ===")
    print(f"HP final de Kael: {(Kael_HP)}")
    print(f"HP final de Nyx: {(Nyx_HP)}")

    if Kael_HP <= 0 and nyx_HP <= 0:
         print("Empate lendário! ambos tombaram no mesmo turno!")
    elif Kael_HP <= 0:
         print("Nyx venceu! as sombras consumiram o Fogo Divino.")
    elif Nyx_HP <= 0:
         print("Kael venceu! O Fogo Divino purificou as trevas.")
    else:
         if Kael_HP > Nyx_HP:
              print("Kael venceu por pontos de vida restantes!")
         elif nyx_HP > Kael_HP:
              print("Nyx venceu por pontos de vida restantes!")
         else:
              print("empate por igualdade de pontos de vida!")

print("====================")
print("        winn        ")
print("====================")