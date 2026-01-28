import sqlite3
import random


class DatabaseLayer:
    '''
    DAL for Main app
    '''

    def __init__(self):
        '''
        Init local db connection
        '''
        with sqlite3.connect('flashcards.db') as connection:
            print("Database connection established.")
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS Cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                english_word TEXT NOT NULL,
                german_word INTEGER
            );
            """
            cursor.execute(create_table_query)
            connection.commit()  # Save the changes
            print("Table 'Cards' created successfully.")

    def add(self, english: str, deutsch: str):
        english = english.lower().strip()
        deutsch = deutsch.lower().strip()
        with sqlite3.connect('flashcards.db') as connection:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO Cards (english_word, german_word) VALUES (?, ?);
            """
            card_data = (english, deutsch)
            cursor.execute(insert_query, card_data)
            connection.commit()
            print("Record inserted successfully.")

    def read(self, row_id: int) -> tuple:
        '''
        reads a specified row
        '''
        with sqlite3.connect('flashcards.db') as connection:
            cursor = connection.cursor()
            query = """
            SELECT * FROM Cards WHERE id = (?);
            """
            cursor.execute(query, str(row_id))
            result = cursor.fetchall()[0]
            # print(result)
            # print(type(result))
            return result

    def browse(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def edit(self):
        raise NotImplementedError

    def translate(self, word: str, english: bool = True) -> tuple:
        word = word.lower().strip()
        with sqlite3.connect('flashcards.db') as connection:
            cursor = connection.cursor()
            if english:
                query = """
                SELECT * FROM Cards WHERE english_word = (?);
                """
                cursor.execute(query, (word,))
            else:
                query = """
                SELECT * FROM Cards WHERE german_word = (?);
                """
                cursor.execute(query, (word,))
            return cursor.fetchone()

    def get_row_count(self) -> int:
        with sqlite3.connect('flashcards.db') as connection:
            cursor = connection.cursor()
            query = """
            SELECT COUNT(*) FROM Cards;

            """
            cursor.execute(query)
            return int(cursor.fetchone()[0])

    def random_word(self, english=True) -> tuple:
        '''
        call read on random word
        '''
        word_id = random.randint(1, self.get_row_count())
        with sqlite3.connect('flashcards.db') as connection:
            cursor = connection.cursor()
            query = """
            SELECT * FROM Cards WHERE id = (?);
            """
            cursor.execute(query, str(word_id))
            result = cursor.fetchall()[0]
            # print(result)
            # print(type(result))
            return result
