# a simple guess the word game.
# built from scratch as a python 3.6 learning exercise
# James Good 6/27/2018
import pickle
import random
from collections import Counter

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

master_word_list = ['LEARNING', 'PYTHON', 'SCRIPT', 'STUDY', 'PROGRAM', 'STRUCTURE', 'CLASS', 'FUNCTION', 'VARIABLE', 'SYNTAX']

try:
    with open('word_list.pickle', 'rb') as p_file:
        word_list = pickle.load(p_file)
except:
    word_list = random.sample(master_word_list, len(master_word_list))

mystery_word = word_list.pop()
mystery_list = list(mystery_word)
mystery_len = len(mystery_list)
found_list = list('_' * mystery_len)
guess_log = list()
status_log = list()

print(f'\n{Style.BRIGHT}{Fore.CYAN}Guess the Mystery Word!{Style.RESET_ALL}\n'
      f'You can one letter at a time, or try to guess the whole word at any time.\n\n'
      f'Type {Style.BRIGHT}{Fore.CYAN}exit{Style.RESET_ALL} to quit.\n\n'
      f'The mystery word contains {Style.BRIGHT}{Fore.CYAN}{Back.BLACK}{mystery_len}{Style.RESET_ALL} letters.')
print(f'{Style.BRIGHT}{Fore.GREEN}{Back.BLACK}[ {" ".join(found_list)} ]{Style.RESET_ALL}  '
      f'{Style.BRIGHT}{Fore.CYAN}<-- Correct guesses will populate the Mystery Word here.')
prompt = 'Guess a letter, or guess the word.'
while found_list != mystery_list:
    print(f'{Style.BRIGHT}{Fore.GREEN}{Back.BLACK}[ {" ".join(found_list)} ]{Style.RESET_ALL}  {prompt} > ', end='')
    guess = str(input()).strip()
    if str(guess).isalpha():
        guess = str(guess).upper()
        if guess in guess_log:
            guess_log.append(guess)
            status_log.append('duplicate') 
            prompt = f'You already guessed {Style.BRIGHT}{Fore.YELLOW}{guess}{Style.RESET_ALL}.'
            continue
        if len(guess) == 1:
            guess_log.append(guess)
            if guess in mystery_list:
                for index, letter in enumerate(mystery_list):
                    if letter == guess:
                        found_list[index] = guess
                status_log.append('correct')
                prompt = f'Correct!! {Style.BRIGHT}{Fore.GREEN}{guess}{Style.RESET_ALL} was a match!'
            else:
                status_log.append('incorrect') 
                prompt = f'Sorry, no {Style.BRIGHT}{Fore.YELLOW}{guess}{Style.RESET_ALL}. Try again.'
        elif len(guess) > 1:
            if guess == mystery_word:
                guess_log.append(guess)
                status_log.append('correct_word')
                break
            elif guess == 'EXIT':
                print(f'\n{Style.BRIGHT}{Fore.BLUE}Goodbye.')
                colorama.deinit()
                quit()
            else:
                guess_log.append(guess)
                status_log.append('incorrect_word')
                prompt = f'Sorry, {Style.BRIGHT}{Fore.YELLOW}{guess}{Style.RESET_ALL} is not the mystery word.'
                continue
    else:
        if len(guess) == 0:
            prompt = f'{Style.BRIGHT}{Fore.RED}No input detected.'
            continue
        else:
            prompt = f'{Style.BRIGHT}{Fore.RED}{guess}{Style.RESET_ALL} is not a valid input.'
            status_log.append('invalid')
            guess_log.append(guess)
            continue

print(f'{Style.BRIGHT}{Fore.GREEN}{Back.BLACK}[ {" ".join(mystery_list)} ]{Style.RESET_ALL}  '
      f'You guessed it! The mystery word was {Style.BRIGHT}{Fore.GREEN}{mystery_word}{Style.RESET_ALL}!\n')

count = Counter(status_log)
print(f'It took you {Style.BRIGHT}{Fore.CYAN}{len(status_log)}{Style.RESET_ALL} guesses\'s.\n'
      f' {Style.BRIGHT}{Fore.GREEN}{count["correct_word"]} correct word guesses.\n'
      f' {Style.BRIGHT}{Fore.GREEN}{count["correct"]} correct letter guesses.\n'
      f' {Style.BRIGHT}{Fore.YELLOW}{count["incorrect_word"]} incorrect word guesses.\n'
      f' {Style.BRIGHT}{Fore.YELLOW}{count["incorrect"]} incorrect letter guesses.\n'
      f' {Style.BRIGHT}{Fore.YELLOW}{count["duplicate"]} duplicate guesses.\n'
      f' {Style.BRIGHT}{Fore.RED}{count["invalid"]} invalid guesses.{Style.RESET_ALL}\n')

print(f'Guess Log: {Style.BRIGHT}{Fore.YELLOW}{" ".join(guess_log)}\n')

if not word_list:
    word_list = random.sample(master_word_list, len(master_word_list))

try:
    with open('word_list.pickle', 'wb') as p_file:
        pickle.dump(word_list, p_file)
except:
    print(f'{Style.BRIGHT}{Fore.YELLOW}Error saving word list.')

colorama.deinit()
