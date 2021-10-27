import pygame
import random

pygame.init()
pygame.mixer.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Direction Game")
game_surface = pygame.Surface((2000, 2000))
game_surface.fill((255, 255, 255))
game_window.blit(game_surface, (0, 0))

# Constants
MOVE_DISTANCE = 125
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
YELLOW = (252, 248, 3)
TURQUOISE = (3, 240, 252)
PURPLE = (177, 3, 252)
PINK = (255, 125, 220)
color_list = [RED, BLUE, GREEN, YELLOW, TURQUOISE, PURPLE, PINK]

# Sounds
go_straight = pygame.mixer.Sound("straight.ogg")
turn_left = pygame.mixer.Sound("left.ogg")
turn_right = pygame.mixer.Sound("right.ogg")

# Pictures
heart_raw = pygame.image.load("heart.png")
heart = pygame.transform.scale(heart_raw, (100, 100))

# Font
font = pygame.font.Font(None, 60)
header_font = pygame.font.Font(None, 140)

# Timer
# clock = pygame.time.Clock()
# counter = 10
# clock_font = font.render(str(counter), True, (0, 128, 0))
# timer_event = pygame.USEREVENT+1
# pygame.time.set_timer(timer_event, 1000)


class Building:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, 200, 200)

    def draw_building(self):
        pygame.draw.rect(game_window, self.color, (self.x, self.y, 200, 200))


class Button:
    def __init__(self, x, y):
        self.color = (220, 50, 113)
        self.x = x
        self.y = y
        self.width = 600
        self.height = 200
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)


menu_button_1 = Button(550, 400)
menu_button_2 = Button(550, 700)


class Player:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.facing = ""
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def draw_player(self):
        pygame.draw.rect(game_window, self.color, (self.x, self.y, 50, 50))
        if player.facing == "right":
            pygame.draw.rect(game_window, (120, 120, 120), (self.x + 40, self.y + 20, 10, 10))
        elif player.facing == "left":
            pygame.draw.rect(game_window, (120, 120, 120), (self.x, self.y + 20, 10, 10))
        elif player.facing == "up":
            pygame.draw.rect(game_window, (120, 120, 120), (self.x + 20, self.y, 10, 10))
        elif player.facing == "down":
            pygame.draw.rect(game_window, (120, 120, 120), (self.x + 20, self.y + 40, 10, 10))

    def move_right(self, move):
        self.x = self.x + move
        player.facing = "right"
        game_window.blit(game_surface, (0, 0))
        self.draw_player()

    def move_left(self, move):
        self.x = self.x - move
        player.facing = "left"
        game_window.blit(game_surface, (0, 0))
        self.draw_player()

    def move_up(self, move):
        self.y = self.y - move
        player.facing = "up"
        game_window.blit(game_surface, (0, 0))
        self.draw_player()

    def move_down(self, move):
        self.y = self.y + move
        player.facing = "down"
        game_window.blit(game_surface, (0, 0))
        self.draw_player()

    def start_position(self):
        random_spot = random.choice(player_start_coordinates)
        self.x, self.y = random_spot[0], random_spot[1]
        if player.y == 10:
            if player.x == 10:
                player.facing = "right"
            else:
                player.facing = "down"
        elif player.y == 760:
            if player.x == 10:
                player.facing = "right"
            else:
                player.facing = "up"
        else:
            player.facing = "right"


# Ghost related answer finding mechanics
UP = (0, 125)
DOWN = (0, -125)
LEFT = (-125, 0)
RIGHT = (125, 0)
move_coordinates = [UP, DOWN, LEFT, RIGHT]
solution = False


def choose_a_direction():
    return random.choice(move_coordinates)


