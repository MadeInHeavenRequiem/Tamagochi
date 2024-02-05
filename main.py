class Critter(object):
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        if 5 <= self.hunger <= 10:
            m = 'нормально'
        elif 11 <= self.hunger <= 15:
            m = 'не так уж и хорошо'
        elif self.hunger > 15:
            m = 'ужасно'
        else:
            m = 'прекрасно'
        return m

    def talk(self):
        print('Меня зовут', self.name, ", и сейчас я чувствую себя", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food=4):
        print('Ммм... Спасибо!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print('Уииии!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input('Какое имя вы хотите дать своему питомцу? ')
    return Critter(crit_name)

crit = main()

choise = None
while choise != "0":
    print \
    ('''Моя зверюшка 
      0 - Выйти
      1 - Узнать самочувствие зверюшки
      2 - Покормить зверюшку
      3 - Поиграть со зверюшкой
      ''')
    choise = input("Ваш выбор: ")
    print()
    if choise == "0":
        print("Хорошо, вы оставили своего питомца на верную смерть. До свидания")
        break
    elif choise == "1":
        crit.talk()
    elif choise == "2":
        crit.eat()
    elif choise == "3":
        crit.play()
    else:
        print("Извините, такого варианта нет")
