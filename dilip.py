import os

if os.path.exists('mem.txt'):
    os.remove('mem.txt')
else:
    print("The file does not exist")