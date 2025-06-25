file = open('mem.txt','r')
print(file.read())
file.close()

file = open('mem.txt','r')
print("\n read in parts \n")
print(file.read(10))  
file.close()

file = open('mem.txt','a')
file.write(" Hi! I am Prajjwal and i am 9 years old")
file.close()