import pygame.gfxdraw
import math
from functools import wraps, reduce

import src.utilities as utilities
import src.game as game
from src.player import Player
from src.enemy import Enemy
from src.weapon import Bullet
from src.blood import Blood
from src.power import PowerUp
from src.wave_controller import WaveController
from src.manager import *


class Button:
    def __init__(self, width, height, inact_clr=(15, 15, 15)):
        self.width = width
        self.height = height
        self.inact_clr = inact_clr

    def draw(self, x, y, message, action=None, font_size=10, b_font_clr=(255, 255, 255)):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        utilities.print_text(
            screen=game.screen, message=message, x=x + 5, y=y + 5, font_clr=b_font_clr, font_size=font_size)

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(game.screen, self.inact_clr, (x, y, self.width, self.height))
                utilities.print_text(
                    screen=game.screen, message=message, x=x + 5, y=y + 5, font_clr=(123, 22, 12), font_size=font_size)
                if click[0] == 1:
                    utilities.play_sound('button.wav')
                    pygame.time.delay(300)
                    if action == 'start':
                        play_loop()
                    if action == 'rating':
                        show_rate_table(
                            pause_bg=pygame.image.load(utilities.get_image('table.jpg'))
                        )
                    if action == 'rules':
                        show_rules(rule_bg=pygame.image.load(utilities.get_image('rules.jpg')))
                    if action == 'quit':
                        pygame.quit()
                        quit()

        else:
            pygame.draw.rect(game.screen, self.inact_clr, (x, y, self.width, self.height))
            utilities.print_text(
                screen=game.screen, message=message, x=x + 5, y=y + 5, font_clr=b_font_clr, font_size=font_size)


class Screen:
    def __init__(self, keys: list = None):
        if keys is None:
            self.keys = []
        else:
            self.keys = keys

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            cursor_img = pygame.image.load(utilities.get_image('cursor.png'))
            cursor_rect = cursor_img.get_rect()

            result = None

            for _ in iter(int, 1):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                result = func(*args, **kwargs)

                if result is not None:
                    kwargs = result

                cursor_rect.topleft = pygame.mouse.get_pos()
                game.screen.blit(cursor_img, cursor_rect)

                keys = pygame.key.get_pressed()

                if len(self.keys) and reduce(lambda x, y: x or y, [keys[ind] for ind in self.keys]):
                    break

                pygame.display.update()

            return result

        return wrapper


def start():
    pygame.mouse.set_visible(False)
    pygame.mixer.music.load(utilities.get_image('menu.mp3'))
    pygame.mixer.music.play(-1)
    print(game.save_data.get('rating'))

    show_menu(
        menu_bg=pygame.image.load(utilities.get_image('crimsonland_menu.jpg')),
        start_btn=Button(125, 25),
        rating_btn=Button(125, 25),
        info_btn=Button(125, 25),
        opt_btn=Button(125, 25),
        quit_btn=Button(125, 25),
    )


@Screen()
def show_menu(*args, **kwargs):
    game.screen.blit(kwargs['menu_bg'], (0, 0))
    kwargs['start_btn'].draw(220, 213, 'Start game', action='start')
    kwargs['rating_btn'].draw(203, 274, 'Rating', action='rating')
    kwargs['info_btn'].draw(182, 333, 'About game', action='rules')
    kwargs['opt_btn'].draw(161, 394, 'Options', action=None)
    kwargs['quit_btn'].draw(140, 453, 'Quit', action='quit')


@Screen([pygame.K_ESCAPE])
def show_congratulations(*args, **kwargs):
    game.screen.blit(kwargs['cong_bg'], (0, 0))


@Screen([pygame.K_RETURN])
def show_pause(*args, **kwargs):
    game.screen.blit(kwargs['pause_bg'], (0, 0))
    utilities.print_text(
        screen=game.screen, message='Paused! press ENTER to continue',
        x=110, y=280, font_clr=(255, 255, 255), font_size=20)


@Screen([pygame.K_ESCAPE, pygame.K_RETURN])
def show_rules(*args, **kwargs):
    game.screen.blit(kwargs['rule_bg'], (0, 0))


@Screen([pygame.K_ESCAPE, pygame.K_RETURN])
def show_rate_table(*args, **kwargs):
    x, y = 165, 155
    step_x, step_y = 380, 40

    sorted_tuples = sorted(game.r_table.r_table.items(), key=lambda item: item[1])

    game.r_table.r_table = {k: v for k, v in sorted_tuples}

    game.screen.blit(kwargs['pause_bg'], (0, 0))

    count = 0

    for name, value in reversed(game.r_table.r_table.items()):
        if count == 0:
            utilities.print_text(
                screen=game.screen,
                message=f' {count + 1}{" " * 5}{name}', x=x, y=y, font_type='fonts/Qore.otf', font_clr=(255, 255, 255),
                font_size=15)
        else:
            utilities.print_text(
                screen=game.screen,
                message=f'{count + 1}{" " * 5}{name}', x=x, y=y, font_type='fonts/Qore.otf', font_clr=(255, 255, 255),
                font_size=15)

        utilities.print_text(
            screen=game.screen,
            message=str(value), x=x + step_x, y=y, font_type='fonts/Qore.otf', font_clr=(255, 255, 255), font_size=15)

        y += step_y
        count += 1
        if count == 10:
            break


