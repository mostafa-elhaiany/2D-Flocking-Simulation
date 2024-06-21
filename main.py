import sys
import pygame
import config

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode(config.SCREEN_DIMS)
pygame.display.set_caption("Boid Flocking")



def draw():
     # Fill screen with black
    screen.fill(config.BLACK)

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

    clock.tick(60)
pygame.quit()
sys.exit()