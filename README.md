# A joke virus about Jonkler brainrot.

## Introdução :telescope:
Esse programa se trata de um joke virus, (vírus de piada), feito com o único objetivo de assustar/irritar/divertir ou só atrapalhar o usuário, ativando aleatoriamente enquanto utiliza o computador, inspirado no meme brainrot do Jonkler.

Existem várias versões do meme, mas caso você não conheça, [clique aqui](https://youtu.be/6KlSYJxTeyk?si=L0f4g1gRkK-nOpOG) para ver uma das versões.

## Sistemas Operacionais Compatíveis :computer: :window:
Os softwares funciona nos seguintes sistemas operacionais:

- Windows 10
- Windows 11

**O jonkler.exe não funciona no Linux**, já outras versões do Windows, como o 7 ou 8 não foram testadas.

## Funcionamento (jonkler.exe) :game_die: :black_joker:
Ele inicia um **loop infinito**, onde ele atribui a variável ```dado``` um número aleatório entre 1 a 6 através da função ```random.randint(1, 6)```, após isso, ele verifica:

- Se ```dado``` for igual a ```3```, então ele abre uma imagem, toca um áudio relacionado a imagem, abre um meme de uma pomba (ave) e a página da Wikipédia sobre rolas-roxas, (a ave, é claro), depois ele espera alguns segundos e sorteia mais um número aleatório.

- Se ```dado``` foi igual ao valor ```6```, então ele abre uma outra imagem, toca outro áudio e abre um gif do joker, (de uma parte aleatória do filme), depois ele aguarda alguns segundos e sorteia mais um número aleatório.

- Caso ```dado``` não seja igual a ```3``` ou a ```6```, então ele não faz nada, apenas espera alguns segundos e repete o loop.

O tempo de espera entre os lançamentos do dado é configurado na variável ```delay```, e no momento ```delay``` é igual a ```20```. Isso dá + ou - 1 ativação por minuto.

Tudo isso operando em **segundo plano**.

## Funcionamento (Batman.exe) :bat: :hocho:
Ele basicamente fecha o jonkler.exe através do seguinte comando:

```taskkill /F /IM jonkler.exe```

E para fechar as imagens, ele utiliza o comando:

```taskkill /F /IM Photos.exe```

Onde:

- ```taskkill``` -> Fechar o processo
- ```/F```       -> Força a ação
- ```/IM```      -> Permite buscar pelo nome do programa, ao invés de usar o PID
- ```<nome do software.exe>``` -> Nome do programa a ser encerrado.

Ele consegue fechar as imagens caso você utilize o **Fotos** da Microsoft como app padrão para abri-las, senão ele apresenta uma mensagem de erro, dizendo que não encontrou as imagens.

E caso o jonkler não esteja aberto, ou o comando tenha apresentado erro, ele exibe o link para acessar o tutorial de como fechar o jonkler.exe manualmente, o mesmo se encontra neste README.

## Capturas de Tela :camera:
Quanto mais tempo o programa rodar, mais imagens serão abertas.

![jonkler-varias-instancias](readme_assets/jonkler-varias-instancias.png)

![jonkler-area-de-trabalho](readme_assets/jonkler-area-de-trabalho.png)

![Gerenciador-de-Tarefas](readme_assets/Gerenciador-de-Tarefas-VM.png)

## Atenção :warning:
Tudo o que o programa faz pode ser revertido sem precisar de nenhum segredo, _ou qualquer habilidade de um grande mago que anda pra cima e para baixo com seus pergaminhos_, tudo o que você precisa saber é como fechar janelas e como usar o gerenciador de tarefas para encerrar o programa, (caso o Batman.exe não dê conta do recado).

> [!WARNING]
> <mark>**Mesmo que o programa seja inofensivo, eu não me responsabilizo por quaisquer danos causados ao seu computador ou de terceiros.**</mark>

E caso você não saiba como usar o Gerenciador de Tarefas para encerrar um programa, tudo bem, o tutorial se encontra neste README, ou [clicando aqui](#como-fechar-o-jonklerexe-x-hocho). :point_left:

## Como executar o jonkler.exe? :arrow_forward: :black_joker:

Após extrair os arquivos, abra a pasta ```jonkler-virus``` e execute o ```jonkler.exe```, não precisa abrir como Administrador.

Após isso, divirta-se :D

## Possivel erro de execução :x:
Segundo alguns testes em outros computadores (Windows 10 e 11), o código é bloqueado pelo **Microsoft Defender SmartScreen**, como exemplifica a imagem abaixo:

![Microsoft Defender SmartScreen](readme_assets/Microsoft-Defender-SmartScreen.png)

Se a opção estiver disponível, clique em ```Mais informações``` e depois em ```Executar assim mesmo```, assim o código vai ser executado.

## Como fechar o jonkler.exe? :x: :hocho:

### Forma automática (Batman.exe) :bat:
Execute o ```Batman.exe```, não precisa abrir como Administrador, ele deve fechar o **jonkler.exe** e as imagens abertas.

**É garantido fechar o jonkler.exe**, mas as abas no navegador terão que ser fechadas manualmente.

### Forma manual :writing_hand:
Clique com o botão direito do mouse sobre a barra de tarefas e depois clique em ```Gerenciador de Tarefas```, **ou** aperte as teclas ```Ctrl``` + ```Shift``` + ```esc``` simultâneamente.

Após isso, clique na aba ```Processos```, (é a 1° aba), e em ```Processos em Segundo Plano``` procure até encontrar pelo nome ```jonkler.exe```, (que é o nome do programa), para encerrar, clique em cima do nome ```jonkler.exe```, e depois clique em um botão chamado ```Finalizar tarefa```, esse botão está embaixo no Windows 10 e em cima no Windows 11.

Caso não esteja encontrando o processo (e você use o Windows 11), você pode buscar ele de uma forma mais simples, que é pesquisando pelo nome ```jonkler``` na barra de busca do Gerenciador de Tarefas e aí encerrando ele, (como expliquei acima). Ou o código pode ter simplesmente bugado e fechado sozinho, já aconteceu algumas vezes...

Lembre-se, encerrar o programa não fechará as imagens que ele abriu, nem mesmo as abas no navegador, sendo necessário fechar elas manualmente.

## Agradecimentos :muscle: :pray:
Agradeço profundamente aos meus amigos que testaram o meu código na máquina deles e compartilharam feedback, amo vocês :heart:

- [davi-goncalves](https://github.com/Davi-Gon)
- [heittorknielingm](https://github.com/heittorknielingm)
- [Zathexko](https://steamcommunity.com/id/Andrezat) <- Steam
- [pudimlucasd](https://steamcommunity.com/profiles/76561199074291946) <- Steam

_FR!_
