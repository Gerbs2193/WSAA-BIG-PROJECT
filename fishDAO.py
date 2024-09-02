import sqlite3

class FishDAO:
    def __init__(self):
        self.connection = sqlite3.connect('fishkeeping.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_fish_table()
        self.create_tank_table()

    def create_fish_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS fish (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                species_name TEXT NOT NULL,
                                tank_name TEXT NOT NULL,
                                date_added DATE NOT NULL,
                                notes TEXT)''')
        self.connection.commit()

    def create_tank_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tanks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                volume INTEGER,
                                description TEXT)''')
        self.connection.commit()

    # Fish CRUD operations
    def get_all_fish(self):
        self.cursor.execute("SELECT * FROM fish")
        return [self.convert_to_dictionary(row, ['id', 'species_name', 'tank_name', 'date_added', 'notes']) for row in self.cursor.fetchall()]

    def add_fish(self, data):
        self.cursor.execute('INSERT INTO fish (species_name, tank_name, date_added, notes) VALUES (?, ?, ?, ?)', (data['species_name'], data['tank_name'], data['date_added'], data['notes']))
        self.connection.commit()
        return self.cursor.lastrowid

    def find_fish_by_id(self, id):
        self.cursor.execute("SELECT * FROM fish WHERE id = ?", (id,))
        return self.convert_to_dictionary(self.cursor.fetchone(), ['id', 'species_name', 'tank_name', 'date_added', 'notes'])

    def update_fish(self, id, data):
        self.cursor.execute('UPDATE fish SET species_name = ?, tank_name = ?, date_added = ?, notes = ? WHERE id = ?', (data['species_name'], data['tank_name'], data['date_added'], data['notes'], id))
        self.connection.commit()
        return True

    def delete_fish(self, id):
        self.cursor.execute('DELETE FROM fish WHERE id = ?', (id,))
        self.connection.commit()
        return True

    # Tank CRUD operations
    def add_tank(self, name, volume, description):
        self.cursor.execute('INSERT INTO tanks (name, volume, description) VALUES (?, ?, ?)', (name, volume, description))
        self.connection.commit()
        return self.cursor.lastrowid

    def get_all_tanks(self):
        self.cursor.execute("SELECT * FROM tanks")
        return [self.convert_to_dictionary(row, ['id', 'name', 'volume', 'description']) for row in self.cursor.fetchall()]

    def find_tank_by_id(self, id):
        self.cursor.execute("SELECT * FROM tanks WHERE id = ?", (id,))
        return self.convert_to_dictionary(self.cursor.fetchone(), ['id', 'name', 'volume', 'description'])

    def update_tank(self, id, data):
        self.cursor.execute('UPDATE tanks SET name = ?, volume = ?, description = ? WHERE id = ?', (data['name'], data['volume'], data['description'], id))
        self.connection.commit()
        return True

    def delete_tank(self, id):
        self.cursor.execute('DELETE FROM tanks WHERE id = ?', (id,))
        self.connection.commit()
        return True

    def convert_to_dictionary(self, row, keys):
        return {keys[i]: row[i] for i in range(len(keys))} if row else None

    def closeAll(self):
        self.cursor.close()
        self.connection.close()