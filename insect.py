try:

   file_read = open('mem.txt', 'r')

   print(file_read.read())

   file_read.close()

except FileNotFoundError:

   print("File not found. Creating a new file.")

   file_create = open('mem.txt', 'w')

   file_create.write("This is a new file created because it was missing.")

   file_create.close()