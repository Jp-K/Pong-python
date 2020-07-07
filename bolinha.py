import pygame
from random import randint
b = (0,0,0)

class bolinha(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        # Definição da bolinha e suas propriedades
        self.image = pygame.Surface([width, height])
        self.image.fill(b)
        self.image.set_colorkey(b)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Declada a propriedade de velocidade em uma tupla para sua variação aleatória posteriormente
        self.velocity = [randint(4,8), randint(-8,8)]

        self.rect = self.image.get_rect()

    # Movimentação da bolinha
    def atualiza(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # Função da interação da bolinha com as tábuas    
    def quicar(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)