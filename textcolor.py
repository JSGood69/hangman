import colorama
from colorama import Fore, Style
color = {'green': Style.BRIGHT + Fore.GREEN,
         'yellow': Style.BRIGHT + Fore.YELLOW,
         'cyan': Style.BRIGHT + Fore.CYAN,
         'red': Style.BRIGHT + Fore.RED,
         'reset': Style.RESET_ALL}

color_key = {'highlight': color['yellow'], 'notify': color['cyan'],
             'correct': color["green"], 'correct_word': color["green"],
             'incorrect': color["yellow"], 'incorrect_word': color["yellow"],
             'duplicate': color["cyan"], 'invalid': color["red"], 'vowel': color["reset"]}


def color_text(key, my_string, reset_color=True):
    if reset_color:
        colored_string = f'{color_key[key]}{my_string}{color["reset"]}'
        return colored_string
    else:
        colored_string = f'{color_key[key]}{my_string}'
        return colored_string

def color_print(key, my_string, reset_color=True):
    if reset_color:
        print(color_key[key], my_string, color['reset'])
    else:
        print(color_key[key], my_string)

