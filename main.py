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
    window_width, window_height = screen_width-495, screen_height - 280
    resize_factor = (1/2)
elif screen_width == 1680:
    window_width, window_height = screen_width - 110, screen_height - 60
    resize_factor = 1/2
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
ding = pygame.mixer.Sound("audio/ding.ogg")
go_straight_man_1 = pygame.mixer.Sound("audio/go_straight_man_1.ogg")
turn_left_man_1 = pygame.mixer.Sound("audio/turn_left_man_1.ogg")
turn_right_man_1 = pygame.mixer.Sound("audio/turn_right_man_1.ogg")
go_straight_man_2 = pygame.mixer.Sound("audio/go_straight_man_2.ogg")
turn_left_man_2 = pygame.mixer.Sound("audio/turn_left_man_2.ogg")
turn_right_man_2 = pygame.mixer.Sound("audio/turn_right_man_2.ogg")
go_straight_woman_1 = pygame.mixer.Sound("audio/go_straight_woman.ogg")
turn_left_woman_1 = pygame.mixer.Sound("audio/turn_left_woman.ogg")
turn_right_woman_1 = pygame.mixer.Sound("audio/turn_right_woman.ogg")
go_straight_woman_2 = pygame.mixer.Sound("audio/go_straight_woman_2.ogg")
turn_left_woman_2 = pygame.mixer.Sound("audio/turn_left_woman_2.ogg")
turn_right_woman_2 = pygame.mixer.Sound("audio/turn_right_woman_2.ogg")

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

bookstore_jordan = pygame.mixer.Sound("audio/jordan/bookstore_jordan.ogg")
combini_jordan = pygame.mixer.Sound("audio/jordan/combini_jordan.ogg")
department_jordan = pygame.mixer.Sound("audio/jordan/department_jordan.ogg")
firestation_jordan = pygame.mixer.Sound("audio/jordan/firestation_jordan.ogg")
flowershop_jordan = pygame.mixer.Sound("audio/jordan/flowershop_jordan.ogg")
gasstation_jordan = pygame.mixer.Sound("audio/jordan/gasstation_jordan.ogg")
gym_jordan = pygame.mixer.Sound("audio/jordan/gym_jordan.ogg")
hospital_jordan = pygame.mixer.Sound("audio/jordan/hospital_jordan.ogg")
library_jordan = pygame.mixer.Sound("audio/jordan/library_jordan.ogg")
park_jordan = pygame.mixer.Sound("audio/jordan/park_jordan.ogg")
police_jordan = pygame.mixer.Sound("audio/jordan/police_jordan.ogg")
postoffice_jordan = pygame.mixer.Sound("audio/jordan/postoffice_jordan.ogg")
restaurant_jordan = pygame.mixer.Sound("audio/jordan/restaurant_jordan.ogg")
school_jordan = pygame.mixer.Sound("audio/jordan/school_jordan.ogg")
station_jordan = pygame.mixer.Sound("audio/jordan/station_jordan.ogg")
supermarket_jordan = pygame.mixer.Sound("audio/jordan/supermarket_jordan.ogg")
temple_jordan = pygame.mixer.Sound("audio/jordan/temple_jordan.ogg")
zoo_jordan = pygame.mixer.Sound("audio/jordan/zoo_jordan.ogg")

