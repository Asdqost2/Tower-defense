import pygame


class Sprite:
    def __init__(self, center, image):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = center

    def render(self, surface):
        surface.blit(self.image, self.rect)


window = pygame.Window("Товер Дефенс", (800, 600))
surface = window.get_surface()
clock = pygame.Clock()
running = True

while running:
    # 1.обработка событий
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
    # 2. обновление объектов
    # 3. отрисовка
    surface.fill("green")
    window.flip()
    clock.tick(60)
    print(clock.get_fps())
