import pygame
import random
import ctypes
import os

# Stop Windows scaling and center the display
ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.mixer.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
if screen_width == 1280:
    window_width, window_height = screen_width-495, screen_height - 300
    resize_factor = (1/2)
elif screen_width == 1680:
    window_width, window_height = screen_width - 110, screen_height - 60
    resize_factor = 1
else:
    window_width, window_height = screen_width - 350, screen_height - 60
    resize_factor = 1
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Direction Game")
game_surface = pygame.Surface((2000, 2000))
game_surface.fill((255, 255, 255))
game_window.blit(game_surface, (0, 0))

# Clock
clock = pygame.time.Clock()
counter, text = 10, "10".rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Constants
IMAGE_SIZE = (int(200*resize_factor), int(200*resize_factor))
MOVE_DISTANCE = 125*resize_factor
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
go_straight = pygame.mixer.Sound("audio/straight.ogg")
turn_left = pygame.mixer.Sound("audio/left.ogg")
turn_right = pygame.mixer.Sound("audio/right.ogg")

bookstore_audio = pygame.mixer.Sound("audio/bookstore.ogg")
combini_audio = pygame.mixer.Sound("audio/combini.ogg")
department_audio = pygame.mixer.Sound("audio/department.ogg")
firestation_audio = pygame.mixer.Sound("audio/firestation.ogg")
flowershop_audio = pygame.mixer.Sound("audio/flowershop.ogg")
gasstation_audio = pygame.mixer.Sound("audio/gasstation.ogg")
gym_audio = pygame.mixer.Sound("audio/gym.ogg")
hospital_audio = pygame.mixer.Sound("audio/hospital.ogg")
library_audio = pygame.mixer.Sound("audio/library.ogg")
park_audio = pygame.mixer.Sound("audio/park.ogg")
police_audio = pygame.mixer.Sound("audio/police.ogg")
postoffice_audio = pygame.mixer.Sound("audio/postoffice.ogg")
restaurant_audio = pygame.mixer.Sound("audio/restaurant.ogg")
school_audio = pygame.mixer.Sound("audio/school.ogg")
station_audio = pygame.mixer.Sound("audio/station.ogg")
supermarket_audio = pygame.mixer.Sound("audio/supermarket.ogg")
temple_audio = pygame.mixer.Sound("audio/temple.ogg")
zoo_audio = pygame.mixer.Sound("audio/zoo.ogg")

# Audio lists
bookstore_list = [bookstore_audio]
combini_list = [combini_audio]
department_list = [department_audio]
firestation_list = [firestation_audio]
flowershop_list = [flowershop_audio]
gasstation_list = [gasstation_audio]
gym_list = [gym_audio]
hospital_list = [hospital_audio]
library_list = [library_audio]
park_list = [park_audio]
police_list = [police_audio]
postoffice_list = [postoffice_audio]
restaurant_list = [restaurant_audio]
school_list = [school_audio]
station_list = [station_audio]
supermarket_list = [supermarket_audio]
temple_list = [temple_audio]
zoo_list = [zoo_audio]



# Pictures
road_raw = pygame.image.load("pictures/road_test.png")
road = pygame.transform.scale(road_raw, (int(300*resize_factor), int(300*resize_factor)))
heart_raw = pygame.image.load("pictures/heart.png")
heart = pygame.transform.scale(heart_raw, (int(100*resize_factor), int(100*resize_factor)))
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
font = pygame.font.Font(None, int(60*resize_factor))
header_font = pygame.font.Font(None, int(140*resize_factor))
timer_font = pygame.font.Font(None, int(150*resize_factor))