@Screen([pygame.K_RETURN, pygame.K_ESCAPE])
def show_input_name(*args, **kwargs):
    game.screen.blit(kwargs['pause_bg'], (0, 0))

    utilities.print_text(
        screen=game.screen,
        message='Enter your name: ', x=274, y=300, font_clr=(255, 255, 255), font_size=20, font_type='fonts/Qore.otf')
    pygame.draw.rect(game.screen, (255, 255, 255), kwargs['input_rect'])
    utilities.print_text(
        screen=game.screen,
        message=kwargs['input_text'] + kwargs['addition'] * '_',
        x=kwargs['input_rect'].x + 5,
        y=kwargs['input_rect'].y + 5,
        font_size=30,
        font_type='fonts/Qore.otf'
    )

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                if len(kwargs['input_text']):
                    game.r_table.update(kwargs['input_text'], ScoreManager.score)
                    if max(game.r_table.r_table, key=game.r_table.r_table.get) == kwargs['input_text']:
                        show_congratulations(cong_bg=pygame.image.load(utilities.get_image('congratulations.jpg')))
                    return kwargs

            elif event.key == pygame.K_ESCAPE:
                kwargs['input_text'] = None
                return kwargs

            elif event.key == pygame.K_BACKSPACE:
                kwargs['input_text'] = kwargs['input_text'][:-1]

            else:
                if len(kwargs['input_text']) < 10:
                    kwargs['input_text'] += event.unicode

    if kwargs['tick'] == 100:
        kwargs['addition'] = not kwargs['addition']
        kwargs['tick'] = 0
    else:
        kwargs['tick'] += 1

    return kwargs


@Screen([pygame.K_ESCAPE])
def show_rip(*args, **kwargs):
    game.screen.blit(kwargs['pause_bg'], (0, 0))

    utilities.print_text(
        screen=game.screen, message='R.I.P.',
        x=280, y=280, font_clr=(255, 255, 255), font_size=50, font_type='fonts/Qore.otf')
    utilities.print_text(
        screen=game.screen, message=kwargs['name'],
        x=280, y=330, font_clr=(255, 255, 255), font_size=50, font_type='fonts/Qore.otf')

    if not kwargs['saved']:
        game.save_data.save(kwargs['name'])
        game.save_data.add('rating', game.r_table.r_table)
        kwargs['saved'] = True
        return kwargs


