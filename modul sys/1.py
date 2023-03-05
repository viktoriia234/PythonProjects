import sys
import os

if len(sys.argv) == 1:
    print('Hello World')
elif len(sys.argv) == 3 and sys.argv[1] == '--name':
    name = sys.argv[2]
    print('Hello', name)
else:
    script_name = os.path.basename(sys.argv[0])
    print(f'Usage: {script_name} [--name <name>]')