class Building:
    def __init__(self, x, y, pic):
        self.x = x
        self.y = y
        self.pic = pic
        self.audio = "hrng"
        self.rect = pygame.Rect(self.x, self.y, 200*resize_factor, 200*resize_factor)

    def assign_word(self):
        if self.pic == bookstore:
            self.audio = random.choice(bookstore_list)
        elif self.pic == combini:
            self.audio = random.choice(combini_list)
        elif self.pic == department:
            self.audio = random.choice(department_list)
        elif self.pic == firestation:
            self.audio = random.choice(firestation_list)
        elif self.pic == flowershop:
            self.audio = random.choice(flowershop_list)
        elif self.pic == gasstation:
            self.audio = random.choice(gasstation_list)
        elif self.pic == gym:
            self.audio = random.choice(gym_list)
        elif self.pic == hospital:
            self.audio = random.choice(hospital_list)
        elif self.pic == library:
            self.audio = random.choice(library_list)
        elif self.pic == park:
            self.audio = random.choice(park_list)
        elif self.pic == police:
            self.audio = random.choice(police_list)
        elif self.pic == postoffice:
            self.audio = random.choice(postoffice_list)
        elif self.pic == restaurant:
            self.audio = random.choice(restaurant_list)
        elif self.pic == school:
            self.audio = random.choice(school_list)
        elif self.pic == station:
            self.audio = random.choice(station_list)
        elif self.pic == supermarket:
            self.audio = random.choice(supermarket_list)
        elif self.pic == temple:
            self.audio = random.choice(temple_list)
        elif self.pic == zoo:
            self.audio = random.choice(zoo_list)

    def draw_building(self):
        game_window.blit(road, (self.x - 50*resize_factor, self.y - 50*resize_factor))
        pygame.draw.rect(game_window, (0, 0, 0), (self.x, self.y, 200*resize_factor, 200*resize_factor))
        game_window.blit(self.pic, (self.x, self.y), )
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, 200*resize_factor, 200*resize_factor), 3)


class Button:
    def __init__(self, x, y):
        self.color = (220, 50, 113)
        self.x = x*resize_factor
        self.y = y*resize_factor
        self.width = 600*resize_factor
        self.height = 180*resize_factor
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)


menu_button_1 = Button(485, 230)
menu_button_2 = Button(485, 480)
menu_button_3 = Button(485, 730)
return_to_menu_button = Button(485, 830)
return_to_menu_button.height = 150
return_to_menu_button.color = (220, 120, 50)


class Player:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.facing = ""
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, 50*resize_factor, 50*resize_factor)

    def draw_player(self):
        if player.facing == "right":
            pygame.draw.rect(game_window, self.color, (self.x, self.y + 9*resize_factor, 50*resize_factor, 30*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x, self.y + 9*resize_factor, 50*resize_factor, 30*resize_factor), 3)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 40*resize_factor, self.y + 10*resize_factor, 8*resize_factor, 8*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x + 40*resize_factor, self.y + 10*resize_factor, 8*resize_factor, 8*resize_factor), 1)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 40*resize_factor, self.y + 30*resize_factor, 8*resize_factor, 8*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x + 40*resize_factor, self.y + 30*resize_factor, 8*resize_factor, 8*resize_factor), 1)

        elif player.facing == "left":
            pygame.draw.rect(game_window, self.color, (self.x, self.y + 9*resize_factor, 50*resize_factor, 30*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x, self.y + 9*resize_factor, 50*resize_factor, 30*resize_factor), 3)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 2*resize_factor, self.y + 10*resize_factor, 8*resize_factor, 8*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x + 2*resize_factor, self.y + 10*resize_factor, 8*resize_factor, 8*resize_factor), 1)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 2*resize_factor, self.y + 30*resize_factor, 8*resize_factor, 8*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x + 2*resize_factor, self.y + 30*resize_factor, 8*resize_factor, 8*resize_factor), 1)

        elif player.facing == "up":
            pygame.draw.rect(game_window, self.color, (self.x + 9*resize_factor, self.y, 30*resize_factor, 50*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x + 9*resize_factor, self.y, 30*resize_factor, 50*resize_factor), 3)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 10*resize_factor, self.y + 2*resize_factor, 8*resize_factor, 8*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x + 10*resize_factor, self.y + 2*resize_factor, 8*resize_factor, 8*resize_factor), 1)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 30*resize_factor, self.y + 2*resize_factor, 8*resize_factor, 8*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x + 30*resize_factor, self.y + 2*resize_factor, 8*resize_factor, 8*resize_factor), 1)
        elif player.facing == "down":
            pygame.draw.rect(game_window, self.color, (self.x + 9*resize_factor, self.y, 30*resize_factor, 50*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x + 9*resize_factor, self.y, 30*resize_factor, 50*resize_factor), 3)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 10*resize_factor, self.y + 40*resize_factor, 8*resize_factor, 8*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x + 10*resize_factor, self.y + 40*resize_factor, 8*resize_factor, 8*resize_factor), 1)
            pygame.draw.rect(game_window, (255, 255, 0), (self.x + 30*resize_factor, self.y + 40*resize_factor, 8*resize_factor, 8*resize_factor))
            pygame.draw.rect(game_window, BLACK, (self.x + 30*resize_factor, self.y + 40*resize_factor, 8*resize_factor, 8*resize_factor), 1)

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
        elif player.y == 10+750*resize_factor:
            if player.x == 10:
                player.facing = "right"
            else:
                player.facing = "up"
        else:
            player.facing = "right"


