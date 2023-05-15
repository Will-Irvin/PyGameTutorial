import pygame

if __name__ == '__main__':
    pygame.init()  # Initialize

    # Initialize display/surface, pixel dimensions must be given as a tuple
    gameDisplay = pygame.display.set_mode((800, 600))
    # Set title of the window
    pygame.display.set_caption('A bit Racey')

    clock = pygame.time.Clock()
    # Main loop to keep the program running, exits when user closes the window
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                crashed = True

        # Update only refreshes certain parts of the screen, display.flip() will update the entire thing
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
