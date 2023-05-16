import pygame

if __name__ == '__main__':
    pygame.init()  # Initialize

    # Initialize display/surface, pixel dimensions must be given as a tuple
    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    # Set title of the window
    pygame.display.set_caption('A bit Racey')

    # Define colors w/ RGB
    black = (0, 0, 0)
    white = (255, 255, 255)

    clock = pygame.time.Clock()
    # Main loop to keep the program running, exits when user closes the window
    crashed = False
    car_image = pygame.image.load('images/racecar.png')
    finish_line_img = pygame.image.load('images/finish_line.png')

    # Draw the car image to the screen
    def car(x, y):
        gameDisplay.blit(finish_line_img, (x - 65, y - 200))
        gameDisplay.blit(car_image, (x,y))


    x = display_width * .45
    y = display_height * .8

    while not crashed:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                crashed = True

        # If this order was flipped the car would be filled over
        gameDisplay.fill(white)
        car(x, y)

        # Update only refreshes certain parts of the screen, display.flip() will update the entire thing
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
