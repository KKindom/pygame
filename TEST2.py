import pygame,sys
#初始化
pygame.init()
#设置屏幕尺寸
size = width, height = 600, 400
#设置横向纵向速度 只识别整数，小数会四舍五入
speed = [1,1]
#设置背景颜色
BLACK = 0, 0, 0
#设置屏幕尺寸
screen = pygame.display.set_mode(size)
#加载图片
pygame.display.set_caption("Pygame壁球")
ball=pygame.image.load("PYG02-ball.gif")
#Pygame使用内部定义的Surface对象表示所有
# 载入的图像
ballrect = ball.get_rect()
fps=30
fclock=pygame.time.Clock()
while True:
    #事件队列中取出对队列
    for event in pygame.event.get():
        #处理事件
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
    #矩形移动一个偏移量
    ballrect = ballrect.move(speed[0], speed[1])
    #触壁反弹
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] =- speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] =-speed[1]
    #填充背景颜色
    screen.fill(BLACK)
    #绘制小球到图像ballrect上
    screen.blit(ball, ballrect)
    #刷新屏幕
    pygame.display.update()
    fclock.tick(fps)