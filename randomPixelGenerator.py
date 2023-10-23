import random
import pygame

# Initialize Pygame
pygame.init()

# Set the window size and title
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Random Colored Pixels')

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # # Clear the screen
    # screen.fill((0, 0, 0))
    # Generate random x and y coordinates for the pixel
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    # Generate random color values for the red, green, and blue components
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Draw the pixel at the random coordinates with the random color
    pygame.draw.rect(screen, (r, g, b), (x, y, 1, 1))
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