bookstore_joy = pygame.mixer.Sound("audio/joy/bookstore_joy.ogg")
combini_joy = pygame.mixer.Sound("audio/joy/combini_joy.ogg")
department_joy = pygame.mixer.Sound("audio/joy/department_joy.ogg")
firestation_joy = pygame.mixer.Sound("audio/joy/firestation_joy.ogg")
flowershop_joy = pygame.mixer.Sound("audio/joy/flowershop_joy.ogg")
gasstation_joy = pygame.mixer.Sound("audio/joy/gasstation_joy.ogg")
gym_joy = pygame.mixer.Sound("audio/joy/gym_joy.ogg")
hospital_joy = pygame.mixer.Sound("audio/joy/hospital_joy.ogg")
library_joy = pygame.mixer.Sound("audio/joy/library_joy.ogg")
park_joy = pygame.mixer.Sound("audio/joy/park_joy.ogg")
police_joy = pygame.mixer.Sound("audio/joy/police_joy.ogg")
postoffice_joy = pygame.mixer.Sound("audio/joy/postoffice_joy.ogg")
restaurant_joy = pygame.mixer.Sound("audio/joy/restaurant_joy.ogg")
school_joy = pygame.mixer.Sound("audio/joy/school_joy.ogg")
station_joy = pygame.mixer.Sound("audio/joy/station_joy.ogg")
supermarket_joy = pygame.mixer.Sound("audio/joy/supermarket_joy.ogg")
temple_joy = pygame.mixer.Sound("audio/joy/temple_joy.ogg")
zoo_joy = pygame.mixer.Sound("audio/joy/zoo_joy.ogg")

bookstore_shantilly = pygame.mixer.Sound("audio/shantilly/bookstore_shantilly.ogg")
combini_shantilly = pygame.mixer.Sound("audio/shantilly/combini_shantilly.ogg")
department_shantilly = pygame.mixer.Sound("audio/shantilly/department_shantilly.ogg")
firestation_shantilly = pygame.mixer.Sound("audio/shantilly/firestation_shantilly.ogg")
flowershop__shantilly = pygame.mixer.Sound("audio/shantilly/flowershop_shantilly.ogg")
gasstation_shantilly = pygame.mixer.Sound("audio/shantilly/gasstation_shantilly.ogg")
gym_shantilly = pygame.mixer.Sound("audio/shantilly/gym_shantilly.ogg")
hospital_shantilly = pygame.mixer.Sound("audio/shantilly/hospital_shantilly.ogg")
library_shantilly = pygame.mixer.Sound("audio/shantilly/library_shantilly.ogg")
park_shantilly = pygame.mixer.Sound("audio/shantilly/park_shantilly.ogg")
police_shantilly = pygame.mixer.Sound("audio/shantilly/police_shantilly.ogg")
postoffice_shantilly = pygame.mixer.Sound("audio/shantilly/postoffice_shantilly.ogg")
restaurant_shantilly = pygame.mixer.Sound("audio/shantilly/restaurant_shantilly.ogg")
school_shantilly = pygame.mixer.Sound("audio/shantilly/school_shantilly.ogg")
station_shantilly = pygame.mixer.Sound("audio/shantilly/station_shantilly.ogg")
supermarket_shantilly = pygame.mixer.Sound("audio/shantilly/supermarket_shantilly.ogg")
temple_shantilly = pygame.mixer.Sound("audio/shantilly/temple_shantilly.ogg")
zoo_shantilly = pygame.mixer.Sound("audio/shantilly/zoo_shantilly.ogg")

# Audio lists
building_audio_dictionary = {
    "bookstore": [bookstore_audio, bookstore_jordan, bookstore_joy, bookstore_shantilly],
    "combini": [combini_audio, combini_jordan, combini_joy, combini_shantilly],
    "department": [department_audio, department_jordan, department_joy, department_shantilly],
    "firestation": [firestation_audio, firestation_jordan, firestation_joy, firestation_shantilly],
    "flowershop": [flowershop_audio, flowershop_jordan, flowershop_joy, flowershop__shantilly],
    "gasstation": [gasstation_audio, gasstation_jordan, gasstation_joy, gasstation_shantilly],
    "gym": [gym_audio, gym_jordan, gym_joy, gym_shantilly],
    "hospital": [hospital_audio, hospital_jordan, hospital_joy, hospital_shantilly],
    "library": [library_audio, library_jordan, library_joy, library_shantilly],
    "park": [park_audio, park_jordan, park_joy, park_shantilly],
    "police": [police_audio, police_jordan, police_joy, police_shantilly],
    "postoffice": [postoffice_audio, postoffice_jordan, postoffice_joy, postoffice_shantilly],
    "restaurant": [restaurant_audio, restaurant_jordan, restaurant_joy, restaurant_shantilly],
    "school": [school_audio, school_jordan, school_joy, school_shantilly],
    "station": [station_audio, station_jordan, station_joy, station_shantilly],
    "supermarket": [supermarket_audio, supermarket_jordan, supermarket_joy, supermarket_shantilly],
    "temple": [temple_audio, temple_jordan, temple_joy, temple_shantilly],
    "zoo": [zoo_audio, zoo_jordan, zoo_joy, zoo_shantilly],

}

