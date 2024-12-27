import pygame

clock = pygame.time.Clock()

#отсюда начинается игра
pygame.init()

# фон
bg = pygame.image.load('images/bg.png')
height = bg.get_height()
width = bg.get_width()

# ставим размер игры, в параметрах размер фона
screen = pygame.display.set_mode((width, height))
# задаем title
icon_text = 'test_game'
pygame.display.set_caption(icon_text)
# задаем иконку
icon_title = pygame.image.load("images/icon_title.png")
pygame.display.set_icon(icon_title)
# по логике должен игрок в начале вставать в эту позу
player_center = pygame.image.load('images/move/center/1.png')
# массив с анимацией движения вправо
walk_right = [
    pygame.image.load('images/move/right/1.png'),
    pygame.image.load('images/move/right/2.png'),
    pygame.image.load('images/move/right/3.png'),
    pygame.image.load('images/move/right/4.png')
]
# массив с анимацией движения влево
walk_left = [
    pygame.image.load('images/move/left/1.png'),
    pygame.image.load('images/move/left/2.png'),
    pygame.image.load('images/move/left/3.png'),
    pygame.image.load('images/move/left/4.png')
]
# счетчик для анимаций
player_anim_count = 0
# счетчик для прокручивания фона
bg_x = 0

bg_sound = pygame.mixer.Sound('music/bg.mp3')
bg_sound.play()
#процесс игры
running = True
while running:
    # первый фон, со старта
    screen.blit(bg, (bg_x, 0))
    # при окончании первого фона, запускается этот
    screen.blit(bg, (bg_x + width, 0))
    # персонаж с бегом вправо
    screen.blit(walk_right[player_anim_count], (500, 460))
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
    clock.tick(20)

