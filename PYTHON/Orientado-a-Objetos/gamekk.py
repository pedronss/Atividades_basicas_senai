import pygame
import sys
import random
import math
class Player:
    def __init__(self):
        self.x=50
        self.y=50
        self.velocidade = 3
    def moveright(self,velocity):
        if self.x < 1280-largura_retangulo:
            self.x+=0.4*velocity
    def moveleft(self,velocity):
        if self.x > 0:
            self.x-=0.4*velocity
    def moveup(self,velocity):
        if self.y >0:
            self.y-=0.4*velocity
    def movedown(self,velocity):
        if self.y < 720-altura_retangulo:
            self.y+=0.4*velocity
player=Player()
class Enemy:
    def __init__(self):
        self.x= random.randint(0,1270)
        self.y= random.randint(0,710)
        self.velocidade = 1.2
    def move_towards_player(self, player_x, player_y):
        # Calcula a direção em relação ao jogador
        dx, dy = player_x - self.x, player_y - self.y
        distance = math.hypot(dx, dy)
        if distance > 0:
            dx /= distance
            dy /= distance
        # Move o inimigo na direção do jogador
        self.x += dx * self.velocidade
        self.y += dy * self.velocidade
enemy= Enemy()
enemy.altura=20
enemy.largura=20
class Apple:
    def __init__(self) :
        self.x= random.randint(0,1270)
        self.y=random.randint(0,710)
    def aparecer(self):
        self.x= random.randint(0,1270)
        self.y=random.randint(0,710)
apple = Apple()
apple.largura=10
apple.altura=10
pygame.init()
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo Pygame")
branco = (255, 255, 255)
preto = (0, 0, 0)
red= (255, 0, 0)
pontos=0
fonte = pygame.font.Font(None, 50)
largura_retangulo, altura_retangulo = 20, 20
executando = True
enemyy=False 
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_w]:
        player.moveup(player.velocidade)
        up=True
    if tecla[pygame.K_s]:
        player.movedown(player.velocidade)
        down=True
    if tecla[pygame.K_a]:
        player.moveleft(player.velocidade)
        left=True
    if tecla[pygame.K_d]:
        player.moveright(player.velocidade)
        right=True
    tela.fill(branco)
    x, y = player.x, player.y
    pygame.draw.rect(tela, red, (enemy.x, enemy.y, enemy.largura, enemy.altura))
    if x == 800 and y==600:
        pass
    else:
        pygame.draw.rect(tela, preto, (x, y, largura_retangulo, altura_retangulo))
    
    if x < apple.x + apple.largura and x + largura_retangulo > apple.x and y < apple.y + apple.altura and y + altura_retangulo > apple.y:
        apple.aparecer()
        largura_retangulo+=5
        altura_retangulo +=5
        pontos+=1
    if x < enemy.x + enemy.largura and x + largura_retangulo > enemy.x and y < enemy.y + enemy.altura and y + altura_retangulo > enemy.y:
        break
    else:
        enemy.move_towards_player(player.x, player.y)
    pygame.draw.rect(tela, preto, (apple.x, apple.y, apple.largura, apple.altura))
    
    texto_superficie = fonte.render(str(pontos), True, preto)
    tela.blit(texto_superficie, (365,0))
    pygame.display.flip()
pygame.quit()
sys.exit()
