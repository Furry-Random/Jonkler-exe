import subprocess #nescessária pra executar o comando do CMD
import time       #pro programa fazer uma pausa pro usuário poder ler as mensagens

jonkler = "jonkler.exe" #armazena o nome do joke virus, caso eu mude algum dia, é só mudar aqui

try:
    # O check=True fará o raise de uma exceção se o comando falhar

    #fecha o "jonkler.exe" por meio do "taskkill", (comando do CMD)
    subprocess.run(f"taskkill /F /IM {jonkler}", check=True, shell=True, capture_output=True)

    #diz pro usuário que o jonkler foi derrotado e agora ele está a salvo
    print(f"O {jonkler} foi derrotado, mas você precisa fechar todas as imagens que ele abriu manualmente...")
    time.sleep(8)
    print("E nem me adianta me olhar com essa cara, eu já fiz o trabalho sujo!")
    time.sleep(7)
except subprocess.CalledProcessError as e:
    
    #caso o "jonkler.exe" não esteja aberto ou o "Batman.exe" tenha dado um erro, (por sei lá o motivo)
    print(f"Ou o {jonkler} não está aberto ou ocorreu um erro, em caso de dúvidas, siga as instruções do README para procurar e fechar o jonkler manualmente...")
    print("Para isso, segure a tecla ctrl e clique no link:")
    print("https://github.com/Furry-Random/Jonkler-exe/tree/main?tab=readme-ov-file#como-fechar-o-jonklerexe-x-hocho")
    
    #isso é pro usuário conseguir ler o resultado e abrir o link no terminal
    time.sleep(20)