# Ghost related answer finding mechanics
UP = (0, MOVE_DISTANCE)
DOWN = (0, -MOVE_DISTANCE)
LEFT = (-MOVE_DISTANCE, 0)
RIGHT = (MOVE_DISTANCE, 0)
move_coordinates = [UP, DOWN, LEFT, RIGHT]
solution = False


def choose_a_direction():
    return random.choice(move_coordinates)


def find_a_way():
    move = choose_a_direction()
    if ghost_player.x + (move[0]) == answer.x + 75*resize_factor and ghost_player.y + (move[1]) == answer.y + 200*resize_factor:
        move_list.append(move)
        global solution
        solution = True
    elif ghost_player.x + move[0] < 0 or ghost_player.x + move[0] > 1550*resize_factor or \
            ghost_player.y + move[1] < 0 or ghost_player.y + move[1] > 800*resize_factor:
        find_a_way()
    else:
        if ghost_player.facing == "up" and move == (0, MOVE_DISTANCE):
            find_a_way()
        elif ghost_player.facing == "down" and move == (0, -MOVE_DISTANCE):
            find_a_way()
        elif ghost_player.facing == "left" and move == (MOVE_DISTANCE, 0):
            find_a_way()
        elif ghost_player.facing == "right" and move == (-MOVE_DISTANCE, 0):
            find_a_way()
        else:
            move_list.append(move)
            ghost_player.x, ghost_player.y = ghost_player.x + move[0] + move[0], ghost_player.y + move[1] + move[1]
            if move == (MOVE_DISTANCE, 0):
                ghost_player.facing = "right"
            elif move == (-MOVE_DISTANCE, 0):
                ghost_player.facing = "left"
            elif move == (0, MOVE_DISTANCE):
                ghost_player.facing = "down"
            elif move == (0, -MOVE_DISTANCE):
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
high_score = 0
high_score_2 = 0


def increase_score():
    global high_score
    global high_score_2
    if menu_selection == 1:
        if score + 1 > high_score:
            high_score = score + 1
    if menu_selection == 2:
        if score + 1 > high_score_2:
            high_score_2 = score + 1
    return score + 1


def display_score():
    scoreboard = font.render(f"Score:  {score}", True, (0, 0, 0), )
    if menu_selection == 1:
        high_score_font = font.render(f"High Score: {high_score}", True, (0, 0, 0), )
        game_window.blit(high_score_font, (10, 880*resize_factor))
    elif menu_selection == 2:
        high_score_2_font = font.render(f"High Score: {high_score_2}", True, (0, 0, 0), )
        game_window.blit(high_score_2_font, (10, 880*resize_factor))
    game_window.blit(scoreboard, (10, 830*resize_factor))


