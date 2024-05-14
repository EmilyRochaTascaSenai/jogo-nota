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
bela= Personagem("imagens/bela.png",100,100,200,300)
#Criando um relogio para controlar o FPS
clock = pygame.time.Clock()
rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("voce clicou")
        if evento.type == pygame.QUIT:
            rodando = False
    tela.blit(FUNDO,(0,0))
    #desenhando as imagens
    bela.movimentar_via_controle(pygame.K_RIGHT,pygame.K_LEFT)
    bela.desenhar(tela)
    #configurando a fonte
    fonte=pygame.font.SysFont("arial black ",12)
    texto_pontucao_bela=fonte.render("Pontuação da bela",False,(255,203,219))
    tela.blit(texto_pontucao_bela,(0,0))
    #Atualizando a tela
    pygame.display.update()

    clock.tick(60)