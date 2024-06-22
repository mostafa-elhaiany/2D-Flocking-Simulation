import random
from Boid import Boid
import config 


class Flock:
    def __init__(self, num_boids):
        w = config.SCREEN_WIDTH
        h = config.SCREEN_HEIGHT
        self.boids = [
            Boid(random.random()*w, random.random()*h)
            for _ in range(num_boids)
        ]
    
    def draw(self, screen):
        for boid in self.boids:
            boid.draw(screen)
    
    def calculate_local_flock(self, boid: Boid, idx: int):
        perception_distance = boid.perception_distance
        local_flock = []
        for b_idx, other in enumerate(self.boids):
            if(b_idx==idx):
                continue
            distance = boid.distance_to(other)
            if(distance<perception_distance):
                local_flock.append(other)
        return local_flock

    def optimzied_update(self):
        for b_idx, boid in enumerate(self.boids):
            boid.optimized_update(b_idx, self.boids)

        for boid in self.boids:
            boid.position.x %= config.SCREEN_WIDTH
            boid.position.y %= config.SCREEN_HEIGHT
            boid.prev_pos = boid.position
            boid.prev_velocity = boid.velocity

    def update(self):
        for b_idx, boid in enumerate(self.boids):
            local = self.calculate_local_flock(boid, b_idx)
            boid.update(local)
            boid.position.x %= config.SCREEN_WIDTH
            boid.position.y %= config.SCREEN_HEIGHT

        
            

