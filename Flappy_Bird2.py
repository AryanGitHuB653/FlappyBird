
import pygame
import random
from pygame import mixer_music
import time
pygame.init()

pygame.display.set_caption('FLAPPY BIRDS!')
background = pygame.image.load('background.png')
screen2 = pygame.display.set_mode((288,512))
base = pygame.image.load('base.png')
icon = pygame.image.load('fblogo.jpeg')
pygame.display.set_icon(icon)
info = pygame.image.load('info_screen.jpg')

# game_over_screen = pygame.image.load('gameover.png')
#bird


def welcome():
    loop = True
    screen_welcome = pygame.display.set_mode((957,649))
    while loop:
        screen_welcome.blit(info,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_loop()
            
        pygame.display.update()










def main_loop():
    screen = pygame.display.set_mode((288,512))
    x = 100
    y = 300
    jump = 0
    speed =  2
    birdimg = pygame.image.load('bird.png') 
    def draw_bird(x,y):
        screen.blit(birdimg, (x,y))




    speed_of_game = 0.5

    #pipes
    pipeupimg = pygame.image.load('pipe-up.png')
    pipedownimg = pygame.image.load('pipe-down.png')
    pipe1 = [300,-170]
    pipe2 = [550,-100]
    Pipes = []
    Pipes.append(pipe1)
    Pipes.append(pipe2)

    def draw_pipe(PIPE):
        screen.blit(pipeupimg, (PIPE[0], PIPE[1]))
        screen.blit(pipedownimg, (PIPE[0], PIPE[1]+420))

    #score
    score = 0
    font = pygame.font.Font('freesansbold.ttf',32)
    sCord = (10,20)
    def print_score(scr):
        screen.blit(font.render('Score'+str(scr), True, (255,0,0)),sCord)


    #sounds
    dieSound = pygame.mixer.Sound('die.wav')
    hitSound = pygame.mixer.Sound('hit.wav')
    swooshSound = pygame.mixer.Sound('swoosh.wav')
    pointSound = pygame.mixer.Sound('point.wav')
    wingSound = pygame.mixer.Sound('wing.wav')
    running = True
    while running:   
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    wingSound.play()
                    jump = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jump = 0

        #bird movement
        draw_bird(x,y)
        if jump==1:
            y-=2    
        else:
            y+=speed
        
        #pipe-movement
        for i in Pipes:
            draw_pipe(i)
            i[0]-=speed_of_game
            if i[0]<=0:
                i[0] = 500
                i[1]= random.randint(-250,-100)

        #game-over
        for i in Pipes:
            if i[0]==100:
                if y<=i[1]+330 or y>=i[1]+430:
                    hitSound.play()
                    dieSound.play()
                    screen2.blit(background,(0,0))
                    # screen.fill((0,0,0))
                    running=False
                    game_over()
                else:
                    pointSound.play()
                    score+=1
                    print(score)

        print_score(score)
        screen.blit(base ,(0,410))
        pygame.display.update()  



def game_over():
    go = True
    game_over_screen = pygame.display.set_mode((957,540))
    over = pygame.image.load('gameover.jpg')
    while go:
        game_over_screen.blit(over, (0,0))
        for event in pygame.event.get():
            # text_screen('Your Final Score in the game was')
            if event.type == pygame.QUIT:
                go=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    main_loop()
                if event.key == pygame.K_q:
                    go=False
            
        pygame.display.update()

    





 
welcome()