import sys
import pygame
import config
from Flock import Flock
# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode(config.SCREEN_DIMS)
pygame.display.set_caption("Boid Flocking")

flocks = [
    Flock(100),
    Flock(100),
    Flock(100),
]


def draw():
     # Fill screen with black
    screen.fill(config.BLACK)
    
    for flock in flocks:
        flock.draw(screen)

    # Update display
    pygame.display.flip()


running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()

    for flock in flocks:
        flock.optimzied_update()


    clock.tick(60)
pygame.quit()
sys.exit()