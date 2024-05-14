import pygame
from personagens import Personagem

pygame.init()

#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Jogo das princesas")
tela.fill((80,120,200))

FUNDO = pygame.image.load("imagens/princesas_mundo.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#criando personagens

bela=Personagem("Imagens/bela.png",100,50,850,50)