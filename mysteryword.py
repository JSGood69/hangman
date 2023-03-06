import string

class MysteryWord:
    def __init__(self, word):
        self.word = word.upper()
        self.word_length = len(self.word)
        self.word_display = ['_' for _ in range(self.word_length)]
        self.alphabet = string.ascii_uppercase
        self.vowels = 'AEIOU'

    def __str__(self):
        return self.word

    def count_letters(self, letter):
        return self.word.count(letter.upper())

    def length_alpha(self):
        return len(self.word.translate(str.maketrans('', '', string.punctuation)))

    def count_vowels(self):
        vowels_count = 0
        for vowel in self.vowels:
            vowels_count += self.count_letters(vowel)
        return vowels_count

    def count_unique_letters(self):
        unique_letters = set(self.word.translate(str.maketrans('', '', string.punctuation)))
        return len(unique_letters)

    def count_unique_vowels(self):
        unique_vowels = set([vowel for vowel in self.word if vowel in self.vowels])
        return len(unique_vowels)
