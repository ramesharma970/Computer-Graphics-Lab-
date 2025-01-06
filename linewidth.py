import pygame

# Initialize Pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Define colors
WHITE = (255, 255, 255)

# Set circle parameters
center = (400, 300)  # Center of the circle (x, y)
radius = 100  # Radius of the circle
line_width = 10  # Border thickness of the circle

# Draw a circle with specified thickness
pygame.draw.circle(screen, WHITE, center, radius, line_width)

# Update the display
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
