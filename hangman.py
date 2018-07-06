# a simple guess the word game.
# built from scratch as a python 3.6 learning exercise
# James Good 6/27/2018
import pickle
import random

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

master_word_list = ['LEARNING', 'PYTHON', 'SCRIPT', 'STUDY', 'PROGRAM', 'STRUCTURE', 'CLASS', 'FUNCTION', 'VARIABLE', 'SYNTAX']

try:
    with open('word_list.pickle', 'rb') as p_file:
        word_list = pickle.load(p_file)
        p_file.close()
except:
    word_list = random.sample(master_word_list, len(master_word_list))

mystery_word = word_list.pop()
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
      f'The mystery word contains {Style.BRIGHT}{Fore.GREEN}{Back.BLACK}{mystery_len}{Style.RESET_ALL} letters.')

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

if not word_list:
    word_list = random.sample(master_word_list, len(master_word_list))
# write pickle data
try:
    with open('word_list.pickle', 'wb') as p_file:
        pickle.dump(word_list, p_file)
        p_file.close()
except:
    print(f'{Style.BRIGHT}{Fore.YELLOW}Error saving word list.')
