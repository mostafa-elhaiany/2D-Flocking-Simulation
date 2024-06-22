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
    
    def update(self):
        for boid in self.boids:
            boid.update()
            boid.position.x %= config.SCREEN_WIDTH
            boid.position.y %= config.SCREEN_HEIGHT
