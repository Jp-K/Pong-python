import pygame
import time
from tabuinha import tabuinha
from bolinha import bolinha

b = (0,0,0)
w = (255,255,255)   # Define a tupla com as cores que serão usadas durante o game
r = (255, 0, 0)

pygame.init()       # Inicia o pygame

# Definição das propriedades da tela
tam_tela = (700, 500)  
tela = pygame.display.set_mode(tam_tela)
pygame.display.set_caption("PONG")

# Definiição das propriedades do tabua 1
jogador1 = tabuinha(w, 10, 100)
jogador1.rect.x = 20
jogador1.rect.y = 200

# Definição das propriedades do jogador da tabua 2
jogador2 = tabuinha(w, 10, 100)
jogador2.rect.x = 670
jogador2.rect.y = 200

# Definição das propriedades do jogador da bola
bola = bolinha(r, 10, 10)
bola.rect.x = 350
bola.rect.y = 250

# Inicializa todos os sprites e os adiciona para a tela
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(jogador1)
all_sprites_list.add(jogador2)
all_sprites_list.add(bola)

on = True
clock = pygame.time.Clock() # Definição do clock

# Propriedades do titulo do menu principal
titleFont = pygame.font.SysFont("Arial", 45)
menuTitle = titleFont.render("PONG", True, w)

# Propriedades de fonte e textos das opções do menu principal
startFont = pygame.font.SysFont("Arial", 22)
startText = startFont.render("(LeftMouseButton) Começa o jogo", True, w)
returnText = startFont.render("(BackSpace) Volta ao menu durante o jogo", True, w)
intrucText = startFont.render("(i) Abre as instruções", True, w)
exitText = startFont.render("(x) Fecha o jogo", True, w)

# Inicializa todos as pontuações dos jogadores em 0
pontosA = 0
pontosB = 0

# Verificador do menu principal
menuVerf = True

# Função que mostra a informações do menu Instrução
def instrucMenu(fonteT, fonteI):
    text1 = fonteT.render("INSTRUÇÕES", True, w)
    text2 = fonteI.render("O jogador 1 controla a tabua da direita com os comandos UP, DOWN", True, w)
    text3 = fonteI.render("O jogador 2 controla a tabua da esquerda com os comandos W, S", True, w)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    tela.fill(b)
    tela.blit(text1, (200, 70))
    tela.blit(text2, (25, 200))
    tela.blit(text3, (25, 250))

    clock.tick(60)
    pygame.display.update()
    time.sleep(5)

# Função do menu principal
def menu(verf):

    while verf:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    verf = False
                    return verf
            elif pygame.key.get_pressed()[pygame.K_x]: # Caso X seja pressionado o jogo fecha
                quit()
            
            elif pygame.key.get_pressed()[pygame.K_i]: # Caso I seja pressionado o menu de instrtuções é apresentado
                instrucMenu(titleFont, startFont)

        # Faz a renderização dos textos do menu principal
        tela.fill(b)
        tela.blit(menuTitle, (280, 70))
        tela.blit(startText, (25, 200))
        tela.blit(returnText, (25, 250))
        tela.blit(intrucText, (25, 300))
        tela.blit(exitText, (25, 350))

        clock.tick(60)
        pygame.display.update()

# Função que verfifica e imprime a vitória de um dos jogador
def winCondition(pontoA, pontoB, fonteT):

    texto = fonteT.render("Jogador 1 venceu!", True, w)
    texto2 = fonteT.render("Jogador 2 venceu!", True, w)

    if pontosA == 10:

        tela.fill(b)
        tela.blit(texto, (150, 150))
        pygame.display.update()
        time.sleep(3)
        return True # Retorna ao menu após a vitória
    
    elif pontosB == 10:
        tela.fill(b)
        tela.blit(texto2, (150, 150))
        pygame.display.update()
        time.sleep(3)
        return True # Retorna ao menu após a vitória

# Loop principal do jogo
while on:

    # Chama o menu principal
    if menuVerf == True:
        menuVerf = menu(menuVerf)

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           on = False

    #Lógica para a movimentação contínua dos jogadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jogador1.MoveUP(5)
    if keys[pygame.K_s]:
        jogador1.MoveDOWN(5)
    if keys[pygame.K_UP]:
        jogador2.MoveUP(5)
    if keys[pygame.K_DOWN]:
        jogador2.MoveDOWN(5)
    
    # Volta para o menu caso pressionado e zera o progresso do jogo
    if keys[pygame.K_BACKSPACE]:
        menuVerf = True
        pontosA = 0
        pontosB = 0
        bola.rect.x = 350
        bola.rect.y = 250

    bola.atualiza()
    all_sprites_list.update()

    # Chama o verificador de vitória independente do vitorioso
    if pontosA or pontosB == 10:
        menuVerf = winCondition(pontosA, pontosB, titleFont)

        # Zera a pontuação e Posiciona todos os sprites em suas posições originais
        if menuVerf:
            pontosA = 0
            pontosB = 0
            jogador1.rect.x = 20
            jogador1.rect.y = 200
            jogador2.rect.x = 670
            jogador2.rect.y = 200
            bola.rect.x = 350
            bola.rect.y = 250

    # Marcaão de pontos para ambos jogadores
    if bola.rect.x >= 690:
        pontosA += 1

        bola.rect.x = 350
        bola.rect.y = 250
        time.sleep(1.5)

        bola.velocity[0] = -bola.velocity[0]

    if bola.rect.x <= 0:
        pontosB += 1

        bola.rect.x = 350
        bola.rect.y = 250
        time.sleep(1.5)

        bola.velocity[0] = -bola.velocity[0]

    # Colisão com as paredes da tela    
    if bola.rect.y > 490:
        bola.velocity[1] = -bola.velocity[1]
    if bola.rect.y < 0:
        bola.velocity[1] = -bola.velocity[1] 

    # Colisão com as tábuas
    if pygame.sprite.collide_mask(bola, jogador1) or pygame.sprite.collide_mask(bola, jogador2):
        bola.quicar()

    # Redesenha todos os sprites
    tela.fill(b)
    pygame.draw.line(tela, w, [349, 0], [349, 500], 5)
    all_sprites_list.draw(tela)

    # Definição e Render do placar
    font = pygame.font.Font(None, 74)
    text = font.render(str(pontosA), 1, w)
    tela.blit(text, (250, 10))
    
    text = font.render(str(pontosB), 1, w)
    tela.blit(text, (420, 10))

    # Atualização da tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()