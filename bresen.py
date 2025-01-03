import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's Line Algorithm")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a line using Bresenham's algorithm
def draw_line_Bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy / dx

    x, y = x1, y1
    screen.set_at((x, y), WHITE)  # Set initial pixel

    if slope <= 1:
        p = 2 * dy - dx
        while x != x2:
            x += 1
            if p < 0:
                p += 2 * dy
            else:
                y += 1 if y1 < y2 else -1
                p += 2 * (dy - dx)
            screen.set_at((x, y), WHITE)  # Set pixel along the line
    else:
        p = 2 * dx - dy
        while y != y2:
            y += 1 if y1 < y2 else -1
            if p < 0:
                p += 2 * dx
            else:
                x += 1
                p += 2 * (dx - dy)
            screen.set_at((x, y), WHITE)  # Set pixel along the line

# Main loop
def main():
    start_pos = (100, 100)
    end_pos = (700, 500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_line_Bresenham(*start_pos, *end_pos)
        pygame.display.flip()

if __name__ == "__main__":
    main()
