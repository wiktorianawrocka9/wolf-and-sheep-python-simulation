import random
import math

class Wolf:
    def __init__(self):
        self.x=0.0
        self.y=0.0
    def move_wolf(self, wolf_move_dist, nearest_sheep_index, nearest_sheep_distance, sheep):
        self.x += wolf_move_dist * ((sheep[nearest_sheep_index].x - self.x) / nearest_sheep_distance)    
        self.y += wolf_move_dist * ((sheep[nearest_sheep_index].y - self.y) / nearest_sheep_distance)  
        # print(sheep[nearest_sheep_index].x)
        # print(sheep[nearest_sheep_index].y)  
    def get_wolf_coordinates(self):
        #"{:.3f}" sluzy do wyswietlenia wspolrzednych wilka z trzema miejscami po przecinku
        print("{:.3f}".format(self.x))
        print("{:.3f}".format(self.y))

class Sheep:
    def __init__(self):
        #wspolrzednie owcy w obszarze (-10,10)
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
            #print("to jest polnoc")
            self.y += sheep_move_dist
        elif random_direction == "west":
            #print("to jest zachod")
            self.x -= sheep_move_dist
        elif random_direction == "east":
            #print("to jest wschod")
            self.x += sheep_move_dist
        else:
            #print("to jest poludnie")
            self.y -= sheep_move_dist

def round(number_rounds, wolf, sheep, wolf_move_dist):
    #liczenie dystansu miedzy wilkiem i owcami
    distances_wolf_sheep = []
    for single_sheep in sheep:
        distances_wolf_sheep.append(math.sqrt(((single_sheep.x - wolf.x) ** 2) + ((single_sheep.y - wolf.y) ** 2)))
    #wybor najblizszej owcy, znalezienie jej indeksu
    nearest_sheep_distance = min(distances_wolf_sheep)
    nearest_sheep_index = distances_wolf_sheep.index(min(distances_wolf_sheep))
    #sprawdzenie czy wilk może pożreć najbliższą owcę:
    if min(distances_wolf_sheep) < wolf_move_dist:
        print("wilk zjada owcę!")
        del sheep[nearest_sheep_index]
        print("byla to owca o indeksie: ")
        print(nearest_sheep_index)
    else:
        wolf.move_wolf(wolf_move_dist, nearest_sheep_index, nearest_sheep_distance, sheep)

def main():
    sheep_move_dist = 0.5
    number_sheep = 15
    wolf_move_dist = 1
    number_rounds = 50

    wolf = Wolf()

    #dodawanie owiec do tablicy sheep
    sheep = []
    i=0
    while i < number_sheep:
        sheep.append(Sheep())
        i+=1

    #rozgrywka
    print("informacje o rundzie:")
    j = 0
    while j < number_rounds:
        round(number_rounds, wolf, sheep, wolf_move_dist)
        print("numer tury: ")
        print(j)
        print("wspolrzedne wilka: ")
        wolf.get_wolf_coordinates()
        print("ilosc owiec, ktore zyja:")
        print(len(sheep))
        if(len(sheep)) == 0:
            break
        j+=1

if __name__ == '__main__':
    main()