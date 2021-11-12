# https://www.edureka.co/blog/snake-game-with-pygame/
import pygame
import numpy as np

import fiddlies


dis_x = 900
dis_y = 900
step = 100
x = dis_x // 2 - step // 2
y = dis_y // 2 - step // 2

pygame.init()
dis = pygame.display.set_mode((dis_x, dis_y))
pygame.draw.rect(dis, fiddlies.snake_colour, [x, y, step, step])
pygame.display.update()
pygame.display.set_caption("Kukik")

game_over = False
apple_exists = False
while not game_over:
    if not apple_exists:
        apple_x = x
        while apple_x == x and apple_x >= dis_x:
            # dis_x/step gives the number of apples that can fit on the display's width
            apple_x = step * int(dis_x/step * np.random.rand())
        apple_y = y
        while apple_y == y and apple_y >= dis_y:
            apple_y = step * int(dis_y/step * np.random.rand())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # some events are not keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= step
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += step
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += step
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= step

        if x >= dis_x or x < 0 or y >= dis_y or y < 0:
            game_over = True

        dis.fill(fiddlies.background_colour)
        pygame.draw.rect(dis, fiddlies.snake_colour, [x, y, step, step])
        pygame.draw.rect(dis, fiddlies.apple_colour, [apple_x, apple_y, step, step])
        pygame.display.update()

pygame.quit()
quit()
