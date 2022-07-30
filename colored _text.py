'''from colorama import init, Fore, Back, Style

# Initializes Colorama
#init(autoreset=True)
text=str(input('enter text'))
print( Back.YELLOW + Fore.RED + text)
#print(Style.BRIGHT + Back.YELLOW + Fore.RED + "CHEESY")'''



import sys
from colorama import init
init()
from termcolor import colored, cprint


text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
