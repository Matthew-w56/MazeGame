# |-----------------------------------|
# |       By: Matthew Williams        |
# |     Enjoy the maze game, and      |
# |    Try to do it without ghost!    |  Lines:      ~525
# |-----------------------------------|  Characters: ~20,000
from Player import *

pygame.mouse.set_visible(True)
menu = True

player = Player()
speed = 1

Enemy1 = Enemy(2, orange, (520, 420), False)

StartButton = pygame.Rect(200, 150, 100, 50)

while menu:
    Screen.fill(white)
    pygame.draw.rect(Screen, green, StartButton)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
            if mouse_rect.colliderect(StartButton):
                menu = False

    write('Press the green button to start', red, (200, 400), size=40)

    pygame.display.update()

LevelSetup(0)
player.rect.x, player.rect.y = o.player_pos
while True:
    Screen.fill((50, 50, 50))
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[K_RIGHT]:
        player.move(player.speed, 0)
    if key[K_LEFT]:
        player.move(-player.speed, 0)
    if key[K_UP]:
        player.move(0, -player.speed)
    if key[K_DOWN]:
        player.move(0, player.speed)
    if key[K_a]:
        player.speed = 10
    if not key[K_a]:
        player.speed = 5
    if key[K_t]:
        player.ghost = True
    if not key[K_t]:
        player.ghost = False

    for wall in o.Walls:
        pygame.draw.rect(Screen, white, wall.rect)
    for point in o.DeathPoints:
        pygame.draw.rect(Screen, blue, point.rect)
    for edge in o.Edges:
        pygame.draw.rect(Screen, brown, edge.rect)
    pygame.draw.rect(Screen, green, o.end_point)
    pygame.draw.rect(Screen, red, player.rect)

    for enemy in o.Enemies:
        if enemy.level == player.level:
            enemy.Find(player)

    for enemy in o.Enemies:
        if enemy.level == player.level:
            if player.rect.colliderect(enemy.rect):
                print("Got Ya!  Good try though.")
                print("-The little square that is not you")
                pygame.quit()
                sys.exit()
            enemy.draw()

    pygame.display.update()
    pygame.time.wait(30)