directions_dictionary = {
    "man 1": [turn_left_man_1, turn_right_man_1, go_straight_man_1],
    "woman 1": [turn_left_woman_1, turn_right_woman_1, go_straight_woman_1],
    "man 2": [turn_left_man_2, turn_right_man_2, go_straight_man_2],
    "woman 2": [turn_left_woman_2, turn_right_woman_2, go_straight_woman_2]
}
man_or_woman = ["woman 1", "man 1", "woman 2", "man 2"]
practice_2_random_list = [
    "bookstore", "combini", "department", "firestation", "flowershop", "gasstation", "gym", "hospital", "library",
    "park", "police", "postoffice", "restaurant", "school", "station", "supermarket", "temple", "zoo", "man 1", "man 2",
    "woman 1", "woman 2"
]

# Pictures
commands_raw = pygame.image.load("pictures/commands.png")
commands = pygame.transform.scale(commands_raw, (int(600*resize_factor), int(180*resize_factor)))
guidance_raw = pygame.image.load("pictures/guidance.png")
guidance = pygame.transform.scale(guidance_raw, (int(580*resize_factor), int(178*resize_factor)))
modoru_raw = pygame.image.load("pictures/modoru.png")
modoru = pygame.transform.scale(modoru_raw, IMAGE_SIZE)
turn_left_raw = pygame.image.load("pictures/turn_left.png")
turn_left_img = pygame.transform.scale(turn_left_raw, (int(214*resize_factor), int(112*resize_factor)))
turn_right_raw = pygame.image.load("pictures/turn_right.png")
turn_right_img = pygame.transform.scale(turn_right_raw, (int(214*resize_factor), int(112*resize_factor)))
go_straight_raw = pygame.image.load("pictures/go_straight.png")
go_straight_img = pygame.transform.scale(go_straight_raw, (int(112*resize_factor), int(172*resize_factor)))
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
        self.name = ""
        self.rect = pygame.Rect(self.x, self.y, 200*resize_factor, 200*resize_factor)

    def assign_word(self):
        if self.pic == bookstore:
            self.audio = random.choice(building_audio_dictionary["bookstore"])
            self.name = "bookstore"
        elif self.pic == combini:
            self.audio = random.choice(building_audio_dictionary["combini"])
            self.name = "combini"
        elif self.pic == department:
            self.audio = random.choice(building_audio_dictionary["department"])
            self.name = "department"
        elif self.pic == firestation:
            self.audio = random.choice(building_audio_dictionary["firestation"])
            self.name = "firestation"
        elif self.pic == flowershop:
            self.audio = random.choice(building_audio_dictionary["flowershop"])
            self.name = "flowershop"
        elif self.pic == gasstation:
            self.audio = random.choice(building_audio_dictionary["gasstation"])
            self.name = "gasstation"
        elif self.pic == gym:
            self.audio = random.choice(building_audio_dictionary["gym"])
            self.name = "gym"
        elif self.pic == hospital:
            self.audio = random.choice(building_audio_dictionary["hospital"])
            self.name = "hospital"
        elif self.pic == library:
            self.audio = random.choice(building_audio_dictionary["library"])
            self.name = "library"
        elif self.pic == park:
            self.audio = random.choice(building_audio_dictionary["park"])
            self.name = "park"
        elif self.pic == police:
            self.audio = random.choice(building_audio_dictionary["police"])
            self.name = "police"
        elif self.pic == postoffice:
            self.audio = random.choice(building_audio_dictionary["postoffice"])
            self.name = "postoffice"
        elif self.pic == restaurant:
            self.audio = random.choice(building_audio_dictionary["restaurant"])
            self.name = "restaurant"
        elif self.pic == school:
            self.audio = random.choice(building_audio_dictionary["school"])
            self.name = "school"
        elif self.pic == station:
            self.audio = random.choice(building_audio_dictionary["station"])
            self.name = "station"
        elif self.pic == supermarket:
            self.audio = random.choice(building_audio_dictionary["supermarket"])
            self.name = "supermarket"
        elif self.pic == temple:
            self.audio = random.choice(building_audio_dictionary["temple"])
            self.name = "temple"
        elif self.pic == zoo:
            self.audio = random.choice(building_audio_dictionary["zoo"])
            self.name = "zoo"

    def draw_building(self):
        game_window.blit(road, (self.x - 50*resize_factor, self.y - 50*resize_factor))
        pygame.draw.rect(game_window, (0, 0, 0), (self.x, self.y, 200*resize_factor, 200*resize_factor))
        game_window.blit(self.pic, (self.x, self.y), )
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, 200*resize_factor, 200*resize_factor), 3)
        pygame.draw.rect(game_window, BLACK, (self.x + 80*resize_factor, self.y + 192*resize_factor, 40*resize_factor, 6*resize_factor))


