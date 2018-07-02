# a simple guess the word game.
# built from scratch as a python 3.6 learning exercise
# James Good 6/27/2018

import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

word_list = ['learning', 'python', 'script', 'study', 'program', 'structure', 'class', 'function', 'variable', 'syntax']
mystery_word = str(random.choice(word_list)).upper()
mystery_list = list(mystery_word)
mystery_len = len(mystery_list)
found_list = list('_' * mystery_len)
guess_log = list()
# counters and such
found = 0
guesses = 0
correct = 0
incorrect = 0
duplicate = 0
invalid = 0
blank = 0
correct_word = 0
incorrect_word = 0
prompt = 'Guess a letter.'
# main
print(f'\nGuess one letter at a time, or try to guess the whole word at any time.\n'
      f'Type "exit" quit.\n\n'
      f'The mystery word contains {mystery_len} letters.')
while found < mystery_len:
    print(f'{Style.BRIGHT}{Fore.CYAN}{Back.BLACK}[ {" ".join(found_list)} ]{Style.RESET_ALL}  {prompt} > ', end='')
    guess = str(input()).strip()
    guesses += 1
    if str(guess).isalpha():
        guess = str(guess).upper()
        if guess in guess_log:
            duplicate += 1
            prompt = f'You already guessed {Style.BRIGHT}{Fore.YELLOW}{guess}{Style.RESET_ALL}.'
            guess_log.append(guess)
            continue
        guess_log.append(guess)
        if len(guess) == 1:
            if guess in mystery_list:
                for index, s in enumerate(mystery_list):
                    if s == guess:
                        found_list[index] = guess
                        found += 1
                correct += 1
                prompt = f'Correct!! {Style.BRIGHT}{Fore.GREEN}{guess}{Style.RESET_ALL} was a match!'
            else:
                incorrect += 1
                prompt = f'Sorry, no {Style.BRIGHT}{Fore.YELLOW}{guess}{Style.RESET_ALL}. Try again.'
        elif len(guess) > 1:
            if guess == mystery_word:
                correct_word += 1
                break
            elif guess == 'EXIT':
                print(f'\n{Style.BRIGHT}{Fore.BLUE}Goodbye.')
                colorama.deinit()
                quit()
            else:
                incorrect_word += 1
                prompt = f'Sorry, {Style.BRIGHT}{Fore.YELLOW}{guess}{Style.RESET_ALL} is not the mystery word.'
                continue
    else:
        if len(guess) == 0:
            blank += 1
            prompt = f'{Style.BRIGHT}{Fore.RED}No input detected.'
            continue
        else:
            prompt = f'{Style.BRIGHT}{Fore.RED}{guess}{Style.RESET_ALL} is not a valid input.'
            invalid += 1
            guess_log.append(guess)
            continue

print(f'{Style.BRIGHT}{Fore.CYAN}{Back.BLACK}[ {" ".join(mystery_list)} ]{Style.RESET_ALL}  '
      f'You guessed it! The mystery word was {Style.BRIGHT}{Fore.GREEN}{mystery_word}!\n')
print(f'It took you {Style.BRIGHT}{Fore.CYAN}{guesses}{Style.RESET_ALL} guesses\'s.\n'
      f' {Style.BRIGHT}{Fore.GREEN}{correct_word} correct word guesses.\n'
      f' {Style.BRIGHT}{Fore.GREEN}{correct} correct letter guesses.\n'
      f' {Style.BRIGHT}{Fore.YELLOW}{incorrect_word} incorrect word guesses.\n'
      f' {Style.BRIGHT}{Fore.YELLOW}{incorrect} incorrect letter guesses.\n'
      f' {Style.BRIGHT}{Fore.YELLOW}{duplicate} duplicate guesses.\n'
      f' {Style.BRIGHT}{Fore.RED}{invalid} invalid guesses.\n'
      f' {Style.BRIGHT}{Fore.RED}{blank} blank guesses.{Style.RESET_ALL}\n\n'
      f'Guess Log: {Style.BRIGHT}{Fore.YELLOW}{" ".join(guess_log)}\n')
colorama.deinit()
# Todo: make the guess_log  = index,input,status,counters.
# Todo:..so when they enter a dupe we can say " x # is STILL not the right answer!, or you already got that one.
# todo: uses the guess log to determine what color to display guess. you alreay guessed X with x green if it was correct
# Todo: possibly put variables into a dict or something similar.
# Todo: need a word list to cycle through randomly for mystery_word
# Todo: make a separate list of funny ways respond to incorrect guesses, and cycle through randomly.
# Todo: give option to restart game at end with a new word.
# Todo: implement a score using multipliers based on integer variables.
# Todo: get name, and save high scores with all stats including contents of input_log
# Todo: colorize output strings based on type correct incorrect etc.
# Todo: add hint feature to reveal one letter. put a cap on use
# Todo: add log keyword to print guesses so far.only log correct and incorrect guesses no invalid, empty or dupe. sort alpa
# Todo: ability to guess substrings. may be downsides
