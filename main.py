import pygame
import time
from snakeGame import *

pygame.init()

width = 500
height = 500
screen_size = (width, height)
game = pygame.display.set_mode(screen_size)
game =  pygame.display.get_active()
pygame.display.set_caption('Snake game')
white = (255, 255, 255)
black = (0, 0, 0)

snake = Snake()

game_over = False
clock = pygame.time.Clock()

snake.draw()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
        if event.type == pygame.KEYDOWN:
            game_over = snake.move(event)
            clock.tick(30)
            print(f'After moving: {snake}')
        pygame.display.update()

