import pygame
import random
from math import *

pygame.init()

# draw surface params
animated_surface_size = animated_surface_width, animated_surface_height = (800, 800)  # DOIT TOUJOURS ETRE CARRE
animation_surface_padding = (20, 20, 20, 100)  # left top rigth bottom # va donner la taille en plus pour la fenetre
animation_surface_background_color = (200, 200, 200)

# window/background surface params
win_surface_color = (100, 100, 100)

win_size = win_width, win_height = (animated_surface_width+animation_surface_padding[0]+animation_surface_padding[2], animated_surface_height+animation_surface_padding[1]+animation_surface_padding[3])
win_surface = pygame.display.set_mode(win_size)


animation_surface_pos_rect = (animation_surface_padding[0], animation_surface_padding[1], animated_surface_width, animated_surface_height)
animation_surface = win_surface.subsurface(animation_surface_pos_rect)
animation_surface.fill(animation_surface_background_color)

print(animated_surface_width, animated_surface_height)

win_surface.fill(win_surface_color)
animation_surface.fill(animation_surface_background_color)
pygame.draw.circle(animation_surface, (255, 0, 0), (0, animated_surface_height), animated_surface_width, 2)

nb_points = 0
nb_points_in_arc = 0

def add_point():
    global nb_points, nb_points_in_arc
    x = random.random()
    y = random.random()
    distance_from_origin = sqrt(x**2+y**2)
    if distance_from_origin <=1:
        nb_points_in_arc +=1
    point_color = (50, 0, 150) if distance_from_origin <=1 else (150, 0, 50)

    nb_points += 1
    print(nb_points_in_arc/nb_points*4, nb_points)

    # pygame.draw.circle(animation_surface, point_color, (int(x*animated_surface_width), animated_surface_height-int(y*animated_surface_height)), 2)

run = True
while run:
    # *** EVENTS ***
    for event in pygame.event.get():
        event_type = event.type

        # end the loop if the game is closed
        if event_type == pygame.QUIT:
            run = False

    add_point()
    # pygame.display.flip()