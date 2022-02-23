# Basic pygame painting program
# Github: redneckvitor
import pygame
from pygame.locals import *


#files
icon = pygame.image.load('icon.png')

#Booleans
exit = False

#Colors
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
magenta = (255,0,255)
cyan = (0,255,255)
white = (255,255,255)
brush_color = black
screen_color = white

#Mouse position on screen
mouse_x, mouse_y = 0, 0

#Size of brush
brush_size = 1

#Surfaces
screen = pygame.display.set_mode((800,600), RESIZABLE)
canvas = pygame.Surface((2000,2000), pygame.SRCALPHA, 32)
canvas.convert_alpha()

pygame.display.set_caption("RDNCK Painting Program")
pygame.display.set_icon(icon)

pygame.init()

while not exit:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit = True

        #Keyboard pressed key event handler
        if event.type == KEYDOWN:

            if event.key == K_1:
                brush_color = red
            if event.key == K_2:
                brush_color = green
            if event.key == K_3:
                brush_color = blue
            if event.key == K_4:
                brush_color = cyan
            if event.key == K_5:
                brush_color = magenta
            if event.key == K_6:
                brush_color = yellow
            if event.key == K_7:
                brush_color = black
            if event.key == K_8:
                brush_color = white

            if event.key == K_x:
                screen_color = brush_color

            #Control brush size with UP and DOWN arrow keys
            if event.key == K_DOWN:
                brush_size -= 1
                if brush_size < 1:
                    brush_size = 1
            if event.key == K_UP:
                brush_size += 1
                if brush_size > 60:
                    brush_size = 60

            #Save image to a file
            if event.key == K_s:
                pygame.image.save(screen,'image.png')

    mouse_x, mouse_y = pygame.mouse.get_pos()

    #Handle mouse left click to draw on screen
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(canvas,(brush_color),(mouse_x , mouse_y), brush_size, 0)

    screen.fill(screen_color)
    screen.blit(canvas,(0,0))
    pygame.display.update()

pygame.quit()
