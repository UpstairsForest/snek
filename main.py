# https://www.edureka.co/blog/snake-game-with-pygame/
import pygame
import numpy as np

import fiddlies


def reposition_apple(passed_snek):
    X = passed_snek[0, 0]
    Y = passed_snek[0, 1]

    x = X
    y = Y
    while x >= dis_x or y >= dis_y or ([x, y] == passed_snek).all(1).any():
        x = step * int(dis_x / step * np.random.rand())
        y = step * int(dis_y / step * np.random.rand())
    return x, y


dis_x = fiddlies.dis_x
dis_y = fiddlies.dis_y
step = fiddlies.step
bw = fiddlies.border_width
head = step * ((np.array([int(dis_x/2), int(dis_y/2)])) // step)
print(head/step)

pygame.init()
dis = pygame.display.set_mode((dis_x, dis_y))

pygame.draw.rect(dis, fiddlies.snake_colour, [head[0]+bw, head[1]+bw, step-2*bw, step-2*bw])
pygame.draw.rect(dis, fiddlies.snake_border_colour, [head[0], head[1], step, step],
                             width=bw, border_radius=5)
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
        apple = reposition_apple(snek)
        apple_exists = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and not (direction == [0, 1]).all():
                direction[0] = 0
                direction[1] = -1
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and not (direction == [-1, 0]).all():
                direction[0] = 1
                direction[1] = 0
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and not (direction == [0, -1]).all():
                direction[0] = 0
                direction[1] = 1
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and not (direction == [1, 0]).all():
                direction[0] = -1
                direction[1] = 0

    t += clock.tick()
    if t >= fiddlies.ticks_per_frame:

        head += step*direction
        if head[0] >= dis_x or head[0] < 0 or head[1] >= dis_y or head[1] < 0:
            game_over = True
        elif head[0] == apple[0] and head[1] == apple[1]:
            snek = np.append(np.array([head]), snek, axis=0)
            apple = reposition_apple(snek)
        else:
            snek = np.append(np.array([head]), snek[:-1], axis=0)

        dis.fill(fiddlies.background_colour)
        pygame.draw.rect(dis, fiddlies.apple_colour, [apple[0]+bw, apple[1]+bw, step-2*bw, step-2*bw])
        pygame.draw.rect(dis, fiddlies.apple_border_colour, [apple[0], apple[1], step, step],
                         width=bw, border_radius=5)
        for chunk in snek:
            pygame.draw.rect(dis, fiddlies.snake_colour, [chunk[0]+bw, chunk[1]+bw, step-2*bw, step-2*bw])
            pygame.draw.rect(dis, fiddlies.snake_border_colour, [chunk[0], chunk[1], step, step],
                             width=bw, border_radius=5)
        pygame.display.update()
        t = 0

pygame.quit()
quit()
