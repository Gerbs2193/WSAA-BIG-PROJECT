import sqlite3

class FishDAO:
    def __init__(self):
        self.connection = sqlite3.connect('fishkeeping.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS fish (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                species_name TEXT NOT NULL,
                tank_name TEXT NOT NULL,
                date_added DATE NOT NULL,
                notes TEXT
            )
        ''')
        self.connection.commit()

    def getAll(self):
        sql = "SELECT * FROM fish"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return [self.convertToDictionary(result) for result in results]

    def findByID(self, id):
        sql = "SELECT * FROM fish WHERE id = ?"
        self.cursor.execute(sql, (id,))
        result = self.cursor.fetchone()
        return self.convertToDictionary(result) if result else None

    def create(self, fish):
        sql = "INSERT INTO fish (species_name, tank_name, date_added, notes) VALUES (?, ?, ?, ?)"
        self.cursor.execute(sql, (fish['species_name'], fish['tank_name'], fish['date_added'], fish['notes']))
        self.connection.commit()
        fish['id'] = self.cursor.lastrowid
        return fish

    def update(self, id, fish):
        sql = "UPDATE fish SET species_name = ?, tank_name = ?, date_added = ?, notes = ? WHERE id = ?"
        self.cursor.execute(sql, (fish['species_name'], fish['tank_name'], fish['date_added'], fish['notes'], id))
        self.connection.commit()

    def delete(self, id):
        sql = "DELETE FROM fish WHERE id = ?"
        self.cursor.execute(sql, (id,))
        self.connection.commit()

    def convertToDictionary(self, result):
        colnames = ['id', 'species_name', 'tank_name', 'date_added', 'notes']
        fish = {colnames[i]: result[i] for i in range(len(colnames))}
        return fish

    def closeAll(self):
        self.cursor.close()
        self.connection.close()