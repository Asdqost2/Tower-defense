import pygame
from random import randint

maxfps = 60
window_SIZE = (800, 600)



class Sprite:
    def __init__(self, center, image):
        self.image = image
        self.rect = image.get_frect()
        self.rect.center = center
        
    def render(self, surface):
        surface.blit(self.image, self.rect)

class MoveSprite(Sprite):
    def __init__(self, center, image, speed, direction):
        super().__init__(center, image)
        self.speed = speed
        self.direction = direction

    def update(self):
        vector = self.direction * self.speed
        self.rect.move_ip(vector)

window = pygame.Window("Tower Defense", window_SIZE)
surface = window.get_surface()
clock = pygame.Clock()

player_image = pygame.Surface([50, 50])
player = Sprite([window_SIZE[0]/2, window_SIZE[1]/2], player_image)

bullets = []
enemies = []

running = True
while running:
    #обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            center = pygame.Vector2(player.rect.center)
            pos = pygame.Vector2(pygame.mouse.get_pos())
            vector = (pos - center).normalize()
            img = pygame.Surface([10, 10])
            img.fill("blue")
            bullet = MoveSprite(center, img, 7, vector)
            bullets.append(bullet)

    #обновление объектов
    if randint(0, 100) <= 5:
        center = pygame.Vector2(player.rect.center)
        pos = pygame.Vector2(0, 0)
        vector = (center - pos).normalize()
        img = pygame.Surface([50, 50])
        img.fill("red")
        enemy = MoveSprite(pos, img, 7, vector)
        enemies.append(enemy)
        
    for bullet in bullets:
        bullet.update()

    for enemy in enemies:
        enemy.update()

    #отрисовка
    surface.fill("green")

    for bullet in bullets:
        bullet.render(surface)
    for enemy in enemies:
        enemy.render(surface)
    player.render(surface)

    window.flip()
    clock.tick(maxfps)
