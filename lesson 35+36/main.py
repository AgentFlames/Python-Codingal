import math 
import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_X_START= 370
PLAYER_Y_START = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40 
BULLET_SPEED_Y = 10 
COLLISON_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load('lesson 35+36/space bg.png')
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
playerImg = pygame.image.load('spaceship.png')
playerX = PLAYER_X_START
playery = PLAYER_Y_START
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies): 
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SCREEN_WIDTH-64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_Y_START
bulletX_change = 0
bullet_change = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.Fond('freesansbold.ttf', 32)
textX = 10
testY = 10 

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y): 
    score = font.render("Score : "+str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def game_over_text(): 
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))

def player(x,y): 
    screen.blit(playerImg, (x,y))

def enemy(x,y,i): 
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y): 
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY): 
    distance = math.sqrt((enemyX-bulletX)**2+(enemyY - bulletY)**2)
    return distance < COLLISON_DISTANCE


