import pickle
import random


class WordList:
    categories = ['fruits', 'states']
    category = str(random.choice(categories)).capitalize()

    def __init__(self, category):
        self.category = str(category).capitalize()
        self.word_list = self._load_list()
        self.word_queue = self._load_queue()
        self.mystery_word = self.get_word()


    def _load_queue(self):
        try:
            with open(f'{self.category}_queue.pickle', 'rb') as p_file:
                return pickle.load(p_file)
        except FileNotFoundError:
            return self._randomize_list()
        except pickle.PickleError as p_err:
            print(f'Error unpickling word list.\n{p_err}')
            return self._randomize_list()
        except OSError as err:
            print(f'Error loading word list.\n{err}')
            return self._randomize_list()

    def _load_list(self):
        # implement reading from text file
        if self.category == 'Fruits':
            return ['apple', 'apricot', 'banana', 'blackberry', 'blueberry', 'boysenberry', 'cherry', 'cranberry',
                    'fig', 'grape', 'grapefruit', 'guava', 'huckleberry', 'kumquat', 'lemon', 'lime', 'mango',
                    'cantaloupe', 'honeydew', 'watermelon', 'nectarine', 'orange', 'tangerine', 'papaya',
                    'peach', 'pear', 'persimmon', 'plum', 'pineapple', 'pomegranate', 'raspberry', 'strawberry']
        elif self.category == 'States':
            return ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                    'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                    'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
                    'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
                    'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
                    'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
                    'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

    def _randomize_list(self):
        return random.sample(self.word_list, len(self.word_list))

    def get_word(self):
        if not self.word_queue:
            self.word_queue = self._randomize_list()
        return str(self.word_queue.pop()).upper()

    def save_word_queue(self):
        if not self.word_queue:
            self.word_queue = self._randomize_list()
        try:
            with open(f'{self.category}_queue.pickle', 'wb') as p_file:
                pickle.dump(self.word_queue, p_file)
        except pickle.PickleError as p_err:
            print(f'Error pickling word list.\n{p_err}')
        except OSError as err:
            print(f'Error saving word list.\n{err}')
