'''
Jogo do Pedra-Papel-Tesoura
2024.08.13
Rafaela Cardoso
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT # funções importadas de "modules.py"
from random import randint
from time import sleep

# Constantes, Variáveis e Listas
msgInicio = ['Seja bem vind@ ao',
            'Jogo do PEDRA-PAPEL-TESOURA',
            'desenvolvido por: Rafaela Cardoso',
            'BOA SORTE!'] # Variável responsável por armazenar a mensagem de início do jogo
msgs = []
playAgain = '' # Variável que armazsna a resposta do jogador
playerScore = 0
computerScore = 0

# Funções
def startPPT(): # Função que inicia o Jogo Pedra Papel Tesoura
  while(True): # Enquanto for dado como verdade
    clrScreen() # A função clrScreen é chamava para limpar a tela 
    displayHeader(msgInicio) # A função responsavel por começar o jogo e mostrar o cabeçalho armazenado em "msgInicio" é chamada
    playPTT()
    playAgain = getUserOption('Deseja jogar novamente [s/n]') # Função responsável por armazenar a opção de "Jogar Novamente" - Mostra a mensagdm acima na tela
    while not validateUserOption(playAgain, ['s', 'n', 'N', 'S']): # Enquanto as respostas recibidas forem iguais aos termos acima, a variavel "playAgain" ira puxar a função "getUserOption(armazena a resposta do usuário) e mostrar na tela a mensagem "Deseja jogar novamente [s/n]"
      playAgain =  getUserOption('Deseja jogar novamente [s/n]')
    if playAgain.lower() != 's':
      break # Se as respostas forem diferentes de "s" o jogo para



def displayMenu():
  msgs = ['Escolha:',
          '[0] -- > Pedra',
          '[1] --> Papel',
          '[2] --> Tesoura']
  displayLine()
  for msg in msgs:
    displayMsg(msg)
  displayLine()



def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs.append(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)



def determineWinner(playerChoice, computerChoice):
  play = ''
  result = ''
  choices = ['PEDRA', 'PAPEL', 'TESOURA']
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  if playerChoice == computerChoice:
    result = 'Empate!'
  elif (playerChoice == '0' and computerChoice == '2') or \
      (playerChoice == '1' and computerChoice == '0') or \
      (playerChoice == '2' and computerChoice == '1'):
    play = f" {playerChoiceStr} vence {computerChoiceStr}"
    result = 'Você Ganhou!'
  else:
    play = f'{computerChoiceStr} vence {playerChoiceStr}'
    result = 'Você Perdeu!'
  msgs = ['Jogada do Player: ' + playerChoiceStr,
          'Jogada do PC: ' + computerChoiceStr, 
         play, result]
  displayHeader(msgs)
  return result




def playPTT():
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['0','1','2']):
      displayMenu()
      playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(0,2))
    result = determineWinner(playerChoice,     
computerChoice)
    if "Ganhou" in result:
      playerScore += 1
    elif "Perdeu" in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
      displayScore('PLACAR', playerScore, computerScore)
    sleep(1)
  displayScore("PLACAR FINAL", playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(['Parabéns', 'YOU WIN!'])
  else:
    displayHeader(['Parabéns', 'YOU LOSE!'])
  
      
# Main