import pygame
import time

pygame.init()

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1600
acclrX = 0
acclrY = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
player = pygame.Rect((300, 250, 50, 50))
font = pygame.font.SysFont("Arial", 30)
maxspeed = 20
clock_s = 60

run = True
while run:

    screen.fill((0,0,0))
    clock.tick(clock_s)
    pygame.draw.rect(screen, (255, 0, 0), player)

    speed_text = font.render(f"X: {acclrX} | Y: {acclrY}", True, (255, 255, 255))
    screen.blit(speed_text, (20, 20))
    
    pos_text = font.render(f"X: {player.x} | Y: {player.y}", True, (0, 255, 0))
    screen.blit(pos_text, (20, 60))

    fps_text = font.render(f"{int(clock.get_fps())}", True, (0, 0, 255))
    screen.blit(fps_text, (20, 100))

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        acclrX -= 2
    if key[pygame.K_d] == True:
        acclrX += 2
    if key[pygame.K_w] == True:
        acclrY -= 2
    if key[pygame.K_s] == True:
        acclrY += 2
    if key[pygame.K_LEFT] == True:
        player.move_ip(-1,0)
    if key[pygame.K_RIGHT] == True:
        player.move_ip(1,0)
    if key[pygame.K_UP] == True:
        player.move_ip(0,-1)
    if key[pygame.K_DOWN] == True:
        player.move_ip(0,1)
    if key[pygame.K_f] == True:
        acclrY = int(acclrY / 2)
        acclrX = int(acclrX / 2)
        
    if key[pygame.K_r] == True:
        player = pygame.Rect((300, 250, 50, 50))
        acclrX = 0
        acclrY = 0

    if key[pygame.K_q] == True:
        clock_s /= 2
        time.sleep(0.5)
    if key[pygame.K_e] == True:
        clock_s *= 2
        time.sleep(0.5)
            
    player.move_ip(acclrX, acclrY)
    if not (key[pygame.K_a] or key[pygame.K_d]):
        if acclrX > 0:
            acclrX -= 1
        elif acclrX < 0:
            acclrX += 1 

    if not (key[pygame.K_w] or key[pygame.K_s]):
        if acclrY > 0:
            acclrY -= 1
        elif acclrY < 0:
            acclrY += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
