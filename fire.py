# Reading the file

print("File in read mode:")

file_read = open('mem.txt', 'r')

print(file_read.read())

file_read.close()

# Writing to the file (overwrites existing content)

file_write = open('mem.txt', 'w')

file_write.write("File in write mode......................................................")

file_write.write(" Hi! I am Prajjwal and I am 9 years old")

file_write.close()

# Appending to the file (adds content at the end)

file_append = open('mem.txt', 'a')

file_append.write("\nFile in append mode......................................................")

file_append.write(" Hi! I am Prajjwal and I am 9 years old")

file_append.close()