class Button:
    def __init__(self, x, y):
        self.color = (220, 50, 113)
        self.x = x*resize_factor
        self.y = y*resize_factor
        self.width = 600*resize_factor
        self.height = 180*resize_factor
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)


menu_button_1 = Button(485, 230)
menu_button_2 = Button(485, 480)
menu_button_3 = Button(485, 730)
menu_button_4 = Button(1200, 800)
menu_button_4.height = 100*resize_factor
menu_button_4.width = 100*resize_factor
return_to_menu_button = Button(20, 830)
return_to_menu_button.height = 180*resize_factor
return_to_menu_button.width = 180*resize_factor
return_to_menu_button.color = (220, 120, 50)
one_more_time_button = Button(1350, 830)
one_more_time_button.width = 180*resize_factor
one_more_time_button.height = 180*resize_factor
turn_left_button = Button(479, 830)
turn_left_button.width = 214*resize_factor
turn_left_button.height = 112*resize_factor
turn_right_button = Button(877, 830)
turn_right_button.width = 214*resize_factor
turn_right_button.height = 112*resize_factor
go_straight_button = Button(729, 830)
go_straight_button.width = 112*resize_factor
go_straight_button.height = 172*resize_factor


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


def random_voice():
    global voice_select
    random_speaker = random.choice(man_or_woman)
    if random_speaker == voice_select:
        random_voice()
    else:
        voice_select = random_speaker


def reset():
    global move_list
    global solution
    global move_list_string
    global move_variable
    global score
    random_voice()
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
    pygame.mixer.Sound.stop(ding)
    pygame.mixer.Sound.stop(go_straight_man_1)
    pygame.mixer.Sound.stop(go_straight_man_2)
    pygame.mixer.Sound.stop(go_straight_woman_1)
    pygame.mixer.Sound.stop(go_straight_woman_2)
    pygame.mixer.Sound.stop(turn_left_man_1)
    pygame.mixer.Sound.stop(turn_left_man_2)
    pygame.mixer.Sound.stop(turn_left_woman_1)
    pygame.mixer.Sound.stop(turn_left_woman_2)
    pygame.mixer.Sound.stop(turn_right_man_1)
    pygame.mixer.Sound.stop(turn_right_man_2)
    pygame.mixer.Sound.stop(turn_right_woman_1)
    pygame.mixer.Sound.stop(turn_right_woman_2)
    for buildings in building_list:
        pygame.mixer.Sound.stop(buildings.audio)


