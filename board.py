import numpy as np
import pygame
import time
import random


pygame.init()

grid_size = (10, 10)

board_size = (int(grid_size[1]*40), int(grid_size[0]*40))

board_state = np.zeros((grid_size))

starting_pos = random.randint(0, grid_size[0]*grid_size[1])

if starting_pos == 0:
    starting_pos_coord = (0, 0)
    print(starting_pos_coord)

else:
    starting_pos_coord = (starting_pos // grid_size[1], starting_pos % grid_size[0])

board_state[starting_pos_coord[0]][starting_pos_coord[1]] = 1

print(starting_pos)

print(starting_pos_coord)

print(board_state)

GRAY=(211,211,211)

font = pygame.font.SysFont("comicsansms", 18)

screen = pygame.display.set_mode((grid_size[1]*40, grid_size[0]*40))

for y in range(grid_size[0]):
    for x in range(grid_size[1]):
        rect = pygame.Rect(x*(board_size[0]/grid_size[1]), y*(board_size[1]/grid_size[0]), (board_size[0]/grid_size[1]) - 1,
                           (board_size[1]/grid_size[1]) - 1)
        pygame.draw.rect(screen, GRAY, rect)
        if (y, x) == starting_pos_coord:
            text = font.render(str(int(board_state[starting_pos_coord[0]][starting_pos_coord[1]])), True, (0, 128, 0))
            screen.blit(text, (x*(board_size[0]/grid_size[1]) + (board_size[0]/grid_size[1])/3, y*(board_size[1]/grid_size[0])))

done = False

starting_time = time.time()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

    if time.time() - starting_time > 1:
        starting_time = time.time()
        screen.fill(pygame.Color("black"))
        board_state[starting_pos_coord[0]][starting_pos_coord[1]] += 1
        for y in range(grid_size[0]):
            for x in range(grid_size[1]):
                rect = pygame.Rect(x * (board_size[0] / grid_size[1]), y * (board_size[1] / grid_size[0]),
                                   (board_size[0] / grid_size[1]) - 1,
                                   (board_size[1] / grid_size[1]) - 1)
                pygame.draw.rect(screen, GRAY, rect)
                if (y, x) == starting_pos_coord:
                    text = font.render(str(int(board_state[starting_pos_coord[0]][starting_pos_coord[1]])), True,
                                       (0, 128, 0))
                    screen.blit(text, (x * (board_size[0] / grid_size[1]) + (board_size[0] / grid_size[1]) / 3,
                                       y * (board_size[1] / grid_size[0])))

    pygame.display.flip()

