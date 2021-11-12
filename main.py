# https://www.edureka.co/blog/snake-game-with-pygame/
import pygame
import numpy as np

import fiddlies


def reposition_apple(passed_array):
    X = passed_array[0]
    Y = passed_array[1]

    x = X
    while x == Y or x >= dis_x:
        # dis_x/step gives the number of apples that can fit on the display's width
        x = step * int(dis_x / step * np.random.rand())
    y = Y
    while y == Y or y >= dis_y:
        y = step * int(dis_y / step * np.random.rand())
    return x, y


dis_x = fiddlies.dis_x
dis_y = fiddlies.dis_y
step = fiddlies.step
head = np.array([dis_x // 2 - step // 2, dis_y // 2 - step // 2])

pygame.init()
dis = pygame.display.set_mode((dis_x, dis_y))
pygame.draw.rect(dis, fiddlies.snake_colour, [head[0], head[1], step, step])
pygame.display.update()
pygame.display.set_caption("Kukik")
clock = pygame.time.Clock()

snek = np.array([head])
direction = np.array([0, 0], dtype=int)

game_over = False
apple_exists = False

t = 0

while not game_over:
    if not apple_exists:
        apple = reposition_apple(head)
        apple_exists = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # some events are not keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                direction[0] = 0
                direction[1] = -1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                direction[0] = 1
                direction[1] = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                direction[0] = 0
                direction[1] = 1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                direction[0] = -1
                direction[1] = 0

    t += clock.tick()
    if t >= fiddlies.ticks_per_frame:

        head += step*direction
        if head[0] >= dis_x or head[0] < 0 or head[1] >= dis_y or head[1] < 0:
            game_over = True
        elif head[0] == apple[0] and head[1] == apple[1]:
            snek = np.append(np.array([head]), snek, axis=0)
        else:
            snek = np.append(np.array([head]), snek[:-1], axis=0)

        dis.fill(fiddlies.background_colour)
        for chunk in snek:
            pygame.draw.rect(dis, fiddlies.snake_colour, [chunk[0], chunk[1], step, step])
        pygame.draw.rect(dis, fiddlies.apple_colour, [apple[0], apple[1], step, step])
        pygame.display.update()
        t = 0

pygame.quit()
quit()
