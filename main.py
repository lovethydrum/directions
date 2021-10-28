import pygame
import random

pygame.init()
pygame.mixer.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
game_window = pygame.display.set_mode((screen_width-350, screen_height-60))
pygame.display.set_caption("Direction Game")
game_surface = pygame.Surface((2000, 2000))
game_surface.fill((255, 255, 255))
game_window.blit(game_surface, (0, 0))


# Constants
IMAGE_SIZE = (200, 200)
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
road = pygame.image.load("pictures/road_test.png")

heart_raw = pygame.image.load("heart.png")
heart = pygame.transform.scale(heart_raw, (100, 100))
bookstore_raw = pygame.image.load("pictures/bookstore.png")
bookstore = pygame.transform.scale(bookstore_raw, IMAGE_SIZE)
combini_raw = pygame.image.load("pictures/combini.png")
combini = pygame.transform.scale(combini_raw, IMAGE_SIZE)
department_raw = pygame.image.load("pictures/department.png")
department = pygame.transform.scale(department_raw, IMAGE_SIZE)
firestation_raw = pygame.image.load("pictures/firestation.png")
firestation = pygame.transform.scale(firestation_raw, IMAGE_SIZE)
flowershop_raw = pygame.image.load("pictures/flowershop.png")
flowershop = pygame.transform.scale(flowershop_raw, IMAGE_SIZE)
gasstation_raw = pygame.image.load("pictures/gasstation.png")
gasstation = pygame.transform.scale(gasstation_raw, IMAGE_SIZE)
gym_raw = pygame.image.load("pictures/gym.png")
gym = pygame.transform.scale(gym_raw, IMAGE_SIZE)
hospital_raw = pygame.image.load("pictures/hospital.png")
hospital = pygame.transform.scale(hospital_raw, IMAGE_SIZE)
library_raw = pygame.image.load("pictures/library.png")
library = pygame.transform.scale(library_raw, IMAGE_SIZE)
park_raw = pygame.image.load("pictures/park.png")
park = pygame.transform.scale(park_raw, IMAGE_SIZE)
police_raw = pygame.image.load("pictures/police.png")
police = pygame.transform.scale(police_raw, IMAGE_SIZE)
postoffice_raw = pygame.image.load("pictures/postoffice.png")
postoffice = pygame.transform.scale(postoffice_raw, IMAGE_SIZE)
restaurant_raw = pygame.image.load("pictures/restaurant.png")
restaurant = pygame.transform.scale(restaurant_raw, IMAGE_SIZE)
school_raw = pygame.image.load("pictures/school.png")
school = pygame.transform.scale(school_raw, IMAGE_SIZE)
station_raw = pygame.image.load("pictures/station.png")
station = pygame.transform.scale(station_raw, IMAGE_SIZE)
supermarket_raw = pygame.image.load("pictures/supermarket.png")
supermarket = pygame.transform.scale(supermarket_raw, IMAGE_SIZE)
temple_raw = pygame.image.load("pictures/temple.png")
temple = pygame.transform.scale(temple_raw, IMAGE_SIZE)
zoo_raw = pygame.image.load("pictures/zoo.png")
zoo = pygame.transform.scale(zoo_raw, IMAGE_SIZE)

picture_list = [bookstore, combini, department, firestation, flowershop, gasstation, gym, hospital, library, park,
                police, postoffice, restaurant, school, station, supermarket, temple, zoo]
# Font
font = pygame.font.Font(None, 60)
header_font = pygame.font.Font(None, 140)


class Building:
    def __init__(self, x, y, pic):
        self.x = x
        self.y = y
        self.pic = pic
        self.word = "hrng"
        self.rect = pygame.Rect(self.x, self.y, 200, 200)

    def assign_word(self):
        if self.pic == bookstore:
            self.word = "bookstore"
        elif self.pic == combini:
            self.word = "combini"
        elif self.pic == department:
            self.word = "department"
        elif self.pic == firestation:
            self.word = "firestation"
        elif self.pic == flowershop:
            self.word = "flowershop"
        elif self.pic == gasstation:
            self.word = "gasstation"
        elif self.pic == gym:
            self.word = "gym"
        elif self.pic == hospital:
            self.word = "hospital"
        elif self.pic == library:
            self.word = "library"
        elif self.pic == park:
            self.word = "park"
        elif self.pic == police:
            self.word = "police"
        elif self.pic == postoffice:
            self.word = "postoffice"
        elif self.pic == restaurant:
            self.word = "restaurant"
        elif self.pic == school:
            self.word = "school"
        elif self.pic == station:
            self.word = "station"
        elif self.pic == supermarket:
            self.word = "supermarket"
        elif self.pic == temple:
            self.word = "temple"
        elif self.pic == zoo:
            self.word = "zoo"

    def draw_building(self):
        game_window.blit(road, (self.x - 50, self.y - 50))
        pygame.draw.rect(game_window, (0, 0, 0), (self.x, self.y, 200, 200))
        game_window.blit(self.pic, (self.x, self.y), )
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, 200, 200), 3)


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


menu_button_1 = Button(485, 350)
menu_button_2 = Button(485, 650)


