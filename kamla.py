with open('mem.txt' ,'w') as file:
    file.write("hi i am kamla i am 45 years old")
    file.close()

    with open('mem.txt', 'r') as file:
        data = file. readlines()
        print("word in this file are good")
        for line in data:
            word = line.split()
            print(word)
           
    file.close()