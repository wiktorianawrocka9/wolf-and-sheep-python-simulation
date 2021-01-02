import random
import math

class Wolf:
    def __init__(self):
        self.x=0.0
        self.y=0.0
    def get_wolf_coordinates(self):
        print(self.x)
        print(self.y)
        

class Sheep:
    def __init__(self):
        self.init_pos_limit=random.uniform(0, 1)*10
        self.x = -(self.init_pos_limit)
        self.y = self.init_pos_limit
    def get_sheep_coordinates(self):
        print(self.x)
        print(self.y)
    def move_sheep(self, sheep_move_dist):
        directions = ["north", "west", "east", "south"]
        random.shuffle(directions)
        random_direction = directions[0]
        if random_direction == "north":
            print("to jest polnoc")
            self.y += sheep_move_dist
        elif random_direction == "west":
            print("to jest zachod")
            self.x -= sheep_move_dist
        elif random_direction == "east":
            print("to jest wschod")
            self.x += sheep_move_dist
        else:
            print("to jest poludnie")
            self.y -= sheep_move_dist

def round(number_rounds, wolf, sheep, wolf_move_dist):
    print("ROZGRYWKA!!!")
    #liczenie dystansu miedzy wilkiem i owcami
    distances_wolf_sheep = []
    for single_sheep in sheep:
        distances_wolf_sheep.append(math.sqrt(((single_sheep.x - wolf.x) ** 2) + ((single_sheep.y - wolf.y) ** 2)))
    #wybor najblizszej owcy, znalezienie jej indeksu
    nearest_sheep_distance = min(distances_wolf_sheep)
    nearest_sheep_index = distances_wolf_sheep.index(min(distances_wolf_sheep))
    print(distances_wolf_sheep)
    print(nearest_sheep_index)
    print(nearest_sheep_distance)
    #sprawdzenie czy wilk może pożreć najbliższą owcę:
    if min(distances_wolf_sheep) < wolf_move_dist:
        print("wilk zjada owcę!")
        del sheep[nearest_sheep_index]
    else:
        print("owca nadal zyje")

def main():
    sheep_move_dist = 0.5
    number_sheep = 3
    wolf_move_dist = 1
    number_rounds = 50

    wolf = Wolf()

    sheep = []
    i=0
    while i < number_sheep:
        sheep.append(Sheep())
        i+=1

    j=0
    while j < number_sheep:
        sheep[j].get_sheep_coordinates()
        j += 1  

    round(number_rounds, wolf, sheep, wolf_move_dist)


if __name__ == '__main__':
    main()