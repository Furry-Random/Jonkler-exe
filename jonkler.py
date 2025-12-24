'''
Programa feito pra dar susto de tempos em tempos com ajuda de uma imagem e um áudio

Feito em 03/12/2025, por Furry Random!

Espero que gostem :)

FR!
'''

import random #pra gerar um número aleatório
import time #pro código jogar o dado de tempos em tempos
import pygame #para executar o som/música (winsound não funcionou no meu note gamer)
import os #pra abrir uma imagem no Windows (não acho que seja específica do Windows)

#armazena o caminho da imagem
#TODO: No momento, a imagem precisa ficar dentro da pasta "dist", tem que arrumar um jeito do programa encontrar o diretório correto dos arquivos
imagem = 'jonkler.jpg'

#armazena o caminho do áudio
#TODO: Mesmo problema da imagem do jonkler, ele só encontra se os arquivos estiverem no mesmo local que o executável
audio = 'WHY_SO_SERIOUS.mp3'

#armazena o tempo entre um sorteio e outro (em segundos)
delay = 10

#inicia o módulo de som do pygame
pygame.mixer.init()

#carrega o áudio na memória
pygame.mixer.music.load(audio)

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
        os.startfile(imagem)

        #executa o áudio
        pygame.mixer.music.play()
    
    #espera "delay" segundos
    time.sleep(delay)