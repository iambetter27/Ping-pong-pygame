from random import randint
import pygame
import time
pygame.init()

# Creates variable for clock

clock = pygame.time.Clock()
tick_counter = 0

# Variables for player 1 and player 2
player_1_score = 0
player_2_score = 0

# Creating the screen
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title of the window
pygame.display.set_caption("Ping-Pong Game: First to 7 wins!")

# Creating rectangle n1
rectangles_length = 250
rectangles_width = 25
rectangles_vel = 3

rectangle_right_x = SCREEN_WIDTH - rectangles_width
rectangle_right_y = 250
rectangle_right = pygame.Rect(rectangle_right_x, rectangle_right_y, rectangles_width, rectangles_length)

# Creating rectangle n2
rectangle_left_x = 0
rectangle_left_y = 250
rectangle_left = pygame.Rect(rectangle_left_x, rectangle_left_y, rectangles_width, rectangles_length)

# Creating border up and border down
border_up = pygame.Rect(0, 60, SCREEN_WIDTH, 10)
border_down = pygame.Rect(0, 680, SCREEN_WIDTH, 10)
border_right = pygame.Rect(SCREEN_WIDTH - rectangles_width - 5, 70, 5, 610)
border_left = pygame.Rect(rectangles_width, 70, 5, 610)

# Creating ball
ping_pong_ball_x = 650
ping_pong_ball_y = 340
ping_pong_ball_side = 75
ping_pong_ball = pygame.Rect(ping_pong_ball_x, ping_pong_ball_y, ping_pong_ball_side, ping_pong_ball_side)
ping_pong_ball_vel_num = 2
ping_pong_ball_vel = [ping_pong_ball_vel_num, -ping_pong_ball_vel_num]
ping_pong_ball_x_vel = ping_pong_ball_vel[randint(0, 1)]
ping_pong_ball_y_vel = ping_pong_ball_vel[randint(0, 1)]
ping_pong_ball_speed_count = 0

# Detectors to detect if the ball passes the line
detector_right = pygame.Rect(SCREEN_WIDTH - rectangles_width + 2, 70, 1, 610)
detector_left = pygame.Rect(rectangles_width - 3, 70, 1, 610)

# Function to display text on the screen
text_font = pygame.font.SysFont("Arial", 40)
title_font = pygame.font.SysFont("Arial", 70)


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


# Creating image to start(i'm not using it)
'''
start_image_x = 450
start_image_y = 333
start_image = pygame.image.load('images/press_space_to_start.png')
start_image_rect = pygame.Rect(start_image_x, start_image_y, start_image.get_width(), start_image.get_height())
'''

# Defining statement for press_space_to_start
statement_start = False
statement_finish = False


def restart():
    global ping_pong_ball_speed_count, rectangles_vel, statement_start, ping_pong_ball_x, ping_pong_ball_y,\
        ping_pong_ball_x_vel, ping_pong_ball_y_vel
    ping_pong_ball_speed_count = 0
    rectangles_vel = 3
    statement_start = False
    ping_pong_ball.x = 650
    ping_pong_ball.y = 340
    ping_pong_ball_x_vel = ping_pong_ball_vel[randint(0, 1)]
    ping_pong_ball_y_vel = ping_pong_ball_vel[randint(0, 1)]


####################### TIME ############################

# Sets timer count
timer = 0

# Delta Time
previous_time = time.time()
dt = 0

fps = 120
target_fps = 120

run = True

