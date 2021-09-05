import random
import pygame

# Init pygame

pygame.init()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)

# define game board width and height
width, height = 400, 400
game_display = pygame.display.set_mode((width, height))

pygame.display.set_caption("Snake_Game")  # Game Name

clock = pygame.time.Clock()

# Snake size and speed
snake_size = 10
snake_speed = 12

# font for message and score
message_font = pygame.font.SysFont('ubuntu', 15)
score_font = pygame.font.SysFont('ubuntu', 25)


def print_score(score):  # Define function for score computation
    text = score_font.render("Score:" + str(score), True, orange)
    game_display.blit(text, [0, 0])


def draw_snake(snake_size, snake_pixels):  # Define function for snake
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])


def run_game():  # Define function to run game
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0  # snake target
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0  # snake target

    # Loops and conditions for game (game over , replay game , quit game)
    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over! Press 1 for play 2 for quit ", True, white)
            game_display.blit(game_over_message, [width / 3, height / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():  # define Keys for game replay or quit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP2 or event.key == pygame.K_2:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_KP1 or event.key == pygame.K_1:
                        run_game()

                elif event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():  # define keys for game play
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                elif event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)  # game display background
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])  # snake length in pixels
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


run_game()
