import pickle
import random
import json
import os

class WordList:

    def __init__(self, category):
        self.categories = self._load_categories()
        self.category = self.select_category(category)
        self.word_list = self._load_list()
        self.word_queue = self._load_queue()
        self.randomized_list = self._randomize_list
        self.mystery_word = self._get_word


    def _load_categories(self):
        wordlists_folder = 'wordlists'
        categories = []
        try:
            for filename in os.listdir(wordlists_folder):
                if filename.endswith('.json'):
                    with open(f'{wordlists_folder}/{filename}', 'r') as json_file:
                        data = json.load(json_file)
                        categories.append(list(data.keys())[0])
            return categories
        except Exception as e:
            print(f"Error loading categories: {e}")
            return []

    
    def select_category(self, category):
        if category:
            category = category.capitalize()
            if category in self.categories:
                return category
        return random.choice(self.categories).capitalize()

    def _load_queue(self):
        try:
            with open(f'picklejar/{self.category.lower()}_queue.pickle', 'rb') as p_file:
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
            with open(f'wordlists/{self.category.lower()}.json', 'r') as json_file:
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

    def _get_word(self):
        if not self.word_queue:
            self.word_queue = self._randomize_list()
        return str(self.word_queue.pop()).upper()

    def _save_word_queue(self):
        if not self.word_queue:
            self.word_queue = self._randomize_list()
        try:
            with open(f'picklejar/{self.category.lower()}_queue.pickle', 'wb') as p_file:
                pickle.dump(self.word_queue, p_file)
        except pickle.PickleError as p_err:
            print(f'Error pickling word list.\n{p_err}')
        except OSError as err:
            print(f'Error saving word list.\n{err}')