def play_direction_sound():
    global voice_select
    if player.facing == "up":
        if move_list_string[move_variable] == "up":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][2])
        elif move_list_string[move_variable] == "left":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][0])
        elif move_list_string[move_variable] == "right":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][1])
    elif player.facing == "down":
        if move_list_string[move_variable] == "left":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][1])
        elif move_list_string[move_variable] == "right":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][0])
        elif move_list_string[move_variable] == "down":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][2])
    elif player.facing == "left":
        if move_list_string[move_variable] == "up":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][1])
        elif move_list_string[move_variable] == "left":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][2])
        elif move_list_string[move_variable] == "down":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][0])
    elif player.facing == "right":
        if move_list_string[move_variable] == "up":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][0])
        elif move_list_string[move_variable] == "right":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][2])
        elif move_list_string[move_variable] == "down":
            stop_sounds()
            pygame.mixer.Sound.play(directions_dictionary[voice_select][1])


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


# noinspection PyTypeChecker
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
    global high_score
    global high_score_2

    game_window.blit(game_surface, (0, 0))
    pygame.draw.rect(game_window, (127, 255, 127), (435*resize_factor, 50*resize_factor, 700*resize_factor, 900*resize_factor))
    pygame.draw.rect(game_window, BLACK, (435*resize_factor, 50*resize_factor, 700*resize_factor, 900*resize_factor), 7)
    menu_button_1.draw_button()
    game_window.blit(commands, (menu_button_1.x, menu_button_1.y))
    menu_button_2.draw_button()
    game_window.blit(guidance, (menu_button_2.x+6, menu_button_2.y))
    menu_button_3.draw_button()
    menu_button_4.draw_button()
    menu_title = header_font.render("Main Menu", True, (0, 0, 0), )
    game_window.blit(menu_title, (520*resize_factor, 70*resize_factor))
    game_type_font_1 = font.render("Commands", True, (0, 0, 0), )
    game_window.blit(game_type_font_1, (484*resize_factor, 180*resize_factor))
    game_window.blit(font.render(f"High Score:  {high_score}", True, (0, 0, 0),), (812*resize_factor, 180*resize_factor))
    game_window.blit(font.render(f"High Score:  {high_score_2}", True, (0, 0, 0),), (812*resize_factor, 430*resize_factor))
    game_type_font_2 = font.render("Guidance", True, (0, 0, 0), )
    game_window.blit(game_type_font_2, (484*resize_factor, 430*resize_factor))
    game_window.blit(font.render("Practice", True, (0, 0, 0), ), (484*resize_factor, 680*resize_factor))
    pygame.display.update()


def score_menu():
    pygame.mixer.Sound.play(ding)
    game_window.blit(game_surface, (0, 0))
    game_window.blit(timer_font.render(f"Next Question...", True, (0, 0, 0), ),
                     (400 * resize_factor, 450 * resize_factor))
    pygame.display.update()
    pygame.time.delay(1300)


def level_up_menu():
    pygame.mixer.Sound.play(ding)
    pygame.time.delay(100)
    pygame.mixer.Sound.play(ding)
    pygame.time.delay(100)
    pygame.mixer.Sound.play(ding)
    game_window.blit(game_surface, (0, 0))
    game_window.blit(timer_font.render(f"LEVEL UP SCREEN HERE", True, (0, 0, 0), ),
                     (200 * resize_factor, 450 * resize_factor))
    pygame.display.update()
    pygame.time.delay(1000)


