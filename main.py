# https://www.edureka.co/blog/snake-game-with-pygame/
import pygame

import fiddlies


dis_x = 900
dis_y = 900
x = dis_x//2
y = dis_y//2

pygame.init()
dis = pygame.display.set_mode((dis_x, dis_y))
pygame.draw.rect(dis, fiddlies.snake_colour, [x, y, 10, 10])
pygame.display.update()
pygame.display.set_caption("Kukik")

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # some events are not keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= 10
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += 10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += 10
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= 10
        dis.fill(fiddlies.background_colour)
        pygame.draw.rect(dis, fiddlies.snake_colour, [x, y, 10, 10])
        pygame.display.update()

pygame.quit()
quit()
