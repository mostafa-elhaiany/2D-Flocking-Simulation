import sys
import pygame
import config
from Flock import Flock
# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode(config.SCREEN_DIMS)
pygame.display.set_caption("Boid Flocking")

flock = Flock(100)


def draw():
     # Fill screen with black
    screen.fill(config.BLACK)

    flock.draw(screen)

    # Update display
    pygame.display.flip()


def handle_event(event):
    pass

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            handle_event(event)
    draw()

    flock.update()

    clock.tick(60)
pygame.quit()
sys.exit()