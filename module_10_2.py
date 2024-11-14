from time import sleep
from threading import Thread

class Knight(Thread):

    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name} на нас напали!')
        day = 0
        enemies = 100
        while enemies > 0:
            sleep(1)
            day += 1
            enemies -= self.power
            print(f'{self.name} сражается {day} день(дня), осталось {enemies} воинов')
            if enemies < 0:
                enemies = 0
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")

def main():
    knight1 = Knight('Sir Lancelot', 10) # power- сколько воинов может победить в день
    knight2 = Knight("Sir Galahad", 20)
    knight1.start()
    knight2.start()
    knight1.join()
    knight2.join()
    print('Битвы окончены.')



if __name__ == '__main__':
    main()