def find_a_way():
    move = choose_a_direction()
    if ghost_player.x + (move[0]) == answer.x + 75 and ghost_player.y + (move[1]) == answer.y + 200:
        move_list.append(move)
        global solution
        solution = True
    elif ghost_player.x + move[0] < 0 or ghost_player.x + move[0] > 1100 or \
            ghost_player.y + move[1] < 0 or ghost_player.y + move[1] > 800:
        find_a_way()
    else:
        if ghost_player.facing == "up" and move == (0, 125):
            find_a_way()
        elif ghost_player.facing == "down" and move == (0, -125):
            find_a_way()
        elif ghost_player.facing == "left" and move == (125, 0):
            find_a_way()
        elif ghost_player.facing == "right" and move == (-125, 0):
            find_a_way()
        else:
            move_list.append(move)
            ghost_player.x, ghost_player.y = ghost_player.x + move[0] + move[0], ghost_player.y + move[1] + move[1]
            if move == (125, 0):
                ghost_player.facing = "right"
            elif move == (-125, 0):
                ghost_player.facing = "left"
            elif move == (0, 125):
                ghost_player.facing = "down"
            elif move == (0, -125):
                ghost_player.facing = "up"


def reset():
    global move_list
    global solution
    global move_list_string
    global move_variable
    global score
    score = increase_score()
    player.start_position()
    ghost_player.x, ghost_player.y, ghost_player.facing = player.x, player.y, player.facing
    move_list = []
    move_list_string = []
    move_variable = 0
    solution = False


def increase_move_variable():
    return move_variable + 1


def stop_sounds():
    pygame.mixer.Sound.stop(go_straight)
    pygame.mixer.Sound.stop(turn_left)
    pygame.mixer.Sound.stop(turn_right)


def play_direction_sound():
    if player.facing == "up":
        if move_list_string[move_variable] == "up":
            stop_sounds()
            pygame.mixer.Sound.play(go_straight)
        elif move_list_string[move_variable] == "left":
            stop_sounds()
            pygame.mixer.Sound.play(turn_left)
        elif move_list_string[move_variable] == "right":
            stop_sounds()
            pygame.mixer.Sound.play(turn_right)
    elif player.facing == "down":
        if move_list_string[move_variable] == "left":
            stop_sounds()
            pygame.mixer.Sound.play(turn_right)
        elif move_list_string[move_variable] == "right":
            stop_sounds()
            pygame.mixer.Sound.play(turn_left)
        elif move_list_string[move_variable] == "down":
            stop_sounds()
            pygame.mixer.Sound.play(go_straight)
    elif player.facing == "left":
        if move_list_string[move_variable] == "up":
            stop_sounds()
            pygame.mixer.Sound.play(turn_right)
        elif move_list_string[move_variable] == "left":
            stop_sounds()
            pygame.mixer.Sound.play(go_straight)
        elif move_list_string[move_variable] == "down":
            stop_sounds()
            pygame.mixer.Sound.play(turn_left)
    elif player.facing == "right":
        if move_list_string[move_variable] == "up":
            stop_sounds()
            pygame.mixer.Sound.play(turn_left)
        elif move_list_string[move_variable] == "right":
            stop_sounds()
            pygame.mixer.Sound.play(go_straight)
        elif move_list_string[move_variable] == "down":
            stop_sounds()
            pygame.mixer.Sound.play(turn_right)


score = 0


def increase_score():
    return score + 1


def display_score():
    scoreboard = font.render(f"Score:  {score}", True, (0, 0, 0), )
    # high_score_font = font.render(f"High Score: {high_score}", True, (0, 0, 0), )
    game_window.blit(scoreboard, (10, 800))
    # game_window.blit(high_score_font, (10, 900))


