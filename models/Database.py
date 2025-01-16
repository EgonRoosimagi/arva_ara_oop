import sqlite3


class Database:
    db_name = 'game_leaderboard_v2.db'
    table = 'ranking'  # vajaliku tabeli nimi

    def __init__(self):
        """Konstruktor"""

        self.conn = None  # ühendus
        self.cursor = None
        self.connect()  #loo ühendus

    def connect(self):

        try:
            if self.conn:
                self.conn.close()
                print('Varasem andmebaasi ühendus suleti.')


            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f'Uus ühendus andmebaasiga {self.db_name} loodud.')
        except sqlite3.Error as error:
            print(f'Tõrge andmebaasiga ühenduse loomisel: {error}')
            self.conn = None
            self.cursor = None

    def close_connection(self):
        """Sulgeb andmebaasi ühenduse"""
        try:
            if self.conn:
                self.conn.close()
                print(f'Ühendus andmebaasiga {self.db_name} suletud.')
        except sqlite3.Error as error:
            print(f'Tõrge ühenduse sulgemisel: {error}')


    def read_records(self):
        """Loeb andmebaasist kogu edetabeli"""

        if self.cursor:
            try:
                sql = f'SELECT * FROM {self.table};'
                self.cursor.execute(sql)
                data = self.cursor.fetchall()  # kõik kirjed muutujasse data
                return data
            except sqlite3.Error as error:
                print(f'Kirjete lugemisel ilmnes tõrge: {error}')
                return []  #tagastab tühja listi
            finally:
                self.close_connection()
        else:
            print('ühendus andmebaasiga puudub. Palun loo ühendus andmebaasiga.')