while run:

    # Refreshes the back of the screen
    screen.fill((0, 0, 0))

    # Title of window for winner if score of a player equals 7
    if player_1_score == 7:
        pygame.display.set_caption("Player 1 wins!")
        draw_text("Player 1 wins!", title_font, (255, 255, 255), 500, 240)
        statement_finish = True
    if player_2_score == 7:
        pygame.display.set_caption("Player 2 wins!")
        draw_text("Player 2 wins!", title_font, (255, 255, 255), 500, 240)
        statement_finish = True

    # Display the players, rectangles, borders, detectors, image and text
    pygame.draw.rect(screen, (255, 255, 255), border_up)
    pygame.draw.rect(screen, (255, 255, 255), border_down)
    pygame.draw.rect(screen, (255, 255, 255), border_right)
    pygame.draw.rect(screen, (255, 255, 255), border_left)

    pygame.draw.rect(screen, (255, 255, 255), rectangle_left)
    pygame.draw.rect(screen, (255, 255, 255), rectangle_right)

    pygame.draw.rect(screen, (0, 255, 0), detector_right)
    pygame.draw.rect(screen, (0, 255, 0), detector_left)

    pygame.draw.rect(screen, (255, 255, 255), ping_pong_ball, width=0, border_radius=75)
    draw_text("Player 1: " + str(player_1_score) + " vs Player 2: " + str(player_2_score), text_font,
              (255, 255, 255), 480, 7)
    if statement_start is False and statement_finish is False:
        # Display text for press start
        draw_text("Press space to Start", title_font, (255, 255, 255), 400, 240)
        # Displaying the image (i'm not using it)
        "screen.blit(start_image, (start_image_x, start_image_y))"

    if statement_start:
        ping_pong_ball.x += ping_pong_ball_x_vel * dt * target_fps
        ping_pong_ball.y += ping_pong_ball_y_vel * dt * target_fps
    
    # Collisions with ping-pong ball on the borders
    if ping_pong_ball.colliderect(border_up) or ping_pong_ball.colliderect(border_down):
        ping_pong_ball_y_vel *= -1
        # Get the ball out of the object
        ping_pong_ball.y += ping_pong_ball_y_vel * dt * target_fps

    # Collisions with ping-pong ball on the rectangles
    if ping_pong_ball.colliderect(rectangle_left) or ping_pong_ball.colliderect(rectangle_right):
        ping_pong_ball_x_vel *= -1
        ping_pong_ball_speed_count += 1
        if ping_pong_ball_speed_count == 5:
            ping_pong_ball_x_vel *= 1.5
            ping_pong_ball_y_vel *= 1.5
            rectangles_vel *= 1.2
            ping_pong_ball_speed_count = 0
        # Get the ball out of the object
        ping_pong_ball.x += ping_pong_ball_x_vel * dt * target_fps

    # When someone scores
    if ping_pong_ball.colliderect(detector_left) and not ping_pong_ball.colliderect(rectangle_left):
        player_2_score += 1
        restart()

    if ping_pong_ball.colliderect(detector_right) and not ping_pong_ball.colliderect(rectangle_right):
        player_1_score += 1
        restart()


####################### Events ###############################

# Creating variable for all key events
    key = pygame.key.get_pressed()

    # Movement of the rectangles
    if statement_start:
        if key[pygame.K_UP] and rectangle_right.y > 70:
            rectangle_right.y -= rectangles_vel * dt * target_fps
        if key[pygame.K_DOWN] and rectangle_right.y < 680 - rectangles_length:
            rectangle_right.y += rectangles_vel * dt * target_fps
        if key[pygame.K_w] and rectangle_left.y > 70:
            rectangle_left.y -= rectangles_vel * dt * target_fps
        if key[pygame.K_s] and rectangle_left.y < 680 - rectangles_length:
            rectangle_left.y += rectangles_vel * dt * target_fps


    # Events in the game
    current_event = pygame.event.get()

    for event in current_event:
        if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
            run = False
        if event.type == pygame.KEYDOWN:
            # Event to start the game
            if event.key == pygame.K_SPACE and statement_finish is False:
                statement_start = True

 ############### TIME ##################

    # Tick of the game
    clock.tick(fps)

    # Delta Time
    now = time.time()
    dt = now - previous_time
    previous_time = now

    # Number of FPS
    display_fps = round(clock.get_fps())

    # Timer to count time
    if statement_finish is False:
        timer += dt
        
    draw_text("FPS: " + str(display_fps), text_font, (255, 255, 255), 20, 7)
    draw_text("Time: " + str(round(timer, 3)), text_font, (255, 255, 255), 1100, 7)
    
    # Updating the process
    pygame.display.update()

pygame.quit()
