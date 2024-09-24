'''
Arquivo de Modulos
2024.08.13
Rafaela Cardoso
'''

# --> Bibliotecas
from random import choice # importei a função "choice" de "random" para fazer com que o computador, quando o código for programado, escolher certos "itens" listados em "CAR" para a formação do cabeçalho.
from time import sleep

# --> Constantes, Variáveis e Listas
TAM = 50 # Tamanho da Tela 
CAR = choice(['=', '*', '|','-']) # Caracter utilizado para desenho da tela
MAR = 5 # Tamanho da Margem


# --> Funções
def clrScreen(): # Função par limpar a tela
  print('\n'*TAM) # Mostra na tela \n == linha * TAM 

def displayLine(): # Função para mostrar uma linha de caracteres
  print(CAR*TAM) # Números de caracteres multiplicados pelo tamanho da tela

def displayMsg(msg): # Mostrar a mgs alinhada a esquerda entre CAR 
  print(f'{CAR} {msg:<{TAM - MAR}} {CAR}') # Mostrar o cabeçalho a esquerda, sendo a mensagem menor que o tamanho da margem 

def displayMsgCenter(msg):
  print(f'{CAR} {msg:^{TAM-MAR}} {CAR}') # Mostrar uma mensagem centralizada ao meio do cabeçalho.

def displayHeader(msgs): # Formação do cabeçalho a partir das funções ja programadas estando dentro de "displayHeader"
  displayLine() #mostra uma linha
  for item in msgs: # pega da biblioteca "item" a variável "msgs"
    displayMsgCenter(item) # deixa a mensagem centralizada 
  displayLine() # mostra uma linha


def displayHeaderT(msgs):
  displayLine() #mostra uma linha
  for item in msgs: # pega da biblioteca "item" a variável "msgs"
    displayMsgCenter(item) # deixa a mensagem centralizada 
    sleep(1)
displayLine() # mostra uma linha


def getUserOption(msg):   # Função responsável por pegar a resposta do usuário
  option = input(f'{CAR} {msg}: ').strip() # Mensagem transmitida para a captura da resposta do usuário, sendo um caracter de CAR e após ele a mensagem.
  return option 

def validateUserOption(option, listOptions): # a função valida a resposta do jogador 
  if option in listOptions:
    return True # se a resposta estiver em "listaOptions" o programa retornará como verdade 
  else:
    msgsErro = ['Opção Inválida!', 'Escolha Novamente...'] # se não o mesmo transmitirá a mensagem acima
    displayHeader(msgsErro) # função que mostra o aviso de mensagem errada 
    return False # retorna como falso
# --> Main