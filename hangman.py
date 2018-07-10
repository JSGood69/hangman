# a simple guess the word game.
# built from scratch as a python 3.6 learning exercise
# James Good 6/27/2018
import pickle
import random
import string
import operator
from collections import Counter

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)
color = {'green': Style.BRIGHT+Fore.GREEN,
         'yellow': Style.BRIGHT+Fore.YELLOW,
         'cyan': Style.BRIGHT+Fore.CYAN,
         'red': Style.BRIGHT+Fore.RED,
         'reset': Style.RESET_ALL}
status_color = {'correct': color["green"], 'correct_word': color["green"],
                'incorrect': color["yellow"], 'incorrect_word': color["yellow"],
                'duplicate': color["cyan"], 'invalid': color["red"]}
master_word_list = ['LEARNING', 'PYTHON', 'SCRIPT', 'STUDY', 'PROGRAM', 'STRUCTURE', 'CLASS', 'FUNCTION', 'VARIABLE', 'SYNTAX']

try:
    with open('word_list.pickle', 'rb') as p_file:
        word_list = pickle.load(p_file)
except:
    word_list = random.sample(master_word_list, len(master_word_list))

mystery_word = word_list.pop()
mystery_len = len(mystery_word)
mystery_list = list(mystery_word)
found_list = list('_' * mystery_len)
guess_log = list()
status_log = list()
score_log = list()
base_score = 10 * mystery_len
found = 0
prompt = 'Guess a letter, or guess the word.'  # initial prompt

print(f'\n{color["yellow"]}Guess the Mystery Word!{color["reset"]}\n'
      f'You can guess one letter at a time, or try to guess the whole word.\n'
      f'Type {color["yellow"]}exit{color["reset"]} to quit without guessing the word.\n\n'
      f'The mystery word contains {color["yellow"]}{mystery_len}{color["reset"]} letters.')

while found_list != mystery_list:
    print(f'{color["green"]}[ {" ".join(found_list)} ]{color["reset"]}  {prompt} Score: {color["green"]}{sum(score_log) + base_score}{color["reset"]}> ', end='')
    guess = str(input()).strip()
    if str(guess).isalpha():
        guess = str(guess).upper()
        if guess in guess_log:
            plus_minus = -5 * Counter(guess_log)[guess] # cost increases for each duplication of the same guess
            score_log.append(plus_minus)
            guess_log.append(guess)
            status_log.append('duplicate')
            prompt = f'You already guessed {color["cyan"]}{guess}{color["reset"]}. ({plus_minus} pts.)'
            continue
        if len(guess) == 1:
            guess_log.append(guess)
            if guess in mystery_list:
                for index, letter in enumerate(mystery_list):
                    if letter == guess:
                        found += 1
                        found_list[index] = guess
                status_log.append('correct')
                plus_minus = 10 * Counter(mystery_word)[guess]
                score_log.append(plus_minus)
                prompt = f'Correct!! {color["green"]}{guess}{color["reset"]} was a match! ({plus_minus} pts.)'
            else:
                status_log.append('incorrect')
                plus_minus = -5
                score_log.append(plus_minus)
                prompt = f'Sorry, no {color["yellow"]}{guess}{color["reset"]} Try again. ({plus_minus} pts.)'
        elif len(guess) > 1:
            if guess == mystery_word:
                guess_log.append(guess)
                status_log.append('correct_word')
                plus_minus = 10 * (mystery_len - found )
                score_log.append(plus_minus)
                break
            elif guess == 'EXIT':
                print(f'\n{color["yellow"]}Goodbye.\n')
                colorama.deinit()
                quit()
            else:
                guess_log.append(guess)
                status_log.append('incorrect_word')
                plus_minus = -5 * Counter(status_log)['incorrect_word']
                score_log.append(plus_minus)
                prompt = f'Sorry, {color["yellow"]}{guess}{color["reset"]} is not the mystery word. ({plus_minus} pts.)'
                continue
    else:
        if len(guess) == 0:
            prompt = f'{color["red"]}No input detected.{color["reset"]}'
            continue
        else:
            status_log.append('invalid')
            guess_log.append(guess)
            plus_minus = 0
            score_log.append(plus_minus)
            prompt = f'{color["red"]}{guess}{color["reset"]} is not a valid input. ({plus_minus} pts.)'
            continue

print(f'{color["green"]}[ {" ".join(mystery_list)} ]{color["reset"]}  '
      f'You guessed it! The mystery word was {color["green"]}{mystery_word}!{color["reset"]}'
      f'({plus_minus} pts.) Score: {color["green"]}{sum(score_log) + base_score}{color["reset"]}\n')

count = Counter(status_log)
print(f'It took you {color["yellow"]}{len(status_log)}{color["reset"]} guesses.\n'
      f' {color["green"]}{count["correct"]} correct letter guesses.\n'
      f' {color["green"]}{count["correct_word"]} correct word guesses.\n'
      f' {color["yellow"]}{count["incorrect"]} incorrect letter guesses.\n'
      f' {color["yellow"]}{count["incorrect_word"]} incorrect word guesses.\n'
      f' {color["cyan"]}{count["duplicate"]} duplicate guesses.\n'
      f' {color["red"]}{count["invalid"]} invalid guesses.{color["reset"]}\n')

game_log = list(zip(guess_log, status_log, list(range(len(status_log)))))
sorted_log = sorted(game_log, key = operator.itemgetter(0, 2))

print('Guess Log: ', end='')
for g, s, i in game_log:
    print(f'{status_color[s]}{g} ', end='', flush=True)
print('\n')

print('A-Z Guess: ', end='')
for g, s, i in sorted_log:
    if g in string.ascii_uppercase:
        print(f'{status_color[s]}{g} ', end='', flush=True)
print('\n')

if not word_list:
    word_list = random.sample(master_word_list, len(master_word_list))

try:
    with open('word_list.pickle', 'wb') as p_file:
        pickle.dump(word_list, p_file)
except:
    print(f'{color["yellow"]}Error saving word list.')

colorama.deinit()
