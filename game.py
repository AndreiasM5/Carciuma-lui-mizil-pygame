import pygame
from random import randint

pygame.init()

# variabile ecran
screen_width = 1024
screen_height = 768
display_output = [screen_width, screen_height]
screen = pygame.display.set_mode(display_output)
pygame.display.set_caption("Carciuma_lui_Mizil") # TITLE
carciuma = pygame.image.load('carciuma1.png')
clock = pygame.time.Clock()

#ICON
mizil = pygame.image.load('mizil.png')
pygame.display.set_icon(mizil)

# variabile scor
score = 0 #SCORE
text_x = 15
text_y = 720

# font
font = pygame.font.Font('BACKTO1982.ttf', 40)

# variabile health
health = 3
health_x = 753
health_y = 720

#Sound
tick = pygame.mixer.Sound("tick.wav")
tick.set_volume(0.4)
song = pygame.mixer.Sound("za_song.mp3")
song.play(-1)
ras = pygame.mixer.Sound("ras.mp3")
ras.play(-1)
ras.set_volume(0)

#variabile meniu
meniu = pygame.image.load('meniu.png')
GAME_OVER = pygame.image.load('GAME_OVER.png')
red = (203, 38, 42)
centru = (0, 0)
game = 0 #seteaza harta


# variabile pahar vin
pahar_width = 132
pahar_pos_x = 450
pahar_pos_y = 600
pahar_y_line = pahar_pos_y + 17
pahar_x_start_co = pahar_pos_x + 40
pahar_x_end_co = pahar_pos_x + 85
pahar_speed_x = 15
present_pahar_speed_x = 0

# variabile strop vin
strop_size = 100
strop_position_x = 50
strop_position_y = 50
strop_x_co = strop_position_x + 50
strop_y_co = strop_position_y + 50
speed_dir_x = 0
speed_dir_y = 5
gravity=0.02

play_game = True

def update_stop_pos():
    global strop_x_co, strop_y_co, pahar_pos_x, strop_position_y, speed_dir_y, gravity
    strop_x_co = strop_position_x + 50
    strop_y_co = strop_position_y + 50
    pahar_pos_x += present_pahar_speed_x
    strop_position_y += int(speed_dir_y)
    speed_dir_y += (speed_dir_y * gravity)

def check_for_event():
    global play_game, present_pahar_speed_x, game, health
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        play_game=0
        health=-1
    if keys[pygame.K_ESCAPE]:
        game=0
        health=-1
    if keys[pygame.K_LEFT]:
        present_pahar_speed_x = - pahar_speed_x
    elif keys[pygame.K_RIGHT]:
        present_pahar_speed_x = pahar_speed_x
    else:
        present_pahar_speed_x = 0

def check_for_strop_in_pahar():
    global score, health
    if strop_y_co in range(pahar_y_line-(int(speed_dir_y)//2), pahar_y_line+(int(speed_dir_y)//2)):
        if strop_x_co in range(pahar_x_start_co-1, pahar_x_end_co+1):
            if(score % 10 == 0):
                health +=1
            score += 1
            tick.play()
        else:
            health -= 1

def display_carciuma():
    global centru
    screen.blit(carciuma, centru)

def display_strop(pos_x, pos_y):
    screen.blit(strop, (pos_x, pos_y))
    update_stop_pos()

def display_pahar(pos_x, pos_y):
    screen.blit(pahar, (pos_x, pos_y))

def display():
    display_carciuma()
    display_strop(strop_position_x, strop_position_y)
    display_pahar(pahar_pos_x, pahar_pos_y)

def random_strop_initialise(): #when strop hits the border
    global strop_position_y, strop_position_x, speed_dir_y
    if strop_position_y > (screen_height + strop_size):
        speed_dir_y = 2
        strop_position_x = randint(0, 924)
        strop_position_y = 0

def enforce_border():
    global pahar_pos_x
    if pahar_pos_x > (screen_width-pahar_width):
        pahar_pos_x = screen_width-pahar_width
    if pahar_pos_x < 0:
        pahar_pos_x = 0

def display_score():
    global text_x, text_y, score
    score_disp = font.render("Scor : " + str(score), True, red)
    screen.blit(score_disp, (text_x, text_y))

def display_health():
    global health_x, health_x, health
    health_disp = font.render("Lifes : " + str(health), True, red)
    screen.blit(health_disp, (health_x, health_y))

def update_pahar_score_region():
    global pahar_x_start_co, pahar_x_end_co
    pahar_x_start_co = pahar_pos_x + 40
    pahar_x_end_co = pahar_pos_x + 85

def display_meniu():
    global centru
    screen.blit(meniu, centru)

def first_game():
    global carciuma, strop, pahar
    carciuma = pygame.image.load('carciuma_cu_vin.jpeg')
    strop = pygame.image.load('strop_vin.png')
    pahar = pygame.image.load('paharvin.png')

def second_game():
    global carciuma, strop, pahar
    carciuma = pygame.image.load('carciuma_cu_bere.jpeg')
    strop = pygame.image.load('strop_bere.png')
    pahar = pygame.image.load('halba.png')

def choose_carciuma():
    global play_game, game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        play_game = 0
        game = 3
    if keys[pygame.K_1]:
        game = 1
    elif keys[pygame.K_2]:
        game = 2

def game_over():
    global health, centru
    screen.blit(GAME_OVER, centru)

while play_game:
    clock.tick(60)
    pygame.display.flip()
    song.set_volume(0.2)
    ras.set_volume(0)
    while game == 0:
        health = 3
        score = 0
        display_meniu()
        choose_carciuma()
        clock.tick(60)
        pygame.display.flip()
        if game == 1:
            first_game()
        elif game == 2:
            second_game()
    display()
    update_pahar_score_region()
    random_strop_initialise()
    enforce_border()
    check_for_event()
    check_for_strop_in_pahar()
    display_score()
    display_health()
    while health == 0:
        clock.tick(60)
        pygame.display.flip()
        game_over()
        song.set_volume(0)
        ras.set_volume(0.1)
        check_for_event()

pygame.quit()
