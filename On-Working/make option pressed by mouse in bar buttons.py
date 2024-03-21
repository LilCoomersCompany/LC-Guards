import pygame

# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((800, 600))

# Previous state of the left mouse button
previous_left_mouse_button_state = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current state of the left mouse button
    current_left_mouse_button_state = pygame.mouse.get_pressed()[0]

    # Check if the left mouse button was previously pressed and is now released
    if previous_left_mouse_button_state and not current_left_mouse_button_state:
        print("Left mouse button released")

        # Place your code here to execute when the left mouse button is released

    # Update the previous state of the left mouse button
    previous_left_mouse_button_state = current_left_mouse_button_state

    pygame.display.flip()

# Quit Pygame
pygame.quit()