def game_over_menu():
    game_window.blit(game_surface, (0, 0))
    game_window.blit(timer_font.render(f"Game Over!", True, (0, 0, 0), ), (450 * resize_factor, 450 * resize_factor))
    pygame.display.update()
    pygame.time.delay(2000)


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
        game_state = "game over"
    if game_state == "menu":
        display_menu()
        voice_select = random.choice(man_or_woman)
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
                    for buildings in building_list:
                        buildings.assign_word()
                    game_state = "transition"
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
                    game_state = "transition"
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
                if menu_button_4.rect.collidepoint(event.pos):
                    menu_selection = 4
                    solution = True
                    random.shuffle(building_coordinates)
                    building_list = [
                        Building(building_coordinates[x][0], building_coordinates[x][1], picture_list[x])
                        for x in range(18)]
                    for buildings in building_list:
                        buildings.assign_word()
                        game_state = "b"
    elif game_state == "transition":
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
            turn_left_button.draw_button()
            turn_right_button.draw_button()
            go_straight_button.draw_button()
            game_window.blit(modoru, (10*resize_factor, 830*resize_factor))
            game_window.blit(turn_left_img, (479*resize_factor, 830*resize_factor))
            game_window.blit(turn_right_img, (877*resize_factor, 830*resize_factor))
            game_window.blit(go_straight_img, (729*resize_factor, 830*resize_factor))
            for items in building_list:
                items.draw_building()
            pygame.display.update()
            game_state = "practice"
        elif menu_selection == 4:
            random_key = random.choice(practice_2_random_list)
            if random_key == "man 1" or random_key == "man 2" or random_key == "woman 1" or random_key == "woman 2":
                dictionary = directions_dictionary
                practice_answer = random.choice(dictionary[random_key])
            else:
                dictionary = building_audio_dictionary
                practice_answer = random.choice(dictionary[random_key])
            pygame.mixer.Sound.play(practice_answer)
            game_window.blit(game_surface, (0, 0))
            pygame.draw.rect(game_window, BLACK, (0, 0, 1570 * resize_factor, 810 * resize_factor), 20)
            return_to_menu_button.draw_button()
            turn_left_button.draw_button()
            turn_right_button.draw_button()
            go_straight_button.draw_button()
            one_more_time_button.draw_button()
            game_window.blit(modoru, (10 * resize_factor, 830 * resize_factor))
            game_window.blit(turn_left_img, (479 * resize_factor, 830 * resize_factor))
            game_window.blit(turn_right_img, (877 * resize_factor, 830 * resize_factor))
            game_window.blit(go_straight_img, (729 * resize_factor, 830 * resize_factor))
            for items in building_list:
                items.draw_building()
                items.assign_word()
            pygame.display.update()
            game_state = "practice 2"
    elif game_state == "practice":
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_menu_button.rect.collidepoint(event.pos):
                    game_state = "menu"
                elif turn_left_button.rect.collidepoint(event.pos):
                    stop_sounds()
                    pygame.mixer.Sound.play(directions_dictionary[random.choice(man_or_woman)][0])
                elif turn_right_button.rect.collidepoint(event.pos):
                    stop_sounds()
                    pygame.mixer.Sound.play(directions_dictionary[random.choice(man_or_woman)][1])
                elif go_straight_button.rect.collidepoint(event.pos):
                    stop_sounds()
                    pygame.mixer.Sound.play(directions_dictionary[random.choice(man_or_woman)][2])
                for buildings in building_list:
                    if buildings.rect.collidepoint(event.pos):
                        stop_sounds()
                        buildings.assign_word()
                        stop_sounds()
                        pygame.mixer.Sound.play(buildings.audio)
            if event.type == pygame.QUIT:
                running = False
    elif game_state == "practice 2":
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_menu_button.rect.collidepoint(event.pos):
                    game_state = "menu"
                elif one_more_time_button.rect.collidepoint(event.pos):
                    stop_sounds()
                    pygame.mixer.Sound.play(practice_answer)
                elif turn_left_button.rect.collidepoint(event.pos):
                    stop_sounds()
                    for speakers in man_or_woman:
                        if directions_dictionary[speakers][0] == practice_answer:
                            pygame.mixer.Sound.play(ding)
                            print("yeah")
                            game_state = "score"
                        else:
                            print("nah")
                elif turn_right_button.rect.collidepoint(event.pos):
                    stop_sounds()
                    for speakers in man_or_woman:
                        if directions_dictionary[speakers][1] == practice_answer:
                            pygame.mixer.Sound.play(ding)
                            print("yeah")
                            game_state = "score"
                        else:
                            print("nah")
                elif go_straight_button.rect.collidepoint(event.pos):
                    stop_sounds()
                    for speakers in man_or_woman:
                        if directions_dictionary[speakers][2] == practice_answer:
                            pygame.mixer.Sound.play(ding)
                            print("yeah")
                            game_state = "score"
                        else:
                            print("nah")
                for buildings in building_list:
                    if buildings.rect.collidepoint(event.pos):
                        for items in building_audio_dictionary[buildings.name]:
                            if items == practice_answer:
                                pygame.mixer.Sound.play(ding)
                                print("yeah")
                                game_state = "score"
                            else:
                                print("nah")

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
    elif game_state == "score":
        if menu_selection == 2:
            level_up_menu()
            game_state = "transition"
        else:
            score_menu()
            game_state = "transition"
    elif game_state == "game over":
        game_over_menu()
        game_state = "menu"
