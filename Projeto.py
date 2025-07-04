'''
Projeto de Programação - Fundamentos Python
2025/06/30
Kauê. Mendes
'''

#Objetivo: desenvolver um jogo Água, fogo ou Terra


# Bibliotecas
import random # bliblioteca que gera codigos aleatorios 
# variáveis
def resultado(jogador, computador): # função que resulta o resultado do jogo
    if jogador == computador: # se o jogador escolheu a mesma opção
        return "Empate!" # se o jogador escolheu a mesma opção e empate
    # fogo vence terra, terra vence água, água vence fogo
    elif (jogador == 'água' and computador == 'fogo') or \
         (jogador == 'fogo' and computador == 'terra') or \
         (jogador == 'terra' and computador == 'água'):
        return "Você venceu!" # o jogador venceu
    else:
        return "Você perdeu!" # o jogador perdeu
# constantes
REGRA = "Água vence Fogo | Fogo vence Terra | Terra vence Água" # Regras do jogo

# codigo do jogo
def jogar(): # função que inicia o jogo
    opcoes = ['água', 'fogo', 'terra'] # lista de opções do jogo
    # cabeçalho do jogo
    print("=== JOGO: ÁGUA, FOGO OU TERRA ===") #titulo do jogo
    print("Regras: Água vence Fogo | Fogo vence Terra | Terra vence Água")# regras
    print("BY: Kauê Mendes\n") # desenvolvedor do jogo
    
    jogador = input("Escolha (Água, Fogo ou Terra): ").lower() # entrada do jogador
    
    if jogador not in opcoes: # verifica se a escolha é válida
        print("Escolha inválida! Tente novamente.") # escolha inválida
        return # retorna

    computador = random.choice(opcoes) # escolha aleatória do computador

    print(f"\nVocê escolheu: {jogador.capitalize()}") # mostra a escolha do jogador
    print(f"Computador escolheu: {computador.capitalize()}") # mostra a escolha do pc
    print("\n" + resultado(jogador, computador)) # resultado do jogo
# inicialização do jogo
jogar() # função para iniciar o jogo
