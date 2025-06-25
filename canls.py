file_read = open('mem.txt', 'r')
print("file in read mode-")
print(file_read.read())
file_read. close()

file_write = open('mem.txt', 'w')
file_write.write("file in write mode......................................................")
file_write.write(" Hi! I am Prajjwal and I am 9 years old")
file_write.close()

file_append = open('mem.txt', 'a')
file_append.write("\nfile in append mode......................................................")
file_append.write(" Hi! I am Prajjwal and I am 9 years old")
file_append.close()