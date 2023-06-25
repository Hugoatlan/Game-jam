import pygame
from Class.Game import Game

print("bonjour, un parasite a contaminé les trois quarts de la population mondial, vous êtes le dernier survivant et votre but est de repousser les vagues de zombie afin de protéger le villages des survivants")
print("afin de protéger le village vous pouvez déposer des tourelles sur le different emplacement par un click gauche mais attention de bien placer vos tourelles car elle cout chacune 100 gold mais heureusement pour vous quand un zombie meurt vous récupérer des Gold")
reponse = input("Voulez-vous lancez le jeux ?\nsi oui ecrivez yes dans le terminal : ")

if reponse != "yes":
     exit(84)

pygame.init()

game = Game()

screen = pygame.display.set_mode(game.screen)
pygame.display.set_caption("Tower Defender")

background = pygame.image.load('img/tower_defender.png')

font = pygame.font.Font(None, 36)

seconde = 0

running = True

while running:
    text_gold = font.render("Gold : {}".format(str(game.gold)), True, (255, 255, 255))
    text_wave = font.render("Wave : {}".format(str(game.wave + 1)), True, (255, 255, 255))
    text_health = font.render("{0} / {1}".format(str(game.health), str(game.health_max)), True, (255, 255, 255))
    seconde += 1
    if seconde == 30:
        seconde = 0
        game.time += 1
        game.check_wave()

    game.dead()

    screen.blit(background, (0, 0))
    game.bar_health(screen)
    screen.blit(text_gold, (0, 5))
    screen.blit(text_wave, (150, 5))
    screen.blit(text_health, (880, 5))

    for tower in game.all_tower:
        tower.attack_enemies(game.all_zombie)
        rotated_tower = pygame.transform.rotate(tower.image, tower.angle - 50)
        rotated_rect_t = rotated_tower.get_rect(center=tower.rect.center)

        screen.blit(rotated_tower, rotated_rect_t)

    for zombie in game.all_zombie:
        zombie.move()
        rotated_zombie = pygame.transform.rotate(zombie.image, zombie.chemin[zombie.pos][2])
        rotated_rect_z = rotated_zombie.get_rect(center=zombie.rect.center)

        screen.blit(rotated_zombie, rotated_rect_z)
        zombie.bar_health(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            game.check_emplacement(mouse_x, mouse_y)

    if game.time >= 110:
        running = False
        print("Win")
    if game.health <= 0:
        running = False
        print("Game over")

    pygame.display.flip()

pygame.quit()
