import pygame

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
carImg = pygame.image.load('images/racecar.png')

black = (0, 0, 0)
white = (255, 255, 255)

def game_loop():
    car_x = (display_width * 0.45)
    car_y = (display_height * 0.8)
    photo_x = (display_width * 0.375)
    photo_y = (display_height * 0.5)
    x_change = 0
    car_speed = 0

    finish_line_img = pygame.image.load('images/finish_line.png')

    car_width = 73  # Used to know the location of both sides of the car
    car_height = 73

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            # Set up movement of the car, adjust variables depending on which keys are pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    car_speed = -5
                elif event.key == pygame.K_DOWN:
                    car_speed = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    car_speed = 0

        # Change the car's position based on its speed
        car_x += x_change
        car_y += car_speed

        gameDisplay.fill(white)
        gameDisplay.blit(finish_line_img, (photo_x, photo_y))
        car(car_x, car_y)

        if car_x > display_width - car_width or car_x < 0 or car_y < 0 or car_y + car_height > display_height:
            gameExit = True

        pygame.display.update()
        clock.tick(60)

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption('A bit Racey')

    clock = pygame.time.Clock()

    game_loop()

    pygame.quit()
