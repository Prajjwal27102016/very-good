new_file = open('new_file.txt', 'w')
new_file. close()

import os
print("cheking if file my_file.txt exists or not")
if os.path.exists('new_file.txt'):
    os.remove('new_file.txt')
else:
    print("the file does not exist")

my_file = open('new_file.txt', 'w')
my_file.write("hi i am a dog i am 5 years old")
my_file.close()

os.remove('mem.txt')
os.rmdir('Folder')