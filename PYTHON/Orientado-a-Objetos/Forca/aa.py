import pygame
import random

# Inicialização do Pygame
pygame.init()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da janela
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Forca")

# Configurações da fonte
fonte = pygame.font.Font(None, 36)

# Palavras para o jogo
palavras = ["PYTHON", "JAVA", "HTML", "CSS", "JAVASCRIPT", "RUBY", "PHP", "C++", "SWIFT"]
palavra_secreta = random.choice(palavras).upper()

# Inicialização de variáveis
letras_certas = set()
letras_erradas = set()
MAX_TENTATIVAS = 6

# Função para reiniciar o jogo
def reiniciar_jogo():
    global palavra_secreta, letras_certas, letras_erradas
    palavra_secreta = random.choice(palavras).upper()
    letras_certas = set()
    letras_erradas = set()

# Função para desenhar a tela de derrota
def tela_derrota():
    win.fill(WHITE)
    texto_derrota = fonte.render('Você perdeu! A palavra era: ' + palavra_secreta, True, BLACK)
    win.blit(texto_derrota, (100, 100))
    pygame.display.flip()
    pygame.time.delay(3000)  # Espera 3 segundos antes de fechar a janela
    reiniciar_jogo()

# Função para desenhar a tela de vitória
def tela_vitoria():
    win.fill(WHITE)
    texto_vitoria = fonte.render('Parabéns! Você venceu!', True, BLACK)
    win.blit(texto_vitoria, (100, 100))
    pygame.display.flip()
    pygame.time.delay(3000)  # Espera 3 segundos antes de fechar a janela
    reiniciar_jogo()

# Loop principal do jogo
clock = pygame.time.Clock()
terminado = False

while not terminado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminado = True
        elif event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                letra = chr(event.key).upper()
                if letra not in letras_certas and letra not in letras_erradas:
                    if letra in palavra_secreta:
                        letras_certas.add(letra)
                    else:
                        letras_erradas.add(letra)

    # Verifica se o jogador venceu
    venceu = all(letra in letras_certas for letra in palavra_secreta)

    # Verifica se o jogador perdeu
    perdeu = len(letras_erradas) >= MAX_TENTATIVAS

    # Limpa a tela
    win.fill(WHITE)

    # Desenha a palavra oculta
    palavra_oculta = ''.join([letra if letra in letras_certas else '_' for letra in palavra_secreta])
    texto_palavra = fonte.render(palavra_oculta, True, BLACK)
    win.blit(texto_palavra, (100, 100))

    # Desenha as letras erradas
    texto_erradas = fonte.render('Letras erradas: ' + ', '.join(letras_erradas), True, BLACK)
    win.blit(texto_erradas, (100, 200))

    # Desenha a forca
    pygame.draw.line(win, BLACK, (400, 400), (400, 100), 5)  # Poste
    pygame.draw.line(win, BLACK, (400, 100), (600, 100), 5)  # Barra superior
    pygame.draw.line(win, BLACK, (600, 100), (600, 150), 5)  # Corda
    if len(letras_erradas) > 0:
        pygame.draw.circle(win, BLACK, (600, 200), 25, 2)  # Cabeça
    if len(letras_erradas) > 1:
        pygame.draw.line(win, BLACK, (600, 225), (600, 300), 2)  # Tronco
    if len(letras_erradas) > 2:
        pygame.draw.line(win, BLACK, (600, 250), (550, 225), 2)  # Braço esquerdo
    if len(letras_erradas) > 3:
        pygame.draw.line(win, BLACK, (600, 250), (650, 225), 2)  # Braço direito
    if len(letras_erradas) > 4:
        pygame.draw.line(win, BLACK, (600, 300), (550, 350), 2)  # Perna esquerda
    if len(letras_erradas) > 5:
        pygame.draw.line(win, BLACK, (600, 300), (650, 350), 2)  # Perna direita

    # Atualiza a tela
    pygame.display.flip()

    # Verifica condições de vitória ou derrota
    if venceu:
        tela_vitoria()
    elif perdeu:
        tela_derrota()

    clock.tick(30)  # 30 FPS

# Encerra o Pygame
pygame.quit()
