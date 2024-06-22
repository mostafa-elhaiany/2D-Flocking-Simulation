import pygame
from pygame import math
import random


class Boid:
    def __init__(self, x, y, radius = 3, perception_distance=30):
        self.position = math.Vector2(x, y)
        self.velocity = math.Vector2(random.random(),random.random())
        self.acceleration = math.Vector2()
        self.perception_distance = perception_distance
        self.radius = radius
        self.cohesion_weight = .6
        self.align_weight = .8
        self.separation_weight = .8
        self.random_weight = 0.05
        self.max_speed = 4
        self.max_force = 2

        self.prev_position = self.position
        self.prev_velocity = self.velocity

        self.locals = []
        self.color = math.Vector3(random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def draw(self, screen):
        for b in self.locals:
            b.color = self.color
        pygame.draw.circle(screen, self.color, self.position, self.radius)

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


    def optimized_update(self, boid_idx, boids):
        self.locals = []

        average_velocity = math.Vector2()
        avg_flock_position = math.Vector2()
        avg_repulsion_positon =  math.Vector2()

        num_local = 0
        for b_idx, boid in enumerate(boids):
            if(b_idx==boid_idx):
                continue
            distance = self.distance_to(boid)
            if(distance < self.perception_distance):
                self.locals.append(boid)
                avg_repulsion_positon += self.position - boid.prev_position
                avg_flock_position += boid.prev_position
                average_velocity += boid.prev_velocity
                num_local +=1
        if(num_local!=0):
            avg_repulsion_positon /= num_local
            avg_flock_position /= num_local
            average_velocity /= num_local

            align_velocity = (average_velocity.normalize() * self.max_speed - self.velocity).clamp_magnitude(self.max_force)
            separation_velocity = (avg_repulsion_positon.normalize() * self.max_speed - self.velocity).clamp_magnitude(self.max_force)
            cohesion_velocity = (((avg_flock_position - self.position).normalize() * self.max_speed) - self.velocity).clamp_magnitude(self.max_force)

            rx = random.random()*2 - 1
            ry = random.random()*2 - 1
            random_heading = math.Vector2(rx, ry)

            self.acceleration = align_velocity * self.align_weight + separation_velocity * self.separation_weight + cohesion_velocity * self.cohesion_weight + random_heading * self.random_weight

            self.velocity += self.acceleration 
            self.velocity = self.velocity.normalize() * self.max_speed
            self.position += self.velocity
        else:
            rx = random.random()*2 - 1
            ry = random.random()*2 - 1
            random_heading = math.Vector2(rx, ry)
            self.acceleration = random_heading * self.random_weight

            self.velocity += self.acceleration 
            self.velocity = self.velocity.normalize() * self.max_speed
            self.position += self.velocity
        

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