# Game Mode 1
    elif game_state == "Game: commands":
        display_health()
        player.draw_player()
        pygame.display.update()
        for event in ev:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if move_list_string[move_variable] == "right":
                        player.move_right(MOVE_DISTANCE)
                        if player.x > 1550*resize_factor:
                            player.move_left(MOVE_DISTANCE)
                        elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                            reset()
                            game_state = "score"
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
                elif event.key == pygame.K_LEFT:
                    if move_list_string[move_variable] == "left":
                        player.move_left(MOVE_DISTANCE)
                        if player.x < 0:
                            player.move_right(MOVE_DISTANCE)
                        elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                            reset()
                            game_state = "score"
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
                elif event.key == pygame.K_UP:
                    if move_list_string[move_variable] == "up":
                        player.move_up(MOVE_DISTANCE)
                        if player.y < 0:
                            player.move_down(MOVE_DISTANCE)
                        elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                            reset()
                            game_state = "score"
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
                elif event.key == pygame.K_DOWN:
                    if move_list_string[move_variable] == "down":
                        player.move_down(MOVE_DISTANCE)
                        if player.y > 800:
                            player.move_up(MOVE_DISTANCE)
                        elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                            reset()
                            game_state = "score"
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
                if event.key == pygame.K_RIGHT:
                    player.move_right(MOVE_DISTANCE)
                    if player.x > 1550*resize_factor:
                        player.move_left(MOVE_DISTANCE)
                    elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                        reset()
                        if score == 5 or score == 10 or score == 15:
                            game_state = "score"
                        else:
                            game_state = "transition"
                    else:
                        player.move_right(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_LEFT:
                    player.move_left(MOVE_DISTANCE)
                    if player.x < 0:
                        player.move_right(MOVE_DISTANCE)
                    elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                        reset()
                        if score == 5 or score == 10 or score == 15:
                            game_state = "score"
                        else:
                            game_state = "transition"
                    else:
                        player.move_left(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_UP:
                    player.move_up(MOVE_DISTANCE)
                    if player.y < 0:
                        player.move_down(MOVE_DISTANCE)
                    elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                        reset()
                        if score == 5 or score == 10 or score == 15:
                            game_state = "score"
                        else:
                            game_state = "transition"
                    else:
                        player.move_up(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
                elif event.key == pygame.K_DOWN:
                    player.move_down(MOVE_DISTANCE)
                    if player.y > 800*resize_factor:
                        player.move_up(MOVE_DISTANCE)
                    elif player.x == answer.x + 75*resize_factor and player.y == answer.y + 200*resize_factor:
                        reset()
                        if score == 5 or score == 10 or score == 15:
                            game_state = "score"
                        else:
                            game_state = "transition"
                    else:
                        player.move_down(MOVE_DISTANCE)
                        moves_remaining = alter_moves_remaining()
                    pygame.draw.rect(game_window, BLACK, (0, 0, 1570*resize_factor, 810*resize_factor), 20)
                    for items in building_list:
                        items.draw_building()
                    pygame.display.update()
            elif moves_remaining <= 0:
                score = 0
                menu_selection = 0
                game_state = "game over"

# TODO

# Potential game changes:
# 1: Do we want to have a ding added to the directions game?
# 2: Do we want to have the Commands game say the direction again if they miss the direction?
# 3: Do we want different colors for the different practices?

# (I would really like some kind of original art for the opening menu) - Evan contacted

# Some kind of description on how to play each version of the game, built into the application
# Find a ding, game over, and level up sound
# Re-record your own voice files
# Normalize sound files



# STILL NEED TO FIX SHINKEISUIJAKU SELECTION BUG