import pygame
import sys

pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Area Filling Example")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Fill the background
screen.fill(WHITE)

# Define the rectangle coordinates and color
rect = pygame.Rect(100, 100, 200, 150)  # (x, y, width, height)
pygame.draw.rect(screen, RED, rect)

# Update the display
pygame.display.flip()

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
