# a simple guess the word game.
# built from scratch as a python 3.6 learning exercise
# James Good 6/27/2018
import random
import string
import operator
from collections import Counter

import colorama

import text_color
from wordlist import WordList

hard_mode = True  # deducts double points for incorrect vowels when enabled.

colorama.init()

vowels = frozenset({'A', 'E', 'I', 'O', 'U'})
word_list = WordList('states')
mystery_word = word_list.mystery_word
mystery_len = len(mystery_word)
mystery_list = list(mystery_word)
mystery_vowels = list(vowels.intersection(mystery_word))
remaining_vowels = random.sample(mystery_vowels, len(mystery_vowels))
found_list = list('_' * mystery_len)
guess_log = list()
status_log = list()
score_log = list()
found = 0
prompt = 'Guess a letter, or guess the word.'  # initial prompt

if ' ' in mystery_list:
    for index, letter in enumerate(mystery_list):
        if letter == ' ':
            mystery_len -= 1
            found_list[index] = '] ['
            mystery_list[index] = '] ['

base_score = 100 * mystery_len

print(text_color.yellow('\nGuess the Mystery Word!\n'))
print('You can guess one letter at a time, or try to guess the whole word.\n')
if hard_mode:
    print(text_color.cyan('Incorrect vowel guesses cost double points! (-150 pts.)\n'))
print(f'Type {text_color.yellow("vowel")} to to reveal a vowel for (-200) points.\n'
      f'Type {text_color.yellow("exit")} to quit without guessing the word.\n\n'
      f'The category is {text_color.green(word_list.category)}\n\n'
      f'The mystery word contains {text_color.yellow(mystery_len)} letters.')

while found_list != mystery_list:
    if sum(score_log) + base_score > 0:
        print(f'{text_color.green("[ " + " ".join(found_list) + " ]")}  {prompt} '
              f'Score: {text_color.green(str(sum(score_log) + base_score))} > ', end='')
        guess = str(input()).strip()
        if guess.isalpha or guess.upper == mystery_word:
            guess = guess.upper()
            if guess in guess_log:
                plus_minus = -75 * Counter(guess_log)[guess]  # cost increases for each duplication of the same guess
                score_log.append(plus_minus)
                guess_log.append(guess)
                status_log.append('duplicate')
                prompt = f'You already guessed {text_color.cyan(guess)}. ({plus_minus} pts.)'
                continue
            if len(guess) == 1:
                is_vowel = guess in vowels
                guess_log.append(guess)
                if guess in mystery_list:
                    for index, letter in enumerate(mystery_list):
                        if letter == guess:
                            found += 1
                            found_list[index] = guess
                    if is_vowel:
                        if guess in remaining_vowels:
                            remaining_vowels.remove(guess)
                    status_log.append('correct')
                    plus_minus = 100 * Counter(mystery_word)[guess]
                    score_log.append(plus_minus)
                    prompt = f'Correct!! {text_color.green(guess)} was a match! ({plus_minus} pts.)'
                else:
                    status_log.append('incorrect')
                    if hard_mode and is_vowel:
                        plus_minus = -150
                    else:
                        plus_minus = -75
                    score_log.append(plus_minus)
                    prompt = f'Sorry, no {text_color.yellow(guess)} Try again. ({plus_minus} pts.)'
            elif len(guess) > 1:
                if guess == mystery_word:
                    found_list = mystery_list
                    guess_log.append(guess)
                    status_log.append('correct_word')
                    plus_minus = 100 * (mystery_len - found)
                    score_log.append(plus_minus)
                    prompt = f'Correct!! {text_color.green(guess)} was a match! ({plus_minus} pts.)'
                    continue
                elif guess == 'EXIT':
                    print(f'\n{text_color.yellow("Goodbye.")}\n')
                    colorama.deinit()
                    quit()
                elif guess == 'VOWEL':
                    status_log.append('vowel')
                    plus_minus = -200
                    score_log.append(plus_minus)
                    if not remaining_vowels:
                        guess_log.append('*vowel')
                        prompt = text_color.cyan('All vowels have already been revealed.') + f' ({plus_minus} pts.)'
                    else:
                        vowel_pick = remaining_vowels.pop()
                        guess_log.append(vowel_pick)
                        for index, letter in enumerate(mystery_list):
                            if letter == vowel_pick:
                                found += 1
                                found_list[index] = vowel_pick
                        prompt = f'All {text_color.green(vowel_pick)}\'s have been revealed.' \
                                 f' ({plus_minus} pts.)'
                else:
                    guess_log.append(guess)
                    status_log.append('incorrect_word')
                    plus_minus = -75
                    score_log.append(plus_minus)
                    prompt = f'Sorry, {text_color.yellow(guess)} ' \
                             f'is not the mystery word. ({plus_minus} pts.)'
                    continue
        else:
            if len(guess) == 0:
                prompt = f'{text_color.red("No input detected.")}'
                continue
            else:
                status_log.append('invalid')
                guess_log.append(guess)
                plus_minus = 0
                score_log.append(plus_minus)
                prompt = text_color.red(guess) + f' is not a valid input. ({plus_minus} pts.)'
                continue
    else:
        print(f'{text_color.green("[ " + " ".join(found_list) + " ]")}  {prompt} '
              f'Score: {text_color.green(str(sum(score_log) + base_score))} > \n'
              f'{text_color.yellow("[ G A M E _ O V E R ]")}  Better luck next time!")\n\n'
              f'Final Score: {text_color.yellow(str(sum(score_log) + base_score))} / {base_score * 2}\n')
        break
else:
    print(f'{text_color.green("[ " + " ".join(mystery_list) + " ]")}  {prompt} '
          f'Score: {text_color.green(str(sum(score_log) + base_score))} > \n'
          f'{text_color.green("[ G A M E _ O V E R ]")}  You guessed it! '
          f'The mystery word was {text_color.green(mystery_word)}!\n\n'
          f'Final Score: {text_color.green(str(sum(score_log) + base_score))} / {base_score * 2}\n')

count = Counter(status_log)
print(f'You made {text_color.yellow(str(len(status_log)))} guesses.\n\n'
      f' {text_color.green(str(count["correct"]) + " correct letter guesses.")}\n'
      f' {text_color.green(str(count["correct_word"]) + " correct word guesses.")}\n'
      f' {text_color.yellow(str(count["incorrect"]) + " incorrect letter guesses.")}\n'
      f' {text_color.yellow(str(count["incorrect_word"]) + " incorrect word guesses.")}\n'
      f' {text_color.cyan(str(count["duplicate"])+ " duplicate guesses.")}\n'
      f' {text_color.red(str(count["invalid"]) + " invalid guesses.")}\n'
      f' {count["vowel"]} vowel reveals.\n')

game_log = list(zip(guess_log, status_log, list(range(len(status_log)))))
sorted_log = sorted(game_log, key=operator.itemgetter(0, 2))

print('Guess Log: ', end='')
for g, s, i in game_log:
    print(f'{text_color.status_color(s, g)} ', end='', flush=True)
print('\n')

print('A-Z Guess: ', end='')
for g, s, i in sorted_log:
    if g in string.ascii_uppercase:
        print(f'{text_color.status_color(s, g)} ', end='', flush=True)
print('\n')

word_list.save_word_queue()
colorama.deinit()
