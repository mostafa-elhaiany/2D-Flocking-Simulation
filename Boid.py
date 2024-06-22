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
        self.max_speed = 4

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)

    def distance_to(self, other):
        return self.position.distance_to(other.position)

    def cohesion(self,local_flock):
        avg = math.Vector2(0,0)
        if(len(local_flock)!=0):
            for boid in local_flock:
                avg += boid.position

            position_direction = ((avg/len(local_flock)) - self.position)

            direction = position_direction - self.velocity
            if(direction.magnitude!=0):
                direction.normalize_ip()
            
            return direction * self.max_force
        else:
            return avg

    def align(self, local_flock):
        avg = math.Vector2(0,0)
        if(len(local_flock)!=0):
            for boid in local_flock:
                avg += boid.velocity

            direction = ((avg/len(local_flock)) - self.velocity)
            if(direction.x!=0 or direction.y!=0):
                direction = direction.normalize() 
            return direction * self.max_force
        else:
            return avg


    def update(self, local_flock):

        align_velocity = self.align(local_flock)
        cohesion_velocity = self.cohesion(local_flock)

        self.acceleration = align_velocity + cohesion_velocity

        self.velocity += self.acceleration 
        self.velocity = self.velocity.normalize() * self.max_speed
        self.position += self.velocity
