import random   #pra gerar um número aleatório
import pygame   #para executar o som/música (winsound não funcionou no meu note gamer)
import time     #pro código jogar o dado de tempos em tempos
import os       #pra abrir uma imagem no Windows (não acho que seja específica do Windows)

#armazena o caminho do executável, da raíz até o diretório do .exe
caminho = os.getcwd()

#armazena o jonkler.jpg
classic_image = caminho + "\Assets\jonkler.jpg"
#armazena o WHY_SO_SERIOUS.mp3
audio_why = caminho + "\Assets\WHY_SO_SERIOUS.mp3"

#armazena o tempo entre um sorteio e outro (em segundos)
delay = 10

#inicia o módulo de som do pygame
pygame.mixer.init()

#carrega o áudio na memória e atriubi a "why_so_serious"
why_so_serious = pygame.mixer.Sound(audio_why)

#roda pra sempre
while True:

    #gera o número aleatório entre 1 e 6
    dado = random.randint(1, 6)

    #imprime pra ver qual número caiu
    print("O dado caiu em: ", dado)
    
    #verifica se o dado caiu no 6
    if dado == 6:

        #debug pra ver se caiu no IF msm
        print("Entrou no if HAHAHAHAHAHA")

        #abre a imagem
        os.startfile(classic_image)
        #executa o áudio
        why_so_serious.play()
    
    #espera "delay" segundos
    time.sleep(delay)
