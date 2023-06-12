import pygame

pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")


image = pygame.image.load("/Users/vihan/Desktop/5 apps/minion.gif")
screen.blit(image, (200,50))
background = pygame.Surface('white')

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
