import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Rotate Rectangle')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create a rectangle surface
rect_width, rect_height = 200, 100
rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)  # Use SRCALPHA for transparency
rect_surface.fill((0, 0, 0, 0))  # Fill with transparent background
pygame.draw.rect(rect_surface, BLUE, (0, 0, rect_width, rect_height))  # Draw a blue rectangle

# Rotation angle
rotation_angle = 45  # Degrees

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Rotate the rectangle surface
    rotated_surface = pygame.transform.rotate(rect_surface, rotation_angle)

    # Calculate the position to blit the rotated rectangle
    rotated_rect = rotated_surface.get_rect(center=(screen_width // 2, screen_height // 2))

    # Draw the rotated rectangle onto the screen
    screen.blit(rotated_surface, rotated_rect.topleft)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
