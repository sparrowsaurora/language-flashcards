class DatabaseLayer:
    '''
    DAL for Main app
    '''

    def __init__(self):
        '''
        Init local db connection
        '''
        pass

    def add(self, english: str, deutsch: str):
        raise NotImplementedError

    def read(self, english: str) -> tuple:
        '''
        returns deutsch translation
        '''
        raise NotImplementedError

    def browse(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def edit(self):
        raise NotImplementedError

    def random_word(self, english=True):
        '''
        call read on random word
        '''
        raise NotImplementedError
