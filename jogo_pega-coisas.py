import pygame


pygame.init()

#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Jogo das princesas")
tela.fill((80,120,200))

FUNDO = pygame.image.load("imagens/princesas_mundo.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

