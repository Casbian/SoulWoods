import pygame
import engine
TITLE = engine.TITLE()
TITLE.TKINTERSTARTWINDOWLOGIC()
GAME = engine.GAME()
WORLD = engine.WORLD()
PLAYER = engine.PLAYER()
PLAYERPOSITION = pygame.Vector2(GAME.SCREEN.get_width() / 2, GAME.SCREEN.get_height() / 2)
PLAYERPNGCENTER = PLAYER.IDLERIGHT1SCALED.get_rect()
FRAME = 1
DIRECTION = 0
ROLLING = False
LASTROLLTIME = 0
ATTACKING = False
RUNNING = False
GAME.Start()
RANDOMWORLD = WORLD.RandomWorldGrass(GAME, PLAYERPOSITION)
while GAME.RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            GAME.RUNNING = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                RUNNING = False
            if event.key == pygame.K_SPACE:
                ROLLING = False   
    GAME.TICK = GAME.CLOCK.tick(60) / 1000
    CURRENTTIME = pygame.time.get_ticks() / 1000
    GAME.SCREEN.blit(RANDOMWORLD, (0,0))
    MOUSE = pygame.mouse.get_pressed()
    if MOUSE[0] == True:
        ATTACKING = True
    if MOUSE[0] == False:
        ATTACKING = False
    KEYBOARD = pygame.key.get_pressed()
    if KEYBOARD[pygame.K_w]:
        RUNNING = True
        PLAYERPOSITION.y -= 300 * GAME.TICK
    if KEYBOARD[pygame.K_s]:
        RUNNING = True
        PLAYERPOSITION.y += 300 * GAME.TICK
    if KEYBOARD[pygame.K_a]:
        DIRECTION = 0
        RUNNING = True
        PLAYERPOSITION.x -= 300 * GAME.TICK
    if KEYBOARD[pygame.K_d]:
        DIRECTION = 1
        RUNNING = True
        PLAYERPOSITION.x += 300 * GAME.TICK
    if KEYBOARD[pygame.K_SPACE] and ROLLING != True and (CURRENTTIME - LASTROLLTIME) > 5:
        LASTROLLTIME = CURRENTTIME
        ROLLING = True
    if (CURRENTTIME - LASTROLLTIME) > 3:
        ROLLING = False
    PLAYERPNGCENTER.center = PLAYERPOSITION
    match DIRECTION:
        case 0:
            FRAME = FRAME+1
            if FRAME > 60:
                FRAME = 1 
            if ROLLING != True: 
                if ATTACKING != True:
                    if RUNNING != True:
                        FRAMEPNG = getattr(PLAYER, "IDLELEFT{}SCALED".format(FRAME))
                        GAME.SCREEN.blit(FRAMEPNG, PLAYERPNGCENTER)
                    else:
                        FRAMEPNG = getattr(PLAYER, "RUNLEFT{}SCALED".format(FRAME))
                        GAME.SCREEN.blit(FRAMEPNG, PLAYERPNGCENTER)
                else:
                    FRAMEPNG = getattr(PLAYER, "ATTACKLEFT{}SCALED".format(FRAME))
                    GAME.SCREEN.blit(FRAMEPNG, PLAYERPNGCENTER)
            else:
                FRAMEPNG = getattr(PLAYER, "ROLLLEFT{}SCALED".format(FRAME))
                GAME.SCREEN.blit(FRAMEPNG, PLAYERPNGCENTER)  
        case 1:
            FRAME = FRAME+1
            if FRAME > 60:
                FRAME = 1
            if ROLLING != True:
                if ATTACKING != True:
                    if RUNNING != True:
                        FRAMEPNG = getattr(PLAYER, "IDLERIGHT{}SCALED".format(FRAME))
                        GAME.SCREEN.blit(FRAMEPNG, PLAYERPNGCENTER)
                    else:
                        FRAMEPNG = getattr(PLAYER, "RUNRIGHT{}SCALED".format(FRAME))
                        GAME.SCREEN.blit(FRAMEPNG, PLAYERPNGCENTER)
                else:
                    FRAMEPNG = getattr(PLAYER, "ATTACKRIGHT{}SCALED".format(FRAME))
                    GAME.SCREEN.blit(FRAMEPNG, PLAYERPNGCENTER)
            else:
                FRAMEPNG = getattr(PLAYER, "ROLLRIGHT{}SCALED".format(FRAME))
                GAME.SCREEN.blit(FRAMEPNG, PLAYERPNGCENTER)  
    pygame.display.flip()  
GAME.Exit()