def display_health():
    display_score()
    if health == 5:
        pygame.draw.rect(game_window, (255, 255, 255), (550*resize_factor, 840*resize_factor, 500*resize_factor, 500*resize_factor))
        game_window.blit(heart, (1000*resize_factor, 850*resize_factor))
        game_window.blit(heart, (890*resize_factor, 850*resize_factor))
        game_window.blit(heart, (780*resize_factor, 850*resize_factor))
        game_window.blit(heart, (670*resize_factor, 850*resize_factor))
        game_window.blit(heart, (560*resize_factor, 850*resize_factor))
    elif health == 4:
        pygame.draw.rect(game_window, (255, 255, 255), (550*resize_factor, 840*resize_factor, 800*resize_factor, 500*resize_factor))
        game_window.blit(heart, (890*resize_factor, 850*resize_factor))
        game_window.blit(heart, (780*resize_factor, 850*resize_factor))
        game_window.blit(heart, (670*resize_factor, 850*resize_factor))
        game_window.blit(heart, (560*resize_factor, 850*resize_factor))
    elif health == 3:
        pygame.draw.rect(game_window, (255, 255, 255), (550*resize_factor, 840*resize_factor, 800*resize_factor, 500*resize_factor))
        game_window.blit(heart, (780*resize_factor, 850*resize_factor))
        game_window.blit(heart, (670*resize_factor, 850*resize_factor))
        game_window.blit(heart, (560*resize_factor, 850*resize_factor))
    elif health == 2:
        pygame.draw.rect(game_window, (255, 255, 255), (550*resize_factor, 840*resize_factor, 800*resize_factor, 500*resize_factor))
        game_window.blit(heart, (670*resize_factor, 850*resize_factor))
        game_window.blit(heart, (560*resize_factor, 850*resize_factor))
    elif health == 1:
        pygame.draw.rect(game_window, (255, 255, 255), (550*resize_factor, 840*resize_factor, 800*resize_factor, 500*resize_factor))
        game_window.blit(heart, (560*resize_factor, 850*resize_factor))
    pygame.display.update()


def alter_health():
    return health - 1


def alter_moves_remaining():
    return moves_remaining - 1


def display_menu():
    game_window.blit(game_surface, (0, 0))
    pygame.draw.rect(game_window, (127, 255, 127), (435*resize_factor, 50*resize_factor, 700*resize_factor, 900*resize_factor))
    pygame.draw.rect(game_window, BLACK, (435*resize_factor, 50*resize_factor, 700*resize_factor, 900*resize_factor), 7)
    menu_button_1.draw_button()
    menu_button_2.draw_button()
    menu_button_3.draw_button()
    menu_title = header_font.render("Main Menu", True, (0, 0, 0), )
    game_window.blit(menu_title, (520*resize_factor, 70*resize_factor))
    game_type_font_1 = font.render("Commands", True, (0, 0, 0), )
    game_window.blit(game_type_font_1, (600*resize_factor, 180*resize_factor))
    game_type_font_2 = font.render("Guidance", True, (0, 0, 0), )
    game_window.blit(game_type_font_2, (600*resize_factor, 430*resize_factor))
    game_window.blit(font.render("Practice", True, (0, 0, 0), ), (600*resize_factor, 680*resize_factor))
    pygame.display.update()


move_list = []
move_list_string = []
move_variable = 0
building_base_coordinate = (10+50*resize_factor)
building_coordinates = [(building_base_coordinate, building_base_coordinate),
                        (building_base_coordinate+250*resize_factor, building_base_coordinate),
                        (building_base_coordinate+500*resize_factor, building_base_coordinate),
                        (building_base_coordinate+750*resize_factor, building_base_coordinate),
                        (building_base_coordinate+1000*resize_factor, building_base_coordinate),
                        (building_base_coordinate+1250*resize_factor, building_base_coordinate),
                        (building_base_coordinate, building_base_coordinate+250*resize_factor),
                        (building_base_coordinate+250*resize_factor, building_base_coordinate+250*resize_factor),
                        (building_base_coordinate+500*resize_factor, building_base_coordinate+250*resize_factor),
                        (building_base_coordinate+750*resize_factor, building_base_coordinate+250*resize_factor),
                        (building_base_coordinate+1000*resize_factor, building_base_coordinate+250*resize_factor),
                        (building_base_coordinate+1250*resize_factor, building_base_coordinate+250*resize_factor),
                        (building_base_coordinate, building_base_coordinate+500*resize_factor),
                        (building_base_coordinate+250*resize_factor, building_base_coordinate+500*resize_factor),
                        (building_base_coordinate+500*resize_factor, building_base_coordinate+500*resize_factor),
                        (building_base_coordinate+750*resize_factor, building_base_coordinate+500*resize_factor),
                        (building_base_coordinate+1000*resize_factor, building_base_coordinate+500*resize_factor),
                        (building_base_coordinate + 1250*resize_factor, building_base_coordinate+500*resize_factor)]
