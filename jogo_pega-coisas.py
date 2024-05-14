import pygame
from personagens import Personagem

pygame.init()

#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Jogo das princesas")
tela.fill((80,120,200))

#criando imagens
FUNDO=pygame.image.load("Imagens/princesas_mundo.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#criando personagem
bela=jogador1 = Personagem("imagens/bela.png",100,50,150,0)


rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False

