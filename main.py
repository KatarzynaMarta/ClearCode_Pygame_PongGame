import random

import pygame, sys


def ball_animation():
    global ball_speed_x, ball_speed_y,opponent_score,player_score
    # Moving ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # Edge of screen
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score+=1
        ball_start()
    if ball.right >= screen_width:
        opponent_score+=1
        ball_start()
    # Collision with ball
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation(player):
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top <= ball.y:
        opponent.y += opponent_speed
    if opponent.bottom >= ball.y:
        opponent.bottom -= opponent_speed


def ball_start():
    global  ball_speed_x,ball_speed_y
    ball.center = (screen_width / 2), (screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


# General setup
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

# Game Screen
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game from ClearCode v1")
# Colors
GREY12 = pygame.Color('grey12')
LIGHT_GREY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Text variables
player_score=0
opponent_score=0
game_font=pygame.font.Font("freesansbold.ttf",32)

# Creating rectangles
ball = pygame.Rect(screen_width / 2, screen_height / 2, 30, 30)
player = pygame.Rect(screen_width / 2, screen_height / 2, 20, 140)
opponent = pygame.Rect(screen_width / 2, screen_height / 2, 20, 140)
# my coordinates
ball.center = (screen_width / 2), (screen_height / 2)
player.center = (screen_width), (screen_height / 2)
opponent.center = 0, (screen_height / 2)

# speed of ball horizontal and vertical
speed_value = 7

ball_speed_x = speed_value*random.choice((1, -1))
ball_speed_y = speed_value

player_speed = 0

opponent_speed = speed_value

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += speed_value
            if event.key == pygame.K_UP:
                player_speed -=speed_value
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed += speed_value
            if event.key == pygame.K_UP:
                player_speed -= speed_value

    # ball animation function
    ball_animation()
    player.y += player_speed

    player_animation(player)
    player_animation(opponent)

    opponent_ai()


    # Visuals
    screen.fill(GREY12)
    pygame.draw.aaline(screen, LIGHT_GREY, (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, GREEN, opponent)
    pygame.draw.ellipse(screen, RED, ball)
    # Text
    player_text=game_font.render(f"{player_score}",False,LIGHT_GREY)
    screen.blit(player_text,((screen_width//2)+10,(screen_height/2)))
    opponent_text = game_font.render(f"{opponent_score}", False, LIGHT_GREY)
    screen.blit(opponent_text, ((screen_width// 2) - 20, (screen_height / 2)))
    # Updating window
    pygame.display.flip()
    clock.tick(60)