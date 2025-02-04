from datetime import datetime, timedelta


class ExportToFile:
    def __init__(self, db_model):
        """Konstruktor, mis seadistab mudeli ja võtab andmed andmebaasist."""
        self.db = db_model
        self.data = self.db.for_export()  # Saadakse andmebaasi andmed meetodiga for_export()

    def format_time(self, seconds):
        """Kujundab sekundid ajaks formaadis HH:MM:SS."""
        if seconds is None:
            return '00:00:00'
        time = str(timedelta(seconds=seconds))
        return time.split(' ')[-1]

    def format_date(self, game_time):
        """Kujundab kuupäeva ajaks formaadis PP.KK.AAAA HH:MM:SS."""
        if game_time is None:
            return '01.01.1970 00:00:00'
        game_time = datetime.utcfromtimestamp(game_time)
        return game_time.strftime('%d.%m.%Y %H:%M:%S')

    def export(self):
        """Ekspordib andmed txt faili ja vormindab viimased kaks veergu inimlikuks."""
        if not self.data:
            print("Ei leitud andmeid eksportimiseks.")
            return

        try:
            # Faili nimi on sama, mis andmebaasi failil
            filename = self.db.db_name.split('.')[0] + '.txt'

            with open(filename, 'w') as file:
                # Esimene rida - veergude nimed
                column_names = ['name', 'quess', 'steps', 'game_length', 'game_time']
                file.write(';'.join(column_names) + '\n')

                # Kirjutame kõik read, kus viimased kaks veergu on formaaditud
                for row in self.data:
                    # Formateerime viimased kaks veergu
                    game_length = self.format_time(row[3])  # game_length on x[3]
                    game_time = self.format_date(row[4])  # game_time on x[4]
                    file.write(';'.join(map(str, row[:3])) + f';{game_length};{game_time}\n')

            print(f'Andmed on edukalt eksporditud faili {filename}.')

        except Exception as e:
            print(f'Tõrge faili kirjutamisel: {e}')