class Player:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.facing = ""
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def draw_player(self):
        if player.facing == "right":
            pygame.draw.rect(game_window, self.color, (self.x, self.y + 9, 50, 30))
            pygame.draw.rect(game_window, BLACK, (self.x, self.y + 9, 50, 30), 3)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 40, self.y + 10, 8, 8))
            pygame.draw.rect(game_window, BLACK, (self.x + 40, self.y + 10, 8, 8), 1)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 40, self.y + 30, 8, 8))
            pygame.draw.rect(game_window, BLACK, (self.x + 40, self.y + 30, 8, 8), 1)

        elif player.facing == "left":
            pygame.draw.rect(game_window, self.color, (self.x, self.y + 9, 50, 30))
            pygame.draw.rect(game_window, BLACK, (self.x, self.y + 9, 50, 30), 3)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 2, self.y + 10, 8, 8))
            pygame.draw.rect(game_window, BLACK, (self.x + 2, self.y + 10, 8, 8), 1)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 2, self.y + 30, 8, 8))
            pygame.draw.rect(game_window, BLACK, (self.x + 2, self.y + 30, 8, 8), 1)

        elif player.facing == "up":
            pygame.draw.rect(game_window, self.color, (self.x + 9, self.y, 30, 50))
            pygame.draw.rect(game_window, BLACK, (self.x + 9, self.y, 30, 50), 3)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 10, self.y + 2, 8, 8))
            pygame.draw.rect(game_window, BLACK, (self.x + 10, self.y + 2, 8, 8), 1)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 30, self.y + 2, 8, 8))
            pygame.draw.rect(game_window, BLACK, (self.x + 30, self.y + 2, 8, 8), 1)
        elif player.facing == "down":
            pygame.draw.rect(game_window, self.color, (self.x + 9, self.y, 30, 50))
            pygame.draw.rect(game_window, BLACK, (self.x + 9, self.y, 30, 50), 3)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 10, self.y + 40, 8, 8))
            pygame.draw.rect(game_window, BLACK, (self.x + 10, self.y + 40, 8, 8), 1)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 30, self.y + 40, 8, 8))
            pygame.draw.rect(game_window, BLACK, (self.x + 30, self.y + 40, 8, 8), 1)

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
    elif ghost_player.x + move[0] < 0 or ghost_player.x + move[0] > 1550 or \
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
    if menu_selection == 1:
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
    game_window.blit(scoreboard, (10, 900))
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
    pygame.draw.rect(game_window, (127, 255, 127), (435, 50, 700, 900))
    pygame.draw.rect(game_window, BLACK, (435, 50, 700, 900), 7)
    menu_button_1.draw_button()
    menu_button_2.draw_button()
    menu_title = header_font.render("Main Menu", True, (0, 0, 0), )
    game_window.blit(menu_title, (520, 100))
    game_type_font_1 = font.render("Commands", True, (0, 0, 0), )
    game_window.blit(game_type_font_1, (455, 300))
    game_type_font_2 = font.render("Guidance", True, (0, 0, 0), )
    game_window.blit(game_type_font_2, (455, 600))
    pygame.display.update()


move_list = []
move_list_string = []
move_variable = 0
building_coordinates = [(60, 60), (310, 60), (560, 60), (810, 60), (1060, 60), (1310, 60),
                        (60, 310), (310, 310), (560, 310), (810, 310), (1060, 310), (1310, 310),
                        (60, 560), (310, 560), (560, 560), (810, 560), (1060, 560), (1310, 560)]
player_start_coordinates = [(10, 10), (260, 10), (510, 10), (760, 10), (1010, 10), (1260, 10), (10, 260),
                            (10, 510), (10, 760), (260, 760), (510, 760), (760, 760), (1010, 760), (1260, 10)]
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
                    random.shuffle(picture_list)
                    building_list = [
                        Building(building_coordinates[x][0], building_coordinates[x][1], picture_list[x])
                        for x in range(18)]
                    game_state = "a"
                if menu_button_2.rect.collidepoint(event.pos):
                    solution = True
                    menu_selection = 2
                    player.start_position()
                    random.shuffle(building_coordinates)
                    building_list = [
                        Building(building_coordinates[x][0], building_coordinates[x][1], picture_list[x])
                        for x in range(18)]
                    for buildings in building_list:
                        buildings.assign_word()
                    game_state = "a"
    elif game_state == "a":
        game_window.blit(game_surface, (0, 0))
        answer = random.choice(building_list)
        pygame.draw.rect(game_window, BLACK, (0, 0, 1570, 810), 20)
        for items in building_list:
            items.draw_building()
        player.draw_player()
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
            if len(move_list) > 13:
                move_list = []
                ghost_player.x, ghost_player.y = player.x, player.y
            else:
                find_a_way()
    elif game_state == "sound":
        if menu_selection == 1:
            play_direction_sound()
            game_state = "Game: commands"
        elif menu_selection == 2:
            moves_remaining = 9
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
                        if player.x > 1550:
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
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570, 810), 20)
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
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570, 810), 20)
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
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570, 810), 20)
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
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570, 810), 20)
                    for items in building_list:
                        items.draw_building()
            if event.type == pygame.QUIT:
                running = False
# Game Mode 2
    elif game_state == "Game: directions":
        winning_font_boys = font.render(f"{answer.word}", True, (0, 0, 0), )
        # high_score_font = font.render(f"High Score: {high_score}", True, (0, 0, 0), )
        game_window.blit(winning_font_boys, (300, 900))
        display_moves_remaining = font.render(f"{moves_remaining} moves left", True, (0, 0, 0), )
        game_window.blit(display_moves_remaining, (600, 900))
        display_score()
        player.draw_player()
        pygame.display.update()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.move_right(MOVE_DISTANCE)
                    if player.x > 1550:
                        player.move_left(MOVE_DISTANCE)
                    elif player.x == answer.x + 75 and player.y == answer.y + 200:
                        reset()
                        game_state = "a"
                    else:
                        player.move_right(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570, 810), 20)
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
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570, 810), 20)
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
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570, 810), 20)
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
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570, 810), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
            elif moves_remaining == 0:
                score = 0
                game_state = "menu"

# TODO
# Record "I want to go to dokodoko"
# Make my road pretty
# High Score
