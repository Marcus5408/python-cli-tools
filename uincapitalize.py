from colors import bcolors
from colorama import Fore, Back, Style

input = input(f'{bcolors.OKGREEN}Enter a string: {bcolors.ENDC}')
print("Uncapitalized: " + input.lower())