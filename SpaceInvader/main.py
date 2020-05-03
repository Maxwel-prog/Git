import pygame
import random
import math
from pygame import mixer
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Background

background = pygame.image.load("malaga.jpg")

# Background Sound
mixer.music.load('lobo_loco.mp3')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Segway Invaders")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("cool.png")
playerX = 370
playerY = 480
playerX_change = 0

# Lives
global lives_left
lives_left = 3

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("segway.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# Bullet
# Ready - you can't see the bullet on the screnn
# Fire  - the bullet is currently moving
bulletImg = pygame.image.load("banana.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 7
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('Moonhouse-yE5M.ttf', 32)

textX = 10
testY = 10

# Game Over text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

# Logo

logoImg = pygame.image.load("topsegway.png")
logoX = 15
logoY = 40


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        original_color = (0, 125, 200, 0)
        screen.fill(original_color)
        intro_text = font.render("welcome to TopGame", True, (255, 255, 0))
        screen.blit(intro_text, (200, 250))

        pygame.display.update()




def show_logo(x, y):
    screen.blit(logoImg, (logoX, logoY))


def show_score(x, y):
    score = font.render("TopSegway :" + str(score_value), True, (255, 255, 0))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = game_over_font.render("Try Again, beach", True, (255, 255, 0))
    screen.blit(over_text, (200, 250))



def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def game_over():
    for j in range(num_of_enemies):
        enemyY[j] = -2000
    pygame.mixer.music.fadeout(2000)
    game_over_text()
    over_Sound = mixer.Sound('wel.wav')
    over_Sound.play()






def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    # Movement
    # playerX += -0.1
    # playerY += -0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('piu4.wav')
                    bullet_Sound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 780
    elif playerX >= 780:
        playerX = 0

    # enemy movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 430:
            game_over()

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

            # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('auch.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #game_intro()
    player(playerX, playerY)
    show_score(textX, testY)
    show_logo(logoX, logoY)
    pygame.display.update()
