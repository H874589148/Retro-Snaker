# -*- coding:utf-8 -*-
import pygame,sys,random
# 这个模块包含各种pygame所使用的常量
from pygame.locals import *

# 1.定义颜色变量
redColor = pygame.Color(255,0,0)
# 背景为黑色
blackColor = pygame.Color(0,0,0)
# 贪吃蛇为白色
whiteColor = pygame.Color(255,255,255)

# 2.定义游戏结束的函数
def gameover():
    pygame.quit()
    sys.exit()

# 3.定义main函数-->定义我们的入口函数
def main():
    # 3.1 初始化pygame
    pygame.init()
    # 3.2 定义一个变量来控制速度
    fpsClock = pygame.time.Clock()
    # 3.3 创建pygame显示层，创建一个界面
    playSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption('贪吃蛇')
    # 3.4 初始化变量
    # 初始化贪吃蛇的起始坐标位置
    snakePoosition = [100,100]
    # 初始化贪吃蛇的长度列表中有几个元素就代表有几段身体
    snakeBody =[[100,100],[80,100],[60,100]]
    # 初始化目标方块的位置
    targetPosition = [300,300]
    # 目标方块的标记 目的：判断是否吃掉 1 没吃 0 吃了
    targetflag = 1
    # 初始化方向
    direction = 'right'
    # 定义一个方向变量（人为控制）
    changeDirection = direction
    # 3.5 pygame中它的所有时间都是放在一个实时循环中完成的
    while True:
        # 从队列中获取事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection == 'right'
                if event.key == K_LEFT:
                    changeDirection == 'left'
                if event.key == K_UP:
                    changeDirection == 'up'
                if event.key == K_DOWN:
                    changeDirection == 'down'
                    # 对应键盘esc键
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

    # 3.6 确定方向
    if changeDirection == 'left' and not direction == 'right':
        direction = changeDirection
    if changeDirection == 'right' and not direction == 'left':
        direction = changeDirection
    if changeDirection == 'up' and not direction == 'down':
        direction = changeDirection
    if changeDirection == 'down' and not direction == 'up':
        direction = changeDirection
    # 3.7 根据方向移动蛇头
    if direction == 'right':
        snakePoosition[0] += 20
    if direction == 'left':
        snakePoosition[0] -= 20
    if direction == 'up':
        snakePoosition[1] -= 20
    if direction == 'down':
        snakePoosition[1] += 20
    # 3.8 增加蛇的长度
    snakeBody.insert(0,list(snakePoosition))
    # 如果我们的贪吃蛇的位置和目标方块的位置重合
    if snakePoosition[0] == targetPosition[0] and snakePoosition[0] == targetPosition[0]:
        targetflag = 0
    else:
        snakeBody.pop()

    if targetflag == 0:
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        targetPosition = [int(x*20),int(y*20)]
        targetflag = 1
    # 3.9 填充背景颜色
    playSurface.fill(blackColor)

# 4.更新到屏幕表面

# 5.启动入口函数