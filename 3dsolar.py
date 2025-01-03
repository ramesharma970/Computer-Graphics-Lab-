import pygame
import sys
import math
from pygame.math import Vector3

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Solar System Simulation')

# Function to rotate a point around the y-axis
def rotate_point_y(point, angle):
    x, y, z = point
    new_x = x * math.cos(angle) - z * math.sin(angle)
    new_z = x * math.sin(angle) + z * math.cos(angle)
    return (new_x, y, new_z)

# Class for celestial bodies
class CelestialBody:
    def __init__(self, position, radius, color, orbit_radius, angular_speed):
        self.position = position  # Position as tuple (x, y, z)
        self.radius = radius
        self.color = color
        self.orbit_radius = orbit_radius
        self.angular_speed = angular_speed
        self.angle = 0

    def update(self):
        # Update angle for rotation around own axis
        self.angle += self.angular_speed

    def get_current_position(self):
        # Calculate position on orbit
        x = self.orbit_radius * math.cos(self.angle)
        z = self.orbit_radius * math.sin(self.angle)
        return (x, self.position[1], z)

    def draw(self):
        # Project 3D position to 2D screen coordinates (simple orthographic projection)
        x, y, z = self.get_current_position()
        projected_x = int(x) + SCREEN_WIDTH // 2
        projected_y = int(z) + SCREEN_HEIGHT // 2

        # Draw the body
        pygame.draw.circle(screen, self.color, (projected_x, projected_y), self.radius)

# Initialize celestial bodies
sun = CelestialBody(position=(0, 0, 0), radius=40, color=YELLOW, orbit_radius=0, angular_speed=0.01)
planet1 = CelestialBody(position=(200, 0, 0), radius=15, color=BLUE, orbit_radius=200, angular_speed=0.01)
planet2 = CelestialBody(position=(300, 0, 0), radius=20, color=RED, orbit_radius=300, angular_speed=0.008)
planet3 = CelestialBody(position=(400, 0, 0), radius=25, color=ORANGE, orbit_radius=400, angular_speed=0.005)

celestial_bodies = [sun, planet1, planet2, planet3]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update and draw celestial bodies
    for body in celestial_bodies:
        body.update()
        body.draw()

    # Rotate the sun around its own axis
    sun.position = rotate_point_y(sun.position, 0.01)

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
