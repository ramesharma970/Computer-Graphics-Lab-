import pygame
import sys

def boundary_fill(surface, x, y, fill_color, boundary_color):
    """Fills an area bounded by boundary_color with fill_color with visual feedback."""
    width, height = surface.get_size()
    pixels = pygame.surfarray.pixels3d(surface)
    current_color = pixels[x, y]
    
    if (pixels[x, y] == boundary_color).all() or (pixels[x, y] == fill_color).all():
        return
    
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if (0 <= cx < width and 0 <= cy < height and
                (pixels[cx, cy] == current_color).all() and
                not (pixels[cx, cy] == boundary_color).all() and
                not (pixels[cx, cy] == fill_color).all()):
            pixels[cx, cy] = fill_color
            pygame.display.flip()  # Update display to show the fill process
            pygame.time.delay(10)  # Delay to make the fill process visible
            
            # Push adjacent pixels onto the stack
            stack.append((cx + 1, cy))
            stack.append((cx - 1, cy))
            stack.append((cx, cy + 1))
            stack.append((cx, cy - 1))

pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Boundary Fill Example")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fill the background
screen.fill(WHITE)

# Draw a boundary
pygame.draw.rect(screen, BLACK, (100, 100, 300, 200), 3)  # Boundary rectangle

# Update the display to show the initial state
pygame.display.flip()

# Perform boundary fill with visual feedback
boundary_fill(screen, 150, 150, RED, BLACK)

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
