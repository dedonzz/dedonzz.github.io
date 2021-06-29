import pygame
import time 
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()

clock = pygame.time.Clock()
ver = "1.3"
autog = 0
mongold = 2
mongnew = 0
level = 0
coins = 0
display_width = 800
display_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 100, 250)
maindisplayloop = 0

asset1_url = resource_path('asset/img1.png')
asset2_url = resource_path('asset/img2.png')
asset3_url = resource_path('asset/cursor.png')

main = [pygame.image.load(asset1_url), pygame.image.load(asset2_url)]

#levelup = [pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load()]
#autocode = [pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load()]

cursor = pygame.image.load(asset3_url)
cursor = pygame.transform.scale(cursor, (30, 40))

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Coding Hell")
pygame.mouse.set_visible(False)

def levelup():
    global mongold
    global level
    if mongold < mongnew:
        mongold += mongnew
        level += 9

def autocoder():
    global coins
    global autog
    time.sleep(0.1)
    coins = coins + autog

def DrawText(text, Textcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)

def wait_for_key(x):
    waiting = True
    while waiting:
        clock.tick()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                if x:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        waiting = False
                if not x:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            waiting = False

def start_screen():
        gameDisplay.fill(black)
        DrawText("WELCOME TO CODING HELL", white, display_width / 2, display_height / 4, 48)
        DrawText("Click anywhere to start coding!", white, display_width / 2, display_height / 2, 22)
        pygame.display.flip()
        wait_for_key(True)
        main_loop()

def gameover_screen():
        gameDisplay.fill(black)
        DrawText("All Done", white, display_width / 2, display_height / 4, 48)
        DrawText("You have completed your python final project", white, display_width / 2, display_height / 2, 22)
        DrawText("Press Enter to do it once again ;D", white, display_width / 2, display_height * 3 / 4, 22)
        pygame.display.flip()
        wait_for_key(False)
        main_loop()

def main_loop():
    global clock
    global autog
    global ver
    global maindisplayloop
    global coins
    global mongnew
    global level
    startmain = False
    startauto = True
    firstimg = True
    game_running = True
    mong = 1
    cost = 50
    cost2 = 50

    while game_running:
        gameDisplay.fill(white)
        autocoder()
        levelup()
        if coins >= 10000:
            print("Done")
            game_running = False
            coins = 0
            autog = 0
            level = 0
            gameover_screen()

        if firstimg:
            gameDisplay.blit(main[0], (290, 150))

        if startmain:
            if startauto:
                gameDisplay.blit(main[maindisplayloop], (290, 150))
            if startauto == False:
                if maindisplayloop == 0:
                    maindisplayloop = 1
                else:
                    maindisplayloop = 0
                gameDisplay.blit(main[maindisplayloop], (290, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                startmain = True
                firstimg = False
                if mopos <= (800, 0):
                    if maindisplayloop == 0:
                        maindisplayloop = 1
                    else:
                        maindisplayloop = 0
                    coins += mong

                if mopos[0] <= 760 and mopos[0] >= 670:
                    if mopos[1] <= 390 and mopos[1] >= 350:
                        if coins >= cost:
                            coins = coins - cost
                            cost *= 5
                            mong *= 3
                            mongnew = mong

                if mopos[0] <= 170 and mopos[0] >= 10:
                    if mopos[1] <= 390 and mopos[1] >= 350:
                        if coins >= cost2:
                            startauto = False
                            coins = coins - cost2
                            cost2 = cost2 * 3
                            autog = autog + 2

        DrawText("Version: " + ver, black, 730, 20, 20)
        DrawText("Coding hell", black, 400, 100, 50)

        DrawText("You have complete ", black, 100, 20, 20)
        DrawText(str(f'{coins}') + " lines", black, 100, 40, 20)

        DrawText("Level Up ", black, 730, 370, 20)
        DrawText(str(cost), black, 730, 390, 20)
        DrawText("Buy Auto Coder ", black, 100, 370, 20)
        DrawText(str(cost2), black, 100, 390, 20)

        pygame.draw.rect(gameDisplay, black, (720, 415, 20, 100))
        pygame.draw.rect(gameDisplay, white, (721, 506-level, 18, 8+level))

        gameDisplay.blit(cursor, pygame.mouse.get_pos())
        pygame.display.update()
        clock.tick(60)

start_screen()
quit()