def display_health():
    display_score()
    if health == 5:
        pygame.draw.rect(game_window, (255, 255, 255), (550, 840, 500, 500))
        game_window.blit(heart, (1000, 850))
        game_window.blit(heart, (890, 850))
        game_window.blit(heart, (780, 850))
        game_window.blit(heart, (670, 850))
        game_window.blit(heart, (560, 850))
    elif health == 4:
        pygame.draw.rect(game_window, (255, 255, 255), (550, 840, 800, 500))
        game_window.blit(heart, (890, 850))
        game_window.blit(heart, (780, 850))
        game_window.blit(heart, (670, 850))
        game_window.blit(heart, (560, 850))
    elif health == 3:
        pygame.draw.rect(game_window, (255, 255, 255), (550, 840, 800, 500))
        game_window.blit(heart, (780, 850))
        game_window.blit(heart, (670, 850))
        game_window.blit(heart, (560, 850))
    elif health == 2:
        pygame.draw.rect(game_window, (255, 255, 255), (550, 840, 800, 500))
        game_window.blit(heart, (670, 850))
        game_window.blit(heart, (560, 850))
    elif health == 1:
        pygame.draw.rect(game_window, (255, 255, 255), (550, 840, 800, 500))
        game_window.blit(heart, (560, 850))
    pygame.display.update()


def alter_health():
    return health - 1


def alter_moves_remaining():
    return moves_remaining - 1


def display_menu():
    game_window.blit(game_surface, (0, 0))
    pygame.draw.rect(game_window, (127, 255, 127), (500, 50, 700, 900))
    pygame.draw.rect(game_window, BLACK, (500, 50, 700, 900), 7)
    menu_button_1.draw_button()
    menu_button_2.draw_button()
    menu_title = header_font.render("Main Menu", True, (0, 0, 0), )
    game_window.blit(menu_title, (584, 100))
    game_type_font_1 = font.render("Commands", True, (0, 0, 0), )
    game_window.blit(game_type_font_1, (510, 350))
    game_type_font_2 = font.render("Guidance", True, (0, 0, 0), )
    game_window.blit(game_type_font_2, (510, 650))
    pygame.display.update()


move_list = []
move_list_string = []
move_variable = 0
building_coordinates = [(60, 60), (310, 60), (560, 60), (810, 60), (1060, 60), (60, 310), (310, 310), (560, 310),
                        (810, 310), (1060, 310), (60, 560), (310, 560), (560, 560), (810, 560), (1060, 560)]
player_start_coordinates = [(10, 10), (260, 10), (510, 10), (760, 10), (1010, 10), (10, 260), (10, 510), (10, 760),
                            (260, 760), (510, 760), (760, 760)]
coordinate_mirror = building_coordinates
player = Player()
health = 5
ghost_player = Player()


running = True
game_state = "menu"

while running:
    high_score = 0
    ev = pygame.event.get()
    if health == 0:
        score = 0
        health = 5
        game_state = "menu"
    if game_state == "menu":
        display_menu()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button_1.rect.collidepoint(event.pos):
                    menu_selection = 1
                    player.start_position()
                    ghost_player.x, ghost_player.y = player.x, player.y
                    random.shuffle(building_coordinates)
                    building_list = [
                        Building(building_coordinates[x][0], building_coordinates[x][1], random.choice(color_list))
                        for x in range(15)]
                    game_state = "a"
                if menu_button_2.rect.collidepoint(event.pos):
                    menu_selection = 2
                    player.start_position()
                    ghost_player.x, ghost_player.y = player.x, player.y
                    random.shuffle(building_coordinates)
                    building_list = [
                        Building(building_coordinates[x][0], building_coordinates[x][1], random.choice(color_list))
                        for x in range(15)]
                    game_state = "a"
    elif game_state == "a":
        game_window.blit(game_surface, (0, 0))
        player.draw_player()
        answer = random.choice(building_list)
        answer.color = (120, 120, 120)
        for items in building_list:
            items.draw_building()
        pygame.display.update()
        game_state = "b"
    elif game_state == "b":
        if solution:
            for moves in move_list:
                if moves == (125, 0):
                    move_list_string.append("right")
                elif moves == (-125, 0):
                    move_list_string.append("left")
                elif moves == (0, 125):
                    move_list_string.append("down")
                elif moves == (0, -125):
                    move_list_string.append("up")
            game_state = "sound"
        else:
            if len(move_list) > 8:
                move_list = []
                ghost_player.x, ghost_player.y = player.x, player.y
            else:
                find_a_way()
    elif game_state == "sound":
        if menu_selection == 1:
            play_direction_sound()
            game_state = "Game: commands"
        elif menu_selection == 2:
            moves_remaining = 8
            game_state = "Game: directions"
