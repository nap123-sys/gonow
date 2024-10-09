import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('3D Game')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a simple 3D-like object (a cube)
    # For simplicity, we are just drawing a 2D representation
    color = (255, 0, 0)
    points = [(400, 300), (450, 350), (400, 400), (350, 350)]
    pygame.draw.polygon(screen, color, points)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()