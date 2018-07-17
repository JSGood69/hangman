from colorama import Fore, Style

_green = Style.BRIGHT + Fore.GREEN
_yellow = Style.BRIGHT + Fore.YELLOW
_cyan = Style.BRIGHT + Fore.CYAN
_red = Style.BRIGHT + Fore.RED
_reset = Style.RESET_ALL

_status_color = {'correct': _green, 'correct_word': _green,
                 'incorrect': _yellow, 'incorrect_word': _yellow,
                 'duplicate': _cyan, 'invalid': _red, 'vowel': ''}


def green(my_string, reset_color=True):
    if reset_color:
        return f'{_green}{my_string}{_reset}'
    else:
        return f'{_green}{my_string}'

def yellow(my_string, reset_color=True):
    if reset_color:
        return f'{_yellow}{my_string}{_reset}'
    else:
        return f'{_yellow}{my_string}'

def cyan(my_string, reset_color=True):
    if reset_color:   
        return f'{_cyan}{my_string}{_reset}'
    else:
         return f'{_cyan}{my_string}'

def red(my_string, reset_color=True):
    if reset_color:
        return f'{_red}{my_string}{_reset}'
    else:
        return f'{_red}{my_string}'

def status_color(my_status, my_string, reset_color=True):
    if reset_color:
        return f'{_status_color[my_status]}{my_string}{_reset}'
    else:
        return f'{_status_color[my_status]}{my_string}'
