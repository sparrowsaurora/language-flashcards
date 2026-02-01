from database import DatabaseLayer
from enum import Enum


class RoutineLevels(Enum):
    BEGINNER = 3
    INTERMEDIATE = 50
    EXPERT = 90


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
        # get random word & translation
        line: tuple = self.DB.random_word()
        print(f"{line[1]}")

        translation: str = str(line[2])

        # ask user for translation
        answer: str = input("Enter Translation: ")

        if answer.lower().strip() == translation:
            return True
        return False

    def routine(self, level_rating: RoutineLevels) -> None:
        '''
        main dev point
        the actual program that asks for input

        level = no. of words to complete
        '''
        passes: int = 0
        print(f"Starting {level_rating.name}")
        runs = level_rating.value
        for i in range(runs):
            print(f"Level {i}:", end=" ")
            if self.level() == True:
                passes += 1
        print(
            f"Score: {passes}/{runs} or {int(((passes / runs) * 100) + 0.5)}%"
        )

    def random(self) -> tuple:
        random_word: tuple = self.DB.random_word()
        return random_word


main = Main()
# main.DB.add("hello", "hallo")
# main.DB.add("Thank you", "Danke")
# main.DB.add("Bye", "Tschüß")
# main.DB.random_word()
# print(main.DB.translate("hello"))
# print(main.DB.translate("danke", english=False))
main.routine(RoutineLevels.BEGINNER)
