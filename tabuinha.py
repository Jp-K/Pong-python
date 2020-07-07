import pygame
b = (0,0,0)

class tabuinha(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        # Definição da classe tábua e suas propriedades
        self.image = pygame.Surface([width, height])
        self.image.fill(b)
        self.image.set_colorkey(b)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    # Função de movimentação continua
    def MoveUP(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
            self.rect.y = 0

    def MoveDOWN(self, pixels):
        self.rect.y += pixels

        if self.rect.y > 400:
            self.rect.y = 400