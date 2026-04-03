import pygame
import random
import math

screen_width = 900
screen_height = 700

player_start_x = 420
player_start_y = 560
enemy_speed_x = 2
enemy_speed_y = 30
bullet_speed = 5
collision_distance = 27
num_enemies = 6

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

pygame.mixer.music.load("bg music.mp3")
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Minecraft Shooting Game")

clock = pygame.time.Clock()
background = pygame.image.load("minecraft_Background.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

player_img = pygame.image.load("Steve_minecraft.jpg")
player_img = pygame.transform.scale(player_img, (64, 64))
player_x = player_start_x
player_y = player_start_y
player_x_change = 0

enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

for i in range(num_enemies):
    img = pygame.image.load("zombie.jpg")
    img = pygame.transform.scale(img, (64, 64))
    enemy_img.append(img)
    enemy_x.append(random.randint(0, screen_width - 64))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

bullet_img = pygame.image.load("bulletno_bg.png")
bullet_img = pygame.transform.scale(bullet_img, (32, 32))

bullet_x = 0
bullet_y = player_start_y
bullet_y_change = bullet_speed
bullet_state = "ready"

score_value = 0
font      = pygame.font.Font("freesansbold.ttf", 32)
over_font = pygame.font.Font("freesansbold.ttf", 64)

text_x = 10
text_y = 10

gameover_played = False

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (screen_width // 2 - 180, screen_height // 2 - 32))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(ex, ey, bx, by):
    return math.sqrt((ex - bx) ** 2 + (ey - by) ** 2) < collision_distance

running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -6
            if event.key == pygame.K_RIGHT:
                player_x_change = 6
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                bullet_y = player_y
                shoot_sound.play()          # 🔊 shoot
                fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change
    player_x = max(0, min(player_x, screen_width - 64))

    for i in range(num_enemies):
        if enemy_y[i] > 600:
            for j in range(num_enemies):
                enemy_y[j] = 2000
            game_over_text()
            if not gameover_played:
                gameover_sound.play()       # 🔊 game over
                gameover_played = True
            running = False
            break

        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] <= 0 or enemy_x[i] >= screen_width - 64:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]

        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)

        if collision:
            bullet_y = player_start_y
            bullet_state = "ready"
            score_value += 1
            hit_sound.play()                # 🔊 hit
            enemy_x[i] = random.randint(0, screen_width - 64)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    if bullet_y <= 0:
        bullet_y = player_start_y
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    show_score(text_x, text_y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()