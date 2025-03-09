import pygame
import random
pygame.init()

# SCREEN SHIT
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
white = (255, 255, 255)
pygame.display.set_caption("Pong")
fps = 60
clock = pygame.time.Clock()
border_thickness = 10
border_color = (0, 0, 0)

# OBJECTS
rect_1x, rect_1y = 750, 250
rect_1w, rect_1h = 15, 80
rect_2x, rect_2y = 35, 250
rect_2w, rect_2h = 15, 80

ball_x, ball_y = WIDTH / 2, HEIGHT / 2
ball_w, ball_h = 15, 15
ball_vel_x = 5 * random.choice((1, -1))  
ball_vel_y = 5 * random.choice((1, -1))

# Movement flags
move_up_1 = move_down_1 = False
move_up_2 = move_down_2 = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_up_2 = True
            if event.key == pygame.K_s:
                move_down_2 = True
            if event.key == pygame.K_UP:
                move_up_1 = True
            if event.key == pygame.K_DOWN:
                move_down_1 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_up_2 = False
            if event.key == pygame.K_s:
                move_down_2 = False
            if event.key == pygame.K_UP:
                move_up_1 = False
            if event.key == pygame.K_DOWN:
                move_down_1 = False

    
    WIDTH, HEIGHT = pygame.display.get_surface().get_size()

    
    if move_up_2 and rect_2y > border_thickness:
        rect_2y -= 11
    if move_down_2 and rect_2y + rect_2h < HEIGHT - border_thickness:
        rect_2y += 11
    if move_up_1 and rect_1y > border_thickness:
        rect_1y -= 11
    if move_down_1 and rect_1y + rect_1h < HEIGHT - border_thickness:
        rect_1y += 11

    
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    
    if ball_y <= border_thickness or ball_y + ball_h >= HEIGHT - border_thickness:
        ball_vel_y *= -1  

    
    if (rect_2x < ball_x < rect_2x + rect_2w and
        rect_2y < ball_y +ball_h and ball_y < rect_2y + rect_2h):
        ball_vel_x *= -1  

    if (rect_1x < ball_x + ball_w < rect_1x + rect_1w and
        rect_1y < ball_y + ball_h and ball_y < rect_1y + rect_1h):
        ball_vel_x *= -1  

    
    if ball_x < 0 or ball_x > WIDTH:
        ball_x, ball_y = WIDTH / 2, HEIGHT / 2
        ball_vel_x = 5 * random.choice((1, -1))  
        ball_vel_y = 5 * random.choice((1, -1))

    
    screen.fill(white)

    # Borders
    pygame.draw.rect(screen, border_color, (-5, -5, WIDTH + 10, border_thickness))
    pygame.draw.rect(screen, border_color, (-5, HEIGHT - border_thickness + 5, WIDTH + 10, border_thickness))
    pygame.draw.rect(screen, border_color, (-5, -5, border_thickness, HEIGHT + 10))
    pygame.draw.rect(screen, border_color, (WIDTH - border_thickness + 5, -5, border_thickness, HEIGHT + 10))

    # Paddles and Ball
    pygame.draw.rect(screen, (0, 0, 0), (rect_1x, rect_1y, rect_1w, rect_1h))
    pygame.draw.rect(screen, (0, 0, 0), (rect_2x, rect_2y, rect_2w, rect_2h))
    pygame.draw.rect(screen, (0, 0, 0), (ball_x, ball_y, ball_w, ball_h))

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
