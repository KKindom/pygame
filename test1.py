import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((300,300))
pygame.display.set_caption("第一次pygame")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()