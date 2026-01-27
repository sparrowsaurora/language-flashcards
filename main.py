from database import DatabaseLayer
from enum import Enum


class RoutineLevels(Enum):
    BEGINNER = 20
    INTERMEDIATE = 50
    HIGH = 90


class Main:
    """
    Main app entry (call on db for flash cards)
    """

    def __init__(self) -> None:
        '''
        init DB and start vocab
        '''
        self.DB = DatabaseLayer()
        pass

    def level(self) -> bool:
        '''
        level function
        pass = true
        fail = false
        '''
        return True

    def check(self, word: str, english: bool = True) -> bool:
        return True

    def routine(self, level: RoutineLevels):
        '''
        main dev point
        the actual program that asks for input

        level = no. of words to complete
        '''

    def random(self):
        random_word = self.DB.random_word()
        return random_word
