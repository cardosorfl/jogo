'''
Jogo do Par ou Impar
2024.08.20
Rafaela Cardoso
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT # funções importadas de "modules.py"
from random import randint
from time import sleep

# Constantes, Variáveis e Listas
msgInicio = ['Seja bem vind@ ao',
            'Jogo do PEDRA-PAPEL-TESOURA',
             ' e PAR OU ÍMPAR!'
            'desenvolvido por: Rafaela Cardoso',
            'BOA SORTE!'] # Variável responsável por armazenar a mensagem de início do jogo
msgs = []
playAgain = '' # Variável que armazena a resposta do jogador
playerScore = 0 # Váriavel da pontuação inicial do jogador
computerScore = 0 # Váriavel da pontuação inicial do computador
playerChoice = ''
computerChoice = ''
total = playerChoice + computerChoice # O resultado séra a respostado do jogador somada com a do computador

# Funções
def startparimpar(): # Tela de início do jogo PAR OU IMPAR
  while(True):
    clrScreen() # Limpa a tela em 50 linhas
    displayHeader(msgInicio) # Mostrar cabeçalho 
    Playparimpar() # Função para jogar par ou impar 
    playAgain = getUserOption('Deseja jogar novamente [s/n]') # Função que faz aparecer na tela se o jogador deseja jogar novamente
    while not validateUserOption(playAgain, ['s', 'n', 'N', 'S']): # Enquanto a resposta do usuário não for igual a 's, n, N, S' a mensagem aparecerá novamente na tela
      playAgain =  getUserOption('Deseja jogar novamente [s/n]') # Variável playagain armazena a resposta do jogador com a função getUserOption. Respondendo a função 
    if playAgain.lower() != 's':
      break # Se nenhuma das respostas forem igual a 's' o jogo para


def displayMenu(): # Função que mostra na tela o menu de escolhas
  msgs = ['Escolha:',
         '[0] - IMPAR',
         '[1] - PAR']
  displayLine() # Função que mostrar uma linha de caracteres na tela 
  for msg in msgs:
    displayMsg(msg) # Mostra a mensagem configurada acima na tela
  displayLine() # Mostra uma linha de caracteres na tela 
  if validateUserOption(msgs, ['1']): # Se a opção do usuario for igual a "1" entao a seguinte mensagem aparecerá na tela para a escolha dos números
    msg = ['Escolha:',
          '2',
          '4',
          '6',
          '8',
          '10'] # Números pares a serem escolhidos 
    displayLine() # Aparece uma linha na tela 
    for msg in msgs:
      displayMsg(msg) # Configura a variável "mensagem" na tela
    displayLine() # Aparece uma linha na tela
  elif validateUserOption(msgs, ['0']): # Caso a resposta do jagador for "0" os números que devem ser escolhidos irão aparecer como na mensagem abaixo
    msg = ['Escolha',
          '1',
          '3'
          '5',
          '7',
          '9'] #Números ímpares a serem escolhidos
    displayLine() # Aparece uma linha na tela 
    for msg in msgs:
      displayMsg(msg) # Configura a variável "mensagem" na tela
    displayLine() # Aparece uma linha na tela 
     



  
    


def displayScore(typeScore, playerScore, computerScore): # Calcila a pontuação do jogo
  msgs = []
  msgs.append(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)

def determineWinner(playerChoice, computerChoice): # Determina o ganhador
  play = ''
  result = ''
  choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] # Escolhas possíveis 
  playerChoiceStr = choices[int(playerChoice)] # Variável que guarda a opção do jogador
  computerChoiceStr = choices[int(computerChoice)] # Variável que guarda a opção do computador
  if total % 2 == int(playerChoice): # Se total for igual a 0:
    play = f" {playerChoiceStr} vence {computerChoiceStr}" # O jogador vence
    result = 'VOCÊ É O BICHÃO MESMO!' # Mensagem que aparece quando o jogador vence
  elif total %2 > 0 == int(playerChoice): # Se o resto da divisão por dois for maior que zero e corresponde a opção do jogador:
    play = f" {playerChoiceStr} vence {computerChoiceStr}" # Jogador vence
    result = 'VOCÊ É O BICHÃO MESMO!' # Mensagem que aparece quando o jogador vence
  else:
    play = f" {computerChoiceStr} vence {playerChoiceStr}"  # Caso contrário o computador vence
    result = 'YOU LOSE!' # Mensagem que aparece na tela quando 
  msgs = ['Jogada do Player: ' + playerChoiceStr,
    'Jogada do PC: ' + computerChoiceStr, 
   play, result]
  displayHeader(msgs)
  return result
  
def Playparimpar():
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
     displayMenu()
     playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(1,10))
    result = determineWinner(playerChoice,     
  computerChoice)
    if 'Ganhou!' in result:
      playerScore += 1
    elif 'Perdeu!' in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
      displayScore('PLACAR', playerScore, computerScore)
    sleep(1)
  displayScore("PLACAR FINAL", playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(['Parabéns', 'YOU WIN!'])
  else:
    displayHeader(['Parabéns', 'YOU LOSE!'])


    
