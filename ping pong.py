import pygame, sys, random
width = 1000
height = 500
ball_size = 10
index = 1

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
yellow = (255,255,0)
pink = (255,105,180)
bumper_width = 20
bumper_height = 60
pygame.init()

derek = pygame.image.load('derek.png')
class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

class Bumper:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.change_y1= 0
        self.change_y2 = 0

def game_over_screen():
    size = [width,height]
    pygame.init()
    pygame.font.init()
    myfont1 = pygame.font.SysFont('Tlwg Typist', 120)
    myfont2 = pygame.font.SysFont('Tlwg Typist', 30)

    text_surface1 = myfont1.render('Game Over', False, (255,0,0))
    text_surface2 = myfont2.render('press any key to restart', False, (255,0,0))
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    screen.fill(black)
    screen.blit(text_surface1,(width/5,height/4))
    screen.blit(text_surface2,(width/3,height/1.8))
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                waiting = False
    main()
def home_screen():
    size = [width,height]
    pygame.init()
    pygame.mixer.music.load('bf.wav')
    pygame.mixer.music.play(-1)
    pygame.font.init()
    myfont1 = pygame.font.SysFont('Tlwg Typist', 120)
    myfont2 = pygame.font.SysFont('Tlwg Typist', 30)
    myfont3 = pygame.font.SysFont('Tlwg Typist', 20)
    text_surface1 = myfont1.render('Ping Pong', False, (255,0,0))
    text_surface2 = myfont2.render('press any key to start', False, (255,0,0))
    text_surface3 = myfont3.render('Player 1: W = UP, S = DOWN ', False, (255, 0, 0))
    text_surface4 = myfont3.render('Player 2: O = UP, L= DOWN', False, (255, 0, 0))
    text_surface5 = myfont3.render('Start game: SPACE', False, (255, 0, 0))


    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    screen.fill(black)
    screen.blit(text_surface1,(width/5.1,height/4))
    screen.blit(text_surface2,(width/3.1,height/1.9))
    screen.blit(text_surface3, (30, height / 1.3))
    screen.blit(text_surface4, (30, height / 1.2))
    screen.blit(text_surface5, (30, height/1.1))

    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                waiting = False
    main()
def make_ball():
    ball = Ball()
    ball.x = width//2
    ball.y = height//2
    ball.change_y = random.randint(-4,4)
    ball.change_x = 6
    return ball
def make_bumper():
    bumper = Bumper()
    bumper.x1 = bumper_width
    bumper.y1 = (height*.5) - (bumper_height*.5)
    bumper.x2 = width-bumper_width*2
    bumper.y2 = (height*.5) - (bumper_height*.5)
    bumper.change_y1 = 7
    bumper.change_y2 = 7
    return bumper

def main():

    pygame.init()

    colors = [green, blue, pink, yellow]
    index = 0

    clock = pygame.time.Clock()
    size = [width,height]

    pressed_down_left = False
    pressed_up_left= False
    pressed_down_right = False
    pressed_up_right = False
    ball_move = False
    collision = False
    caption = pygame.display.set_caption("Ping Pong")
    screen = pygame.display.set_mode(size)
    ball = make_ball()
    bumper = make_bumper()
    # drawing the bumpers

    #drawing the ball
    #pygame.draw.circle(screen,red, [ball.x, ball.y], ball_size)

    #main loop
    while True: 

        screen.fill(black)
        bumper1 = pygame.draw.rect(screen, red, [bumper.x1, bumper.y1, bumper_width, bumper_height])
        bumper2 = pygame.draw.rect(screen, red, [bumper.x2, bumper.y2, bumper_width, bumper_height])


        circle = pygame.draw.circle(screen, colors[index], [ball.x, ball.y], ball_size)







        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball_move = True
                if event.key == pygame.K_s:
                    pressed_down_left = True
                elif event.key == pygame.K_w:
                    pressed_up_left = True
                elif event.key == pygame.K_l:
                    pressed_down_right = True
                elif event.key == pygame.K_o:
                    pressed_up_right = True


                #elif event.key == pygame.K_w:
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    pressed_down_left = False
                elif event.key == pygame.K_w:
                    pressed_up_left = False
                elif event.key == pygame.K_l:
                    pressed_down_right = False
                elif event.key == pygame.K_o:
                    pressed_up_right = False
        #left bumper
        if pressed_down_left == True:
            bumper.y1 += bumper.change_y1
        if bumper.y1>height-bumper_height: bumper.y1 = height-bumper_height

        if pressed_up_left == True:
            bumper.y1 -= bumper.change_y1
        if bumper.y1<0:bumper.y1 = 0

        #right bumper
        if pressed_down_right == True:
            bumper.y2 += bumper.change_y2
        if bumper.y2>height-bumper_height: bumper.y2 = height-bumper_height

        if pressed_up_right == True:
            bumper.y2 -= bumper.change_y2
        if bumper.y2<0:bumper.y2 = 0

        if ball_move:
            ball.x -= ball.change_x
            ball.y -= ball.change_y
        #collision detection
        if ball.x>bumper.x1 and ball.x<bumper.x1+bumper_width and ball.y>bumper.y1 and ball.y<bumper.y1+bumper_height or ball.x> bumper.x2 and ball.x < bumper.x2 + bumper_width and ball.y > bumper.y2 and ball.y < bumper.y2 + bumper_height:
            effect = pygame.mixer.Sound('boop.wav')
            effect.play()
            ball.change_x *= -1


            index+=1
        #if ball.x > (bumper.x1+60) and ball.x < bumper.x1 + (bumper_width +60)and ball.y > bumper.y1 and ball.y < bumper.y1 + bumper_height or ball.x > (bumper.x2-60) and ball.x < bumper.x2 + (bumper_width+60)and ball.y > bumper.y2 and ball.y < bumper.y2 + bumper_height:
            #effect.play()
        if ball.x> width+80 or ball.x <0-80:
            game_over_screen()
        if index > 3:
            index = 0

        if ball.y<0 or ball.y > height:
            ball.change_y*=-1





        clock.tick(100)
        pygame.display.update()







home_screen()