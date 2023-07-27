import pygame
from pygame.locals import *

exit = False

black = (0, 0, 0)
red = (230, 59, 59)
green = (70, 240, 70)
blue = (52, 52, 223)
brush_color = (200, 200, 200)
screen_color = (15, 15, 15)

mouse_x, mouse_y = 0, 0

brush_size = 1

screen = pygame.display.set_mode((600, 800), RESIZABLE)
canvas = pygame.Surface((2000, 2000), pygame.SRCALPHA, 32)
canvas.convert_alpha()

pygame.display.set_caption("RDNCK Paint")
pygame.display.set_icon(pygame.image.load('icon.png'))

pygame.init()

while not exit:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit = True

        # TODO: switch case aqui
        if event.type == KEYDOWN:
            if event.key == K_1:
                brush_color = red
            if event.key == K_2:
                brush_color = green
            if event.key == K_3:
                brush_color = blue
            if event.key == K_4:
                brush_color = (200, 200, 200)

            # Control brush size with UP and DOWN arrow keys
            if event.key == K_DOWN:
                brush_size -= 1
                if brush_size < 1:
                    brush_size = 1
            if event.key == K_UP:
                brush_size += 1
                if brush_size > 60:
                    brush_size = 60

            if event.key == K_s:
                pygame.image.save(screen, 'image.png')

    mouse_x, mouse_y = pygame.mouse.get_pos()

    isPainting = pygame.mouse.get_pressed()[0]
    isErasing = pygame.mouse.get_pressed()[2]

    if isPainting:
        pygame.draw.circle(canvas, brush_color, (mouse_x, mouse_y), brush_size, 0)
    if isErasing:
        pygame.draw.circle(canvas, screen_color, (mouse_x, mouse_y), brush_size, 0)

    screen.fill(screen_color)
    screen.blit(canvas, (0, 0))
    pygame.display.update()

pygame.quit()
