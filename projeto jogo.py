import random
#Temas e palavras
temas = {
    'objeto': ['celular', 'garfo', 'cadeira'],
    'times': ['palmeiras','vasco', 'realmadrid' ],
    'jogadores': ['rony', 'raphaelveiga', 'dudu'],
    'anime': ['jojo', 'one piece', 'chainsaw main'],
    'animais':['macaco', 'gato', 'sapo'],}

# Selecionar um tema aleatório
tema = random.choice(list(temas.keys()))
palavras = temas[tema]

# Selecionar uma palavra aleatória
palavra = random.choice(palavras)

# Variáveis do jogo
letras_erradas = []
letras_corretas = []
vidas = 6

# Função para exibir o corpo do boneco de acordo com as letras erradas
def exibir_boneco():
    partes_corpo = ['O', '|', '/', '\\', '/', '\\']
    for i in range(vidas):
        print(partes_corpo[i])

# Função para exibir o estado atual da palavra
def exibir_palavra():
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print('\n')

# Loop principal do jogo
while True:
    print(f'Tema: {tema.capitalize()}')
    exibir_palavra()
    letra = input('Digite uma letra: ').lower()

    # Verificar se a letra já foi jogada
    if letra in letras_erradas or letra in letras_corretas:
        print('Você já jogou essa letra. Tente novamente.\n')
        continue

    # Verificar se a letra está na palavra
    if letra in palavra:
        letras_corretas.append(letra)
        # Verificar se o jogador ganhou o jogo
        if set(palavra) == set(letras_corretas):
            print(f'Parabéns! Você acertou a palavra "{palavra}". Você venceu!')
            break
    else:
        letras_erradas.append(letra)
        vidas -= 1
        print(f'A letra "{letra}" não está na palavra.')
        exibir_boneco()
        print(f'Letras erradas: {", ".join(letras_erradas)}\n')
        # Verificar se o jogador perdeu o jogo
        if vidas == 0:
            print(f'Você perdeu! A palavra era "{palavra}".')
            break
