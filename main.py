import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solor System Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

class Planet:
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        #WIN.fill()
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

main()