# Game Mode 1
    elif game_state == "Game: commands":
        display_health()
        player.draw_player()
        pygame.display.update()
        for event in ev:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if move_list_string[move_variable] == "right":
                        player.move_right(MOVE_DISTANCE)
                        if player.x > 1150:
                            player.move_left(MOVE_DISTANCE)
                        elif player.x == answer.x + 75 and player.y == answer.y + 200:
                            reset()
                            game_state = "a"
                        else:
                            player.move_right(MOVE_DISTANCE)
                            move_variable = increase_move_variable()
                            game_state = "sound"
                    else:
                        health = alter_health()
                        display_health()
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_a:
                    if move_list_string[move_variable] == "left":
                        player.move_left(MOVE_DISTANCE)
                        if player.x < 0:
                            player.move_right(MOVE_DISTANCE)
                        elif player.x == answer.x + 75 and player.y == answer.y + 200:
                            reset()
                            game_state = "a"
                        else:
                            player.move_left(MOVE_DISTANCE)
                            move_variable = increase_move_variable()
                            game_state = "sound"
                    else:
                        health = alter_health()
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_w:
                    if move_list_string[move_variable] == "up":
                        player.move_up(MOVE_DISTANCE)
                        if player.y < 0:
                            player.move_down(MOVE_DISTANCE)
                        elif player.x == answer.x + 75 and player.y == answer.y + 200:
                            reset()
                            # answer.color = random.choice(color_list)
                            game_state = "a"
                        else:
                            player.move_up(MOVE_DISTANCE)
                            move_variable = increase_move_variable()
                            game_state = "sound"
                    else:
                        health = alter_health()
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_s:
                    if move_list_string[move_variable] == "down":
                        player.move_down(MOVE_DISTANCE)
                        if player.y > 800:
                            player.move_up(MOVE_DISTANCE)
                        elif player.x == answer.x + 75 and player.y == answer.y + 200:
                            reset()
                            # answer.color = random.choice(color_list)
                            game_state = "a"
                        else:
                            player.move_down(MOVE_DISTANCE)
                            move_variable = increase_move_variable()
                            game_state = "sound"
                    else:
                        health = alter_health()
                    for items in building_list:
                        items.draw_building()
            if event.type == pygame.QUIT:
                running = False
# Game Mode 2
    elif game_state == "Game: directions":
        display_score()
        player.draw_player()
        pygame.display.update()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.move_right(MOVE_DISTANCE)
                    if player.x > 1150:
                        player.move_left(MOVE_DISTANCE)
                    elif player.x == answer.x + 75 and player.y == answer.y + 200:
                        reset()
                        game_state = "a"
                    else:
                        player.move_right(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_a:
                    player.move_left(MOVE_DISTANCE)
                    if player.x < 0:
                        player.move_right(MOVE_DISTANCE)
                    elif player.x == answer.x + 75 and player.y == answer.y + 200:
                        reset()
                        game_state = "a"
                    else:
                        player.move_left(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_w:
                    player.move_up(MOVE_DISTANCE)
                    if player.y < 0:
                        player.move_down(MOVE_DISTANCE)
                    elif player.x == answer.x + 75 and player.y == answer.y + 200:
                        reset()
                        game_state = "a"
                    else:
                        player.move_up(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_s:
                    player.move_down(MOVE_DISTANCE)
                    if player.y > 800:
                        player.move_up(MOVE_DISTANCE)
                    elif player.x == answer.x + 75 and player.y == answer.y + 200:
                        reset()
                        # answer.color = random.choice(color_list)
                        game_state = "a"
                    else:
                        player.move_down(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
            elif moves_remaining == 0:
                score = 0
                game_state = "menu"

# TODO
# add a timer
# figure out where it might be best to put the display health
