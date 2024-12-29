import pygame

clock = pygame.time.Clock()

# отсюда начинается игра
pygame.init()

# фон
bg = pygame.image.load('images/bg.png')
height = bg.get_height()
width = bg.get_width()

# ставим размер игры, в параметрах размер фона
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('images/bg.png').convert_alpha()
# задаем title
icon_text = 'test_game'
pygame.display.set_caption(icon_text)
# задаем иконку
icon_title = pygame.image.load("images/icon_title.png").convert_alpha()
pygame.display.set_icon(icon_title)
# по логике должен игрок в начале вставать в эту позу
player_center = pygame.image.load('images/move/center/1.png').convert_alpha()
# массив с анимацией движения вправо
walk_right = [
    pygame.image.load('images/move/right/1.png').convert_alpha(),
    pygame.image.load('images/move/right/2.png').convert_alpha(),
    pygame.image.load('images/move/right/3.png').convert_alpha(),
    pygame.image.load('images/move/right/4.png').convert_alpha()
]
# массив с анимацией движения влево
walk_left = [
    pygame.image.load('images/move/left/1.png').convert_alpha(),
    pygame.image.load('images/move/left/2.png').convert_alpha(),
    pygame.image.load('images/move/left/3.png').convert_alpha(),
    pygame.image.load('images/move/left/4.png').convert_alpha()
]
robot = pygame.image.load('images/robot.png').convert_alpha()
robot_list_in_game = []
# счетчик для анимаций
player_anim_count = 0
# счетчик для прокручивания фона
bg_x = 0
# скорость передвижения игрока
player_speed = 5
# начальные коры игрока
player_x = 150
player_y = 460

is_jump = False
jump_count = 8

bg_sound = pygame.mixer.Sound('music/bg.mp3')
# bg_sound.play()

robot_timer = pygame.USEREVENT + 1
pygame.time.set_timer(robot_timer, 2500)

# процесс игры
running = True
while running:
    # первый фон, со старта
    screen.blit(bg, (bg_x, 0))
    # при окончании первого фона, запускается этот
    screen.blit(bg, (bg_x + width, 0))

    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
    if robot_list_in_game:
        for el in robot_list_in_game:
            screen.blit(robot, el)
            el.x -= 10
            if player_rect.colliderect(el):
                print("You lose")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        # персонаж с бегом вправо
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        # персонаж с бегом влево
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
    # прыгание персонажа
    # если сейчас не прыгает и зажали пробел то начинается прыжок
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        # логика такая, в начале двигаемся вверх пока положительное число
        # потом падаем вниз когда отрицательное
        # потом убираем прыжок и ставим счетчику дефолт
        if jump_count >= -8:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2

            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8

    # else:
    #     screen.blit(player_center, (player_x, player_y))

    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < width - 50:
        player_x += player_speed

    player_anim_count += 1
    # сдвиг фона
    bg_x -= 1
    if bg_x == -width:
        bg_x = 0
    # начало перебора анимаций заново
    if player_anim_count == len(walk_right):
        player_anim_count = 0
    # обновляем вьюшку
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == robot_timer:
            robot_list_in_game.append(robot.get_rect(topleft=(width, 460)))
    clock.tick(20)
