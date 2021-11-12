# RGB values
background_colour = (0, 0, 0)
text_colour = (175, 175, 175)

snake_colour = (150, 255, 70)
snake_border_colour = (50, 75, 50)
apple_colour = (255, 100, 50)
apple_border_colour = (75, 30, 30)

# sizes
dis_x = 900
dis_y = 800
step = 50
border_width = 8

# game speed
fps = 8

# checks:
if (dis_x%step, dis_y%step) != (0, 0):
    print("ugly grid:step ratio")

