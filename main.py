import engine
TITLE = engine.TITLE()
TITLE.TKINTERSTARTWINDOWLOGIC()
GAME = engine.GAME()
WORLD = engine.WORLD()
PLAYER = engine.PLAYER()
PLAYERPOSITION = engine.pygame.Vector2(GAME.SCREEN.get_width() / 2, GAME.SCREEN.get_height() / 2)
PLAYERPNGCENTER = PLAYER.IDLERIGHT1SCALED.get_rect()
HEALTHBARPOSITION = PLAYER.HEALTHBAR1SCALED.get_rect()
STAMINABARPOSITION = PLAYER.STAMINABAR1SCALED.get_rect()
MAGICABARPOSITION = PLAYER.MAGICABAR1SCALED.get_rect()
PLAYERSTAMINA = 100
FRAME = 1
DIRECTION = 0
ROLLING = False
LASTROLLTIME = 0
ATTACKING = False
RUNNING = False
LASTCLICKTIME = 0
FIRSTCLICKLOCK = 0
GAME.Start()
GAME.TitleMenu()
RANDOMWORLD = WORLD.RandomWorldGrass(GAME, PLAYERPOSITION)
while GAME.RUNNING:
    for event in engine.pygame.event.get():
        if event.type == engine.pygame.QUIT: 
            GAME.RUNNING = False
        if event.type == engine.pygame.KEYUP:
            if event.key == engine.pygame.K_a or event.key == engine.pygame.K_d or event.key == engine.pygame.K_w or event.key == engine.pygame.K_s:
                RUNNING = False
            if event.key == engine.pygame.K_SPACE:
                ROLLING = False
                LASTROLLTIME = CURRENTTIME  
    GAME.TICK = GAME.CLOCK.tick(60) / 1000
    CURRENTTIME = engine.pygame.time.get_ticks() / 1000
    GAME.SCREEN.blit(RANDOMWORLD, (0,0))
    MOUSE = engine.pygame.mouse.get_pressed()
    if MOUSE[0] == True and (CURRENTTIME - FIRSTCLICKLOCK) > 3:
        if not PLAYERSTAMINA < 25:
            if PLAYERSTAMINA != 0:
                ATTACKING = True
                LASTCLICKTIME = CURRENTTIME
    if MOUSE[0] == False and (CURRENTTIME - LASTCLICKTIME) > 1:
        ATTACKING = False
    KEYBOARD = engine.pygame.key.get_pressed()
    if KEYBOARD[engine.pygame.K_s] and KEYBOARD[engine.pygame.K_a] and not KEYBOARD[engine.pygame.K_d]:
        if ATTACKING != True:
            RUNNING = True
            PLAYERPOSITION.x -= (300 / engine.math.sqrt(2)) * GAME.TICK 
            PLAYERPOSITION.y += (300 / engine.math.sqrt(2)) * GAME.TICK 
    if KEYBOARD[engine.pygame.K_s] and KEYBOARD[engine.pygame.K_d] and not KEYBOARD[engine.pygame.K_a]:
        if ATTACKING != True:
            RUNNING = True
            PLAYERPOSITION.x += (300 / engine.math.sqrt(2)) * GAME.TICK 
            PLAYERPOSITION.y += (300 / engine.math.sqrt(2)) * GAME.TICK 
    if KEYBOARD[engine.pygame.K_w] and KEYBOARD[engine.pygame.K_a] and not KEYBOARD[engine.pygame.K_d]:
        if ATTACKING != True:
            RUNNING = True
            PLAYERPOSITION.x -= (300 / engine.math.sqrt(2)) * GAME.TICK 
            PLAYERPOSITION.y -= (300 / engine.math.sqrt(2)) * GAME.TICK 
    if KEYBOARD[engine.pygame.K_w] and KEYBOARD[engine.pygame.K_d] and not KEYBOARD[engine.pygame.K_a]:
        if ATTACKING != True:
            RUNNING = True
            PLAYERPOSITION.x += (300 / engine.math.sqrt(2)) * GAME.TICK 
            PLAYERPOSITION.y -= (300 / engine.math.sqrt(2)) * GAME.TICK 
    if KEYBOARD[engine.pygame.K_w] and not KEYBOARD[engine.pygame.K_a] and not KEYBOARD[engine.pygame.K_s] and not KEYBOARD[engine.pygame.K_d]:
        if ATTACKING != True:
            RUNNING = True
            PLAYERPOSITION.y -= 300 * GAME.TICK
    if KEYBOARD[engine.pygame.K_s] and not KEYBOARD[engine.pygame.K_a] and not KEYBOARD[engine.pygame.K_w] and not KEYBOARD[engine.pygame.K_d]:
        if ATTACKING != True:
            RUNNING = True
            PLAYERPOSITION.y += 300 * GAME.TICK
    if KEYBOARD[engine.pygame.K_a] and not KEYBOARD[engine.pygame.K_w] and not KEYBOARD[engine.pygame.K_s] and not KEYBOARD[engine.pygame.K_d]:
        if ATTACKING != True:
            DIRECTION = 0
            RUNNING = True
            PLAYERPOSITION.x -= 300 * GAME.TICK
    if KEYBOARD[engine.pygame.K_d] and not KEYBOARD[engine.pygame.K_a] and not KEYBOARD[engine.pygame.K_s] and not KEYBOARD[engine.pygame.K_w]:
        if ATTACKING != True:
            DIRECTION = 1
            RUNNING = True
            PLAYERPOSITION.x += 300 * GAME.TICK
    if KEYBOARD[engine.pygame.K_SPACE] and ROLLING != True and (CURRENTTIME - LASTROLLTIME) > 1:
        if not PLAYERSTAMINA < 25:
            if PLAYERSTAMINA != 0:
                if ATTACKING != True:
                    ROLLING = True
    PLAYERPNGCENTER.center = PLAYERPOSITION
    HEALTHBARPOSITION.center = PLAYERPOSITION
    STAMINABARPOSITION.center = PLAYERPOSITION
    MAGICABARPOSITION.center = PLAYERPOSITION
    HEALTHBARPOSITION.y = HEALTHBARPOSITION.y - 76
    STAMINABARPOSITION.y = STAMINABARPOSITION.y - 64
    MAGICABARPOSITION.y = MAGICABARPOSITION.y - 52
    if ATTACKING == True:
        PLAYERSTAMINA = PLAYERSTAMINA - 25 * GAME.TICK
    if ROLLING == True:
        PLAYERSTAMINA = PLAYERSTAMINA - 75 * GAME.TICK
    if PLAYERSTAMINA >= 100:
        PLAYERSTAMINA = 100
    elif PLAYERSTAMINA <5:
        PLAYERSTAMINA = 5
        ATTACKING = False
        ROLLING = False
    else:
        if ATTACKING != True:
            if ROLLING != True:
                PLAYERSTAMINA = PLAYERSTAMINA + 15 * GAME.TICK          
    GAME.SCREEN.blit(PLAYER.HEALTHBAR1SCALED, HEALTHBARPOSITION)
    GAME.SCREEN.blit(PLAYER.MAGICABAR1SCALED, MAGICABARPOSITION)
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
    if PLAYERSTAMINA == 0:
        GAME.SCREEN.blit(PLAYER.STAMINABAR20SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=5:
        GAME.SCREEN.blit(PLAYER.STAMINABAR19SCALED, STAMINABARPOSITION)  
    if PLAYERSTAMINA >=10:
        GAME.SCREEN.blit(PLAYER.STAMINABAR18SCALED, STAMINABARPOSITION) 
    if PLAYERSTAMINA >=15:
        GAME.SCREEN.blit(PLAYER.STAMINABAR17SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=20:
        GAME.SCREEN.blit(PLAYER.STAMINABAR16SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=25:
        GAME.SCREEN.blit(PLAYER.STAMINABAR15SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=30:
        GAME.SCREEN.blit(PLAYER.STAMINABAR14SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=35:
        GAME.SCREEN.blit(PLAYER.STAMINABAR13SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=40:
        GAME.SCREEN.blit(PLAYER.STAMINABAR12SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=45:
        GAME.SCREEN.blit(PLAYER.STAMINABAR11SCALED, STAMINABARPOSITION)  
    if PLAYERSTAMINA >=50:
        GAME.SCREEN.blit(PLAYER.STAMINABAR10SCALED, STAMINABARPOSITION) 
    if PLAYERSTAMINA >=55:
        GAME.SCREEN.blit(PLAYER.STAMINABAR9SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=60:
        GAME.SCREEN.blit(PLAYER.STAMINABAR8SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=65:
        GAME.SCREEN.blit(PLAYER.STAMINABAR7SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=70:
        GAME.SCREEN.blit(PLAYER.STAMINABAR6SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=75:
        GAME.SCREEN.blit(PLAYER.STAMINABAR5SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=80:
        GAME.SCREEN.blit(PLAYER.STAMINABAR4SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=85:
        GAME.SCREEN.blit(PLAYER.STAMINABAR3SCALED, STAMINABARPOSITION)
    if PLAYERSTAMINA >=90:
        GAME.SCREEN.blit(PLAYER.STAMINABAR2SCALED, STAMINABARPOSITION)  
    if PLAYERSTAMINA >=95:
        GAME.SCREEN.blit(PLAYER.STAMINABAR1SCALED, STAMINABARPOSITION) 
    engine.pygame.display.flip()
GAME.Exit()