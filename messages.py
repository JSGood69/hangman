class Messages:
    def __init__(self):
        self.prompt = 'Guess a letter, or guess the word.'
        self.initial_message = (
            '\nGuess the Mystery Word!\n\n'
            'You can guess one letter at a time, or try to guess the whole word.\n'
            'Type "VOWEL" to to reveal a vowel for (-200) points.\n'
            'Type "EXIT" to quit without guessing the word.\n\n'
        )
        self.category_message = 'The category is {}.\n'
        self.mystery_len_message = 'The mystery word contains {} letters.'
        self.vowel_message = (
            'All {}\'s have been revealed.\n'
            '(-200 pts.)\n'
        )
        self.correct_letter_message = (
            'Correct!! {} was a match! ({:.0f} pts.)\n'
        )
        self.incorrect_letter_message = (
            'Sorry, no {} Try again. ({:.0f} pts.)\n'
        )
        self.correct_word_message = (
            'Correct!! {} was a match! ({:.0f} pts.)\n'
        )
        self.incorrect_word_message = (
            'Sorry, {} is not the mystery word. ({:.0f} pts.)\n'
        )
        self.duplicate_guess_message = (
            'You already guessed {}. ({:.0f} pts.)\n'
        )
        self.invalid_input_message = (
            '{} is not a valid input. ({:.0f} pts.)\n'
        )
        self.game_over_message = (
            '{}  Better luck next time!\n\n'
            'Final Score: {:.0f} / {:.0f}\n'
        )
        self.win_message = (
            '{}  You guessed it! The mystery word was {}!\n\n'
            'Final Score: {:.0f} / {:.0f}\n'
        )
        self.stats_message = (
            'You made {} guesses.\n\n'
            ' {} correct letter guesses.\n'
            ' {} correct word guesses.\n'
            ' {} incorrect letter guesses.\n'
            ' {} incorrect word guesses.\n'
            ' {} duplicate guesses.\n'
            ' {} invalid guesses.\n'
            ' {} vowel reveals.\n'
        )