def play_loop():
    player_group = pygame.sprite.Group()
    projectiles_group = pygame.sprite.Group()
    enemies_group = pygame.sprite.Group()
    power_group = pygame.sprite.Group()
    blood_group = pygame.sprite.Group()

    Player.containers = player_group
    Bullet.containers = projectiles_group
    Enemy.containers = enemies_group
    PowerUp.containers = power_group
    Blood.containers = blood_group

    mr_player = Player(game.screen, game.WIDTH / 2, game.HEIGHT / 2)
    wave_controller = WaveController(game.screen, game.WIDTH, game.HEIGHT, enemies_group)

    cursor_img = pygame.image.load(utilities.get_image('curs_white.png'))
    cursor_rect = cursor_img.get_rect()

    for _ in iter(int, 1):

        game.clock.tick(game.FPS)

        game.screen.blit(game.background_image,
                         (-500 - Background.display_scroll[0], -350 - Background.display_scroll[1]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_pause(pause_bg=pygame.image.load(utilities.get_image('land.png')))

        keys = pygame.key.get_pressed()
        cursor_rect.center = pygame.mouse.get_pos()

        if (keys[pygame.K_d] and keys[pygame.K_s]) or (keys[pygame.K_a] and keys[pygame.K_s]) or (
                keys[pygame.K_w] and keys[pygame.K_a]) or (keys[pygame.K_d] and keys[pygame.K_w]):
            buff_speed = 1 / 1.4
        else:
            buff_speed = 1

        if 250 > Background.display_scroll[0] > - 250:

            if keys[pygame.K_d]:
                mr_player.animate()
                Background.display_scroll[0] += buff_speed * mr_player.speed
                for projectile in projectiles_group:
                    projectile.x -= buff_speed * mr_player.speed

            elif keys[pygame.K_a]:
                mr_player.animate()
                Background.display_scroll[0] -= buff_speed * mr_player.speed
                for projectile in projectiles_group:
                    projectile.x += buff_speed * mr_player.speed

        elif Background.display_scroll[0] >= 250:
            if keys[pygame.K_d]:
                mr_player.animate()
                mr_player.move(buff_speed, 0)

            elif keys[pygame.K_a]:
                mr_player.animate()
                mr_player.move(-buff_speed, 0)
                if mr_player.x <= 401 and Background.display_scroll[0] > 250:
                    Background.display_scroll[0] = 249

        elif Background.display_scroll[0] <= -250:
            if keys[pygame.K_d]:
                mr_player.animate()
                mr_player.move(buff_speed, 0)
                if mr_player.x >= 399 and Background.display_scroll[0] < -250:
                    Background.display_scroll[0] = -249

            elif keys[pygame.K_a]:
                mr_player.animate()
                mr_player.move(-buff_speed, 0)

        if 200 > Background.display_scroll[1] > - 200:

            if keys[pygame.K_w]:
                mr_player.animate()
                Background.display_scroll[1] -= buff_speed * mr_player.speed
                for projectile in projectiles_group:
                    projectile.y += buff_speed * mr_player.speed

            elif keys[pygame.K_s]:
                mr_player.animate()
                Background.display_scroll[1] += buff_speed * mr_player.speed
                for projectile in projectiles_group:
                    projectile.y -= buff_speed * mr_player.speed

        elif Background.display_scroll[1] >= 200:

            if keys[pygame.K_w]:
                mr_player.animate()
                mr_player.move(0, -buff_speed)
                if mr_player.y <= 301 and Background.display_scroll[1] >= 200:
                    Background.display_scroll[1] = 199
            elif keys[pygame.K_s]:
                mr_player.animate()
                mr_player.move(0, buff_speed)

        elif Background.display_scroll[1] <= - 200:

            if keys[pygame.K_w]:
                mr_player.animate()
                mr_player.move(0, -buff_speed)
            elif keys[pygame.K_s]:
                mr_player.animate()
                mr_player.move(0, buff_speed)
                if mr_player.y >= 299 and Background.display_scroll[1] <= -200:
                    Background.display_scroll[1] = -199

        if pygame.mouse.get_pressed()[0]:
            mr_player.shoot()

        if keys[pygame.K_1]:
            mr_player.change_weapon(0)
        if keys[pygame.K_2]:
            if wave_controller.wave_number >= 5:
                mr_player.change_weapon(1)
        if keys[pygame.K_3]:
            if wave_controller.wave_number >= 10:
                mr_player.change_weapon(2)

        if (keys[pygame.K_r] and mr_player.player_weapon.ammo_count_max > mr_player.player_weapon.ammo_count > 0) or \
                mr_player.player_weapon.ammo_count == 0:
            mr_player.reload_weapon(cursor_rect.centerx, cursor_rect.centery)

        else:
            mr_player.player_weapon.reload_cooldown = 0

        if wave_controller.wave_number == 0:
            if keys[pygame.K_SPACE]:
                wave_controller.new_wave(mr_player)

        elif len(enemies_group.sprites()) <= 5:
            utilities.print_text(
                screen=game.screen,
                message="New Wave coming in",
                x=280, y=50, font_clr=(255, 255, 255), font_type='fonts/Qore.otf', font_size=17)
            wave_controller.draw_timer(game.screen, 400, 110)
            wave_controller.wave_cd += 1

            if keys[pygame.K_SPACE] or wave_controller.wave_cd == wave_controller.wave_cd_max or (
                    wave_controller.wave_cd < wave_controller.wave_cd_max and len(enemies_group.sprites()) == 0):
                if wave_controller.wave_cd < wave_controller.wave_cd_max:
                    ScoreManager.score += math.ceil((wave_controller.wave_cd_max - wave_controller.wave_cd) / 30)

                wave_controller.new_wave(mr_player)

        mr_player.update(enemies_group, power_group)

        for blood in blood_group:
            blood.update()

        for power in power_group:
            power.update(mr_player)

        for projectile in projectiles_group:
            projectile.update()

        for enemy in enemies_group:
            enemy.update(projectiles_group, power_group)

        if not mr_player.alive:
            name = show_input_name(
                pause_bg=pygame.image.load(utilities.get_image('enter.jpg')),
                input_text='',
                addition=True,
                tick=0,
                input_rect=pygame.Rect(274, 274, 255, 50)
            )['input_text']
            if name is not None:
                show_rip(
                    name=name,
                    pause_bg=pygame.image.load(utilities.get_image('enter.jpg')),
                    saved=False
                )
            ScoreManager.score = 0
            break

        utilities.print_text(
            screen=game.screen,
            message="Score: " + str(ScoreManager.score),
            x=10, y=10, font_clr=(255, 255, 255), font_type='fonts/Qore.otf')

        utilities.print_text(
            screen=game.screen,
            message="Wave: " + str(wave_controller.wave_number),
            x=615, y=10, font_clr=(255, 255, 255), font_type='fonts/Qore.otf')

        game.screen.blit(cursor_img, cursor_rect)

        pygame.display.flip()
