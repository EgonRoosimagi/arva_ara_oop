from random import randint

from models.Database import Database
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
        self.pc_nr = randint(1, 100)  # juhuslik number
        self.steps = 0  # sammude arv
        self.game_over = False  # mäng ei ole läbi
        self.cheater = False  # mängija ei ole petja
        self.stopwatch.reset()  # nullib stopperi
        # self.stopwatch.start() #käivitab stopperi

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
        self.stopwatch.start()
        while not self.game_over:
            self.ask()
        #Näita mängu aega
        print(f'Mäng kestis {self.stopwatch.format_time()}')

        self.what_next() #Mis on järgmiseks
        self.show_menu() # Näita mängu menüüd


    def what_next(self):
        """Küsime mängija nime ja lisame info andmebaasi"""
        name = self.ask_name()
        db = Database() #LOO ANDMEBAASI OBJEKT
        db.add_record(name, self.steps, self.pc_nr, self.cheater, self.stopwatch.seconds)

    def ask_name(self):
        """Küsib nime ja tagastab korrektse nime"""
        name = input('Kuidas on mängija nimi? ')
        if not name.strip():
            name = 'Teadmata'
        return name.strip()

    def show_menu(self):
        """Näita mängu menüüd"""

        print('1 - Mängima')
        print('2 - Edetabel')
        print('3 - Välju programmist')
        user_input = int(input('Sisesta number [1, 2 või 3]: '))
        if 1 <= user_input <= 3:
            if user_input == 1:
                self.reset_game()

                self.lets_play()
            elif user_input == 2:
                self.show_leaderboard()  #näita edetabelit
                self.show_menu()  # lähme mängima
            elif user_input ==3:
                print('Bye, bye :)')
                exit()  #igasugune skripti töö lõppeb
        else:
            self.show_menu()

    def show_leaderboard(self):
        """Näita edetabelit"""
        db = Database()
        data = db.read_records()
        if data:
            for record in data:
                print(record) # name -> record[1]


