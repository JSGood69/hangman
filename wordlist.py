import pickle
import random
import json

class WordList:
    categories = ['fruits', 'countries', 'dinosaurs', 'movies', 'sports']
    category = str(random.choice(categories)).capitalize()

    def __init__(self, category):
        self.category = str(category).capitalize()
        self.word_list = self._load_list()
        self.word_queue = self._load_queue()
        self.mystery_word = self.get_word()

    def _load_queue(self):
        try:
            with open(f'{self.category.lower()}_queue.pickle', 'rb') as p_file:
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
        try:
            with open(f'{self.category.lower()}.json', 'r') as json_file:
                data = json.load(json_file)
                return data[self.category.lower()]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as j_err:
            print(f'Error decoding JSON data.\n{j_err}')
            return []
        except OSError as err:
            print(f'Error loading word list.\n{err}')
            return []

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
            with open(f'{self.category.lower()}_queue.pickle', 'wb') as p_file:
                pickle.dump(self.word_queue, p_file)
        except pickle.PickleError as p_err:
            print(f'Error pickling word list.\n{p_err}')
        except OSError as err:
            print(f'Error saving word list.\n{err}')
