import sys
import os

user_input = input('Enter a command: ')

if user_input.lower().startswith('sys.in'):
    print('Command accepted')
else:
    print('Command rejected')
