import pygame
from pygame import math
import random


class Boid:
    def __init__(self, x, y, radius = 3, perception_distance=25):
        self.position = math.Vector2(x, y)
        self.velocity = math.Vector2(random.random(),random.random())
        self.acceleration = math.Vector2()
        self.perception_distance = perception_distance
        self.radius = radius
        self.cohesion_weight = .25
        self.align_weight = .3
        self.separation_weight = .7
        self.max_speed = 5

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)

    def distance_to(self, other):
        return self.position.distance_to(other.position)

    def separation(self,local_flock):
        avg = math.Vector2(0,0)
        if(len(local_flock)!=0):
            for boid in local_flock:
                difference = self.position - boid.position
                distance = self.distance_to(boid)
                if(distance!=0):
                    difference *= 1/(distance * distance)
                else:
                    difference *= 1/(distance+1e00001)
                avg += difference
            direction = ((avg/len(local_flock)) - self.velocity)
            if(direction.magnitude!=0):
                direction.normalize_ip()
            return direction

        else:
            return avg

    def cohesion(self,local_flock):
        avg = math.Vector2(0,0)
        if(len(local_flock)!=0):
            for boid in local_flock:
                avg += boid.position

            position_direction = ((avg/len(local_flock)) - self.position)

            direction = position_direction - self.velocity
            if(direction.magnitude!=0):
                direction.normalize_ip()
            return direction
        else:
            return avg

    def align(self, local_flock):
        avg = math.Vector2(0,0)
        if(len(local_flock)!=0):
            for boid in local_flock:
                avg += boid.velocity

            direction = ((avg/len(local_flock)) - self.velocity)
            if(direction.magnitude!=0):
                direction.normalize_ip()
            return direction 

        else:
            return avg


    def update(self, local_flock):

        align_velocity = self.align(local_flock)
        cohesion_velocity = self.cohesion(local_flock) 
        separation_velocity = self.separation(local_flock) 

        self.acceleration = self.align_weight * align_velocity + self.cohesion_weight * cohesion_velocity + self.separation_weight * separation_velocity


        rx = random.random()*2 - 1
        ry = random.random()*2 - 1
        self.acceleration += math.Vector2(rx, ry)

        self.velocity += self.acceleration 
        self.velocity = self.velocity.normalize() * self.max_speed
        self.position += self.velocity
