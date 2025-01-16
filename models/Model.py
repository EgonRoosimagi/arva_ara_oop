from random import randint

from models.Stopwatch import Stopwatch


class Model:
    #defineerime klassi muutujad
    pc_nr = randint(1, 100)
    steps = 0
    game_over = False
    cheater = False
    stopwatch = Stopwatch()

    def __init__(self):
        self.reset_game()

    def reset_game(self):
        """Teeb uue mängu"""
        self.pc_nr = randint(1, 100) # juhuslik number
        self.steps = 0 #sammude arv
        self.game_over = False #mäng ei ole läbi
        self.cheater = False #mängija ei ole petja
        self.stopwatch.reset() #nullib stopperi
        self.stopwatch.start() #käivitab stopperi

    def ask(self):
        """Küsib nr ja kontrollib"""
        user_nr = int(input('Sisesta number: '))  # Küsi kasutajalt numbrit
        self.steps += 1

        if user_nr == 1000:
            self.cheater = True  # sa oled petja
            self.game_over = True  # mäng sai läbi
            self.stopwatch.stop()  # peata aeg
            print(f'Leidsid mu nõrga koha. Õige number oli {self.pc_nr}')
        elif user_nr > self.pc_nr:
            print('Väiksem')
        elif user_nr < self.pc_nr:
            print('Suurem')
        elif user_nr == self.pc_nr:
            self.game_over = True
            self.stopwatch.stop()
            print(f'Leidsid õige numbri {self.steps} sammuga')

    def lets_play(self):
        """Mängime mängu avalik meetod"""
        while not self.game_over:
            self.ask()
        #Näita mängu aega
        print(f'Mäng kestis {self.stopwatch.format_time()}')