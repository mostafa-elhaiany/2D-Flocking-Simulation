import random
from Boid import Boid
import config 


class Flock:
    """
    Class to simulate a set of boids in the same flock
    Can create multiple flocks that do not affect each other
    """
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
        """
        calculates the list of local boids for each boid
        """
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
        """
        instead of finding the local flock in a loop then looping over the rules everything happens in the same loop
        """
        for b_idx, boid in enumerate(self.boids):
            boid.optimized_update(b_idx, self.boids)

        for boid in self.boids: # updates position after boids have edited their velocity 
            boid.position.x %= config.SCREEN_WIDTH
            boid.position.y %= config.SCREEN_HEIGHT
            boid.prev_position = boid.position
            boid.prev_velocity = boid.velocity

    def update(self):
        """
        Calculates the local flock for each boid then uses that to calculate each force seperately before using it to change position
        """
        for b_idx, boid in enumerate(self.boids):
            local = self.calculate_local_flock(boid, b_idx)
            boid.update(local)
            boid.position.x %= config.SCREEN_WIDTH
            boid.position.y %= config.SCREEN_HEIGHT

        
            