player_start_coordinates = [(10, 10), (10+250*resize_factor, 10), (10+500*resize_factor, 10), (10+750*resize_factor, 10),
                            (10+1000*resize_factor, 10), (10+1250*resize_factor, 10), (10, 10+250*resize_factor),
                            (10, 10+500*resize_factor),
                            (10, 10+750*resize_factor), (10+250*resize_factor, 10+750*resize_factor),
                            (10+500*resize_factor, 10+750*resize_factor), (10+750*resize_factor, 10+750*resize_factor),
                            (10+1000*resize_factor, 10+750*resize_factor), (10+1250*resize_factor, 10)]
coordinate_mirror = building_coordinates
player = Player()
health = 5
ghost_player = Player()


running = True
game_state = "menu"

while running:
    ev = pygame.event.get()
    if health == 0 or counter == 0:
        score = 0
        counter = 22
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
                    solution = False
                    move_variable = 0
                    move_list = []
                    move_list_string = []
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
                if menu_button_3.rect.collidepoint(event.pos):
                    menu_selection = 3
                    solution = True
                    random.shuffle(building_coordinates)
                    building_list = [
                        Building(building_coordinates[x][0], building_coordinates[x][1], picture_list[x])
                        for x in range(18)]
                    for buildings in building_list:
                        buildings.assign_word()
                        game_state = "b"
    elif game_state == "a":
        game_window.blit(game_surface, (0, 0))
        answer = random.choice(building_list)
        pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
        for items in building_list:
            items.draw_building()
        player.draw_player()
        pygame.display.update()
        game_state = "b"
    elif game_state == "b":
        if menu_selection == 1:
            if solution:
                for moves in move_list:
                    if moves == (MOVE_DISTANCE, 0):
                        move_list_string.append("right")
                    elif moves == (-MOVE_DISTANCE, 0):
                        move_list_string.append("left")
                    elif moves == (0, MOVE_DISTANCE):
                        move_list_string.append("down")
                    elif moves == (0, -MOVE_DISTANCE):
                        move_list_string.append("up")
                game_state = "sound"
            else:
                if len(move_list) > 13:
                    move_list = []
                    ghost_player.x, ghost_player.y = player.x, player.y
                else:
                    find_a_way()
        elif menu_selection == 2:
            game_state = "sound"
        elif menu_selection == 3:
            game_window.blit(game_surface, (0, 0))
            pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
            return_to_menu_button.draw_button()
            for items in building_list:
                items.draw_building()
            pygame.display.update()
            game_state = "practice"
    elif game_state == "practice":
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_menu_button.rect.collidepoint(event.pos):
                    game_state = "menu"
                for buildings in building_list:
                    if buildings.rect.collidepoint(event.pos):
                        pygame.mixer.Sound.play(buildings.audio)
                        buildings.assign_word()
            if event.type == pygame.QUIT:
                running = False
    elif game_state == "sound":
        if menu_selection == 1:
            play_direction_sound()
            game_state = "Game: commands"
        elif menu_selection == 2:
            pygame.mixer.Sound.play(answer.audio)
            if score < 5:
                counter = 22
            elif score < 10:
                counter = 17
            elif score < 15:
                counter = 12
            else:
                counter = 7
            moves_remaining = 10
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
                        if player.x > 1550*resize_factor:
                            player.move_left(MOVE_DISTANCE)
                        elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                            reset()
                            game_state = "a"
                        else:
                            player.move_right(MOVE_DISTANCE)
                            move_variable = increase_move_variable()
                            game_state = "sound"
                    else:
                        health = alter_health()
                        display_health()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_a:
                    if move_list_string[move_variable] == "left":
                        player.move_left(MOVE_DISTANCE)
                        if player.x < 0:
                            player.move_right(MOVE_DISTANCE)
                        elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                            reset()
                            game_state = "a"
                        else:
                            player.move_left(MOVE_DISTANCE)
                            move_variable = increase_move_variable()
                            game_state = "sound"
                    else:
                        health = alter_health()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_w:
                    if move_list_string[move_variable] == "up":
                        player.move_up(MOVE_DISTANCE)
                        if player.y < 0:
                            player.move_down(MOVE_DISTANCE)
                        elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                            reset()
                            # answer.color = random.choice(color_list)
                            game_state = "a"
                        else:
                            player.move_up(MOVE_DISTANCE)
                            move_variable = increase_move_variable()
                            game_state = "sound"
                    else:
                        health = alter_health()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_s:
                    if move_list_string[move_variable] == "down":
                        player.move_down(MOVE_DISTANCE)
                        if player.y > 800:
                            player.move_up(MOVE_DISTANCE)
                        elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                            reset()
                            # answer.color = random.choice(color_list)
                            game_state = "a"
                        else:
                            player.move_down(MOVE_DISTANCE)
                            move_variable = increase_move_variable()
                            game_state = "sound"
                    else:
                        health = alter_health()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
            if event.type == pygame.QUIT:
                running = False
