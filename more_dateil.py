import pygame
import sys
pygame.init()
pygame.display.set_caption("Pygame壁球")
ball=pygame.image.load("PYG02-ball.gif")
#Pygame使用内部定义的Surface对象表示所有
# 载入的图像
ballrect = ball.get_rect()
BLACK = 0, 0, 0
screen=pygame.display.set_mode((300,300),flags=pygame.NOFRAME)
pygame.display.set_caption("第一次pygame")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key,end='\t')
            print(event.mod)
            if event.key == pygame.K_ESCAPE:
                sys.exit()
                #获取鼠标的移动事件
        if event.type == pygame.MOUSEMOTION:
            print(event.buttons)

    #填充背景颜色
    screen.fill(BLACK)
    #绘制小球到图像ballrect上
    screen.blit(ball, ballrect)
    pygame.draw.rect(screen,(255,255,0),ballrect,2)
    pygame.display.update()