import pygame
from pygame import math
import random


class Boid:
    def __init__(self, x, y, radius = 3):
        self.position = math.Vector2(x, y)
        self.velocity = math.Vector2(random.random(),random.random())
        self.acceleration = math.Vector2()
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)


    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration 
