import random
import sys
import pygame

pygame.init()

SIZE = 2
ROW = 260
COL = 450
MARGIN = 1
COLOR_LIVE = (255, 255, 255)
COLOR_DEAD = (80, 80, 80)

arr = [[0] * COL for i in range(ROW)]
arr[random.randint(0, ROW)][random.randint(0, COL)] = 1

size = (COL * SIZE + (COL + 1), ROW * SIZE + (ROW + 1))
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game field')

for row in range(ROW):
    for col in range(COL):
        if arr[row][col]:
            color = COLOR_LIVE
        else:
            color = COLOR_DEAD
        pygame.draw.rect(screen, color,
                         (col * SIZE + MARGIN * (col + 1), row * SIZE + MARGIN * (row + 1), SIZE, SIZE))

while True:

    for row in ROW:
        for col in COL:
            if arr[row-1][col-1] + arr[row][col-1] + arr[row+1][col-1] + arr[row-1][col] + arr[row+1][col] + arr[row-1][col+1] + arr[row][col+1] + arr[row+1][col+1] == 3:
                arr[row][col] = 1
            if arr[row-1][col-1] + arr[row][col-1] + arr[row+1][col-1] + arr[row-1][col] + arr[row+1][col] + arr[row-1][col+1] + arr[row][col+1] + arr[row+1][col+1] == 3:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.display.update()

"""
elif event.type == pygame.MOUSEBUTTONDOWN:
    x_mouse, y_mouse = pygame.mouse.get_pos()
    column = x_mouse // (SIZE + MARGIN)
    row = y_mouse // (SIZE + MARGIN)
    arr[row][column] ^= 1

"""
