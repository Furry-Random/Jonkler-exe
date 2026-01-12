import subprocess #para executar comandos do CMD
import random     #pra gerar um número aleatório
import pygame     #para executar o som/música (winsound não funcionou no meu note gamer)
import time       #pro código jogar o dado de tempos em tempos
import os         #pra abrir uma imagem no Windows (não acho que seja específica do Windows)

#armazena o caminho do executável, da raíz até o diretório do .exe
caminho = os.getcwd()

#[MEMES GRINGOS]
#armazena o jonkler.jpg
classic_image = caminho + "\Assets\jonkler.jpg"
#armazena o WHY_SO_SERIOUS.mp3
caminho_audio_why = caminho + "\Assets\WHY_SO_SERIOUS.mp3"

#[MEMES BR]
#armazena o jonkler_fotos.jpg
jonkler_fotos = caminho + "\Assets\jonkler_fotos.jpg"
#armazena o jonkler_fotos.mp3
caminho_jonkler_fotos_audio = caminho + "\Assets\jonkler_fotos.mp3"

#armazena os links
rola_pg_wiki = "https://pt.wikipedia.org/wiki/Rolinha-roxa"
imagem_rola_meme = "https://images7.memedroid.com/images/UPLOADED48/541f4901744a0.jpeg"
joker_gif = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDR1cGt3OWFkanc3YmJ3MXUzejk1NnJzZnF6Nnl0dXVzZXJocXdyMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dYPRVPUqkpzYQ/giphy.gif"

#armazena o tempo entre um sorteio e outro (em segundos)
delay = 20

#inicia o módulo de som do pygame
pygame.mixer.init()

#carrega os áudios na memória
audio_why = pygame.mixer.Sound(caminho_audio_why)
jonkler_fotos_audio = pygame.mixer.Sound(caminho_jonkler_fotos_audio)

#roda pra sempre
while True:

    #gera o número aleatório entre 1 e 6
    dado = random.randint(1, 6)

    #[DEBUG] imprime pra ver qual número caiu
    print("O dado caiu em: ", dado)
    
    #verifica se o dado caiu no 3, toca meme BR
    if dado == 3:
        
        #[DEBUG] pra ver se caiu no IF msm
        print("Dado = 3, executando meme BR")

        #abre a imagem
        os.startfile(jonkler_fotos)
        #executa o áudio
        jonkler_fotos_audio.play()
        time.sleep(13)
        
        #abre o meme da rola (ave)
        subprocess.run(f"start {imagem_rola_meme}", check=False, shell=True, capture_output=False)
        #o usuário vai ver a rola (ave) primeiro, e depois vai ver a Wiki sobre rolas roxas 
        time.sleep(5)
        #abre a página da Wiki sobre a ave "rolinha roxa"
        subprocess.run(f"start {rola_pg_wiki}", check=False, shell=True, capture_output=False)
    
    #verifica se o dado caiu no 6, toca meme gringo
    elif dado == 6:

        #[DEBUG] pra ver se caiu no IF msm
        print("Dado = 6, executando meme gringo")

        #abre a imagem
        os.startfile(classic_image)
        #executa o áudio
        audio_why.play()
        time.sleep(7)

        #abre um gif do filme do joker, (qual? não sei, eu não ví o filme...)
        subprocess.run(f"start {joker_gif}", check=False, shell=True, capture_output=False)
    
    #espera "delay" segundos
    time.sleep(delay)
