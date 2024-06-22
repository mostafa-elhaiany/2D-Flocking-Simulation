import pygame
from pygame import math
import random


class Boid:
    def __init__(self, x, y, radius = 3, perception_distance=50, max_force=1):
        self.position = math.Vector2(x, y)
        self.velocity = math.Vector2(random.random(),random.random())
        self.acceleration = math.Vector2()
        self.perception_distance = perception_distance
        self.radius = radius
        self.max_force = max_force

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)

    def distance_to(self, other):
        return self.position.distance_to(other.position)

    def align(self, local_flock):
        avg = math.Vector2(0,0)
        if(len(local_flock)!=0):
            for boid in local_flock:
                avg += boid.velocity

            direction = ((avg/len(local_flock)) - self.velocity)
            if(direction.x!=0 or direction.y!=0):
                direction = direction.normalize() * self.max_force
            return direction
        else:
            return avg


    def update(self, local_flock):

        align_velocity = self.align(local_flock)

        self.acceleration = align_velocity

        self.velocity += self.acceleration 
        self.position += self.velocity
