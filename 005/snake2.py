import pygame
import sys
import time
import random


# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120


# Window size
display_size_x = 720
display_size_y = 480

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# score variable


# Initialise game window
pygame.display.set_caption('Eat food if you can...')
game_window = pygame.display.set_mode((display_size_x, display_size_y))


# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Game Over
def game_over(score):
    my_font = pygame.font.SysFont('open sans', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (display_size_x/2, display_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'open sans', 20, score)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_c:
                gameLoop()

# Score
def show_score(choice, color, font, size, score):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (display_size_x/10, 15)
    else:
        score_rect.midtop = (display_size_x/2, display_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


# Lives
def show_lives(choice, color, font, size, lives):
    lives_font = pygame.font.SysFont(font, size)
    lives_surface = lives_font.render('Lives : ' + str(lives), True, color)
    lives_rect = lives_surface.get_rect()
    if choice == 1:
        lives_rect.midtop = (display_size_x/2, 15)
    else:
        lives_rect.midtop = (display_size_x/10, display_size_y/1.25)
    game_window.blit(lives_surface, lives_rect)


# Show message
def message(msg, color):
    font_style = pygame.font.SysFont('consolas', 20)
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [display_size_x / 3, display_size_y / 8])


# Main logic
def gameLoop():
    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

    food_pos = [random.randrange(1, (display_size_x//10)) * 10, random.randrange(1, (display_size_y//10)) * 10]
    food_spawn = True

    direction = 'RIGHT'
    change_to = direction

    difficulty = 10
    score = 0
    lives = 3

    game_over = False
    game_pause = False

    while not game_over:
        print ('[+] gameLoop')

        while game_pause == True:
            my_font = pygame.font.SysFont('consolas', 90)
            game_over_surface = my_font.render('YOU DIED', True, red)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (display_size_x/2, display_size_y/4)
            game_window.fill(black)
            game_window.blit(game_over_surface, game_over_rect)
            show_score(0, red, 'consolas', 20, score)
            show_lives(0, red, 'consolas', 20, lives)
            message('Press C to continue or Q to quit', red)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            difficulty += 1
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (display_size_x//10)) * 10, random.randrange(1, (display_size_y//10)) * 10]
        food_spawn = True

        # GFX
        game_window.fill(black)
        for pos in snake_body:
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Snake food
        pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Game Over conditions
        # Getting out of bounds
        if snake_pos[0] < 0 or snake_pos[0] > display_size_x-10:
            lives -= 1
            game_pause = True
        if snake_pos[1] < 0 or snake_pos[1] > display_size_y-10:
            lives -= 1
            game_pause = True
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                lives -= 1
                game_pause = True

        show_score(1, white, 'consolas', 20, score)
        show_lives(1, white, 'consolas', 20, lives)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)

gameLoop()