# Game Mode 2
    elif game_state == "Game: directions":
        # winning_font_boys = font.render(f"{answer.word}", True, (0, 0, 0), )
        # game_window.blit(winning_font_boys, (300, 900))
        display_moves_remaining = font.render(f"{moves_remaining} moves left", True, (0, 0, 0), )
        game_window.blit(display_moves_remaining, (650*resize_factor, 850*resize_factor))
        if score < 5:
            if counter <= 20:
                clock_text = str(counter).rjust(3) if counter > 0 else "boom!"
                pygame.draw.rect(game_window, (255, 255, 255), (1000*resize_factor, 850*resize_factor, 200*resize_factor, 200*resize_factor))
                game_window.blit(timer_font.render(clock_text, True, (0, 0, 0)), (1000*resize_factor, 850*resize_factor))
        elif score < 10:
            if counter <= 15:
                clock_text = str(counter).rjust(3) if counter > 0 else "boom!"
                pygame.draw.rect(game_window, (255, 255, 255), (1000*resize_factor, 850*resize_factor, 200*resize_factor, 200*resize_factor))
                game_window.blit(timer_font.render(clock_text, True, (0, 0, 0)), (1000*resize_factor, 850*resize_factor))
        elif score < 15:
            if counter <= 10:
                clock_text = str(counter).rjust(3) if counter > 0 else "boom!"
                pygame.draw.rect(game_window, (255, 255, 255), (1000*resize_factor, 850*resize_factor, 200*resize_factor, 200*resize_factor))
                game_window.blit(timer_font.render(clock_text, True, (0, 0, 0)), (1000*resize_factor, 850*resize_factor))
        else:
            if counter <= 5:
                clock_text = str(counter).rjust(3) if counter > 0 else "boom!"
                pygame.draw.rect(game_window, (255, 255, 255), (1000*resize_factor, 850*resize_factor, 200*resize_factor, 200*resize_factor))
                game_window.blit(timer_font.render(clock_text, True, (0, 0, 0)), (1000*resize_factor, 850*resize_factor))
        display_score()
        player.draw_player()
        pygame.display.update()
        for event in ev:
            if event.type == pygame.USEREVENT:
                counter -= 1
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.move_right(MOVE_DISTANCE)
                    if player.x > 1550*resize_factor:
                        player.move_left(MOVE_DISTANCE)
                    elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                        reset()
                        game_state = "a"
                    else:
                        player.move_right(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_a:
                    player.move_left(MOVE_DISTANCE)
                    if player.x < 0:
                        player.move_right(MOVE_DISTANCE)
                    elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                        reset()
                        game_state = "a"
                    else:
                        player.move_left(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_w:
                    player.move_up(MOVE_DISTANCE)
                    if player.y < 0:
                        player.move_down(MOVE_DISTANCE)
                    elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                        reset()
                        game_state = "a"
                    else:
                        player.move_up(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_s:
                    player.move_down(MOVE_DISTANCE)
                    if player.y > 800*resize_factor:
                        player.move_up(MOVE_DISTANCE)
                    elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                        reset()
                        game_state = "a"
                    else:
                        player.move_down(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
            elif moves_remaining == 0:
                score = 0
                menu_selection = 0
                game_state = "menu"

# TODO

# Make lists containing multiple recordings of the same location
# Make a list of different directions (turn left, turn right, go straight) spoken by at least one other person
# Make the high scores available at the main screen
# Make some kind of sound or something that occurs when you get a point so that the kids know they did something right
