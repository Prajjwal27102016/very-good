import sys

def intial_phonebook():
    rows, cols = int(input("please enter a intial number of contacts")),5

    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d detail in the following order(ONLY):" % (i + 1))
        print("NOTE: * indicates mandatory field")
        print("........................................................")

        prajjwal = []
        for j in range(cols):

            if j == 0:
              prajjwal.append(str(input("Name* : ")))
              if prajjwal[j] == ""or prajjwal[j] == " ":
                 sys.exit("name is a mandatory field.process exiting due to blank field")
            if j == 1:
                prajjwal.append(str(input("enter number* : ")))
            if j == 2:
                prajjwal.append(str(input("enter email* : ")))
            if prajjwal[j] == ""or prajjwal[j] == " ":
                prajjwal[j] = None 
            if j == 3:
                prajjwal.append(str(input("enter date of birth(dd/mm/yy): ")))
                if prajjwal[j] == ""or prajjwal[j] == " ":
                   prajjwal[j] = None
            if j == 4:
                prajjwal.append(str(input("enter catogory(family/friends/college): ")))
                if prajjwal[j] == ""or prajjwal[j] == " ":
                 prajjwal[j] = None
        phone_book.append(prajjwal)
    print(phone_book)
    return phone_book
def menu():
            print("........................................................")
      print("\t\t\tSMARTPHONE DIRECTORY",flush=false)
   print("........................................................")
   print("\tYou can now perform the following operationson this phonebook\n")
   print("1. add a new contact")
   print("remove an existing contact")
   print("3.delete all contact")
   print("4.search for a contact")
   print("5.display all contacts")
   print("6.exit phonebook")
choice = int(input("please enter your choice: "))
return choice
def add_contact(pb):
    me=[]
    for i in range(len(pb[0])):
        if i == 0:
            me.append(str(input("enter name* : ")))
        if i == 1:
            me.append(int(input("enter number* : ")))
        if i == 2:
            me.append(str(input("enter email* : ")))
        if i == 3:
            me.append(str(input("enter date of birth(dd/mm/yy): ")))
        if i == 4:
            me.append(str(input("enter catogory(family/friends/college): ")))
        pb.append(me)

        return pb
        qwerty = str(input("please enter the name of the contact you wish to remove: "))
        prajjwal = 0

        for i in range(len(pb)):
            if qwerty == pb[i][0]:
                prajjwal += 1
                print(pb.pop(i))
                print("this qwerty has now been remove")
                return pb
        if prajjwal == 0:
            print("sorry, you have entered an valid qwerty.\nplease recheck and try again later")
            return pb
def delete_all(pb):
    return pb.clear()

def search_existing(pb):
    choice = int(input("enter seach criteria\n\n\n1. name\n2. number\n3. email\n4. date of birth\n5. catogory"))
    prajjwal = []
    check = -1
    if choice == 1:
        qwerty= str(input("please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if qwerty == pb[i][0]:
                check = i
                prajjwal.append(pb[i])
    elif choice == 2:
        qwerty = int(input("please enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if qwerty == pb[i][1]:
                check = i
                prajjwal.append(pb[i])
    elif choice == 3:
        qwerty = str(input("please enter the e-mailID\ of the contact you wish to search: "))
        for i in range(len(pb)):
            if qwerty == pb[i][2]:
                check = i
                prajjwal.append(pb[i])
    elif choice == 4:
        qwerty = str(input("please enter the dob((dd/mm/yy)format only)/ of the contact you wish to search: "))
        for i in range(len(pb)):
            if qwerty == pb[i][3]:
                check = i
                prajjwal.append(pb[i])
    elif choice == 5:
        qwerty = str(input("please enter the catogory of the contact you wish to search: "))
        for i in range(len(pb)):
            if qwerty == pb[i][4]:
                check = i
                prajjwal.append(pb[i])
else:
print("invalid search criteria")
return -1

if check ==1:
    return -1
else:
    diplay_all(prajjwal)
    return check

def diplay_all(pb):
    if not pb:
        print("list is empty:[]")
else:
for in range(len(pb)):
    print(pb[i])
def thanks():
    print("...........................................................")
    print("thank you for using our smartphone directory system")
    print("please visi us again")
    print("...........................................................")
    sys.exit("goodbye, have a nice day ahead")
    print("...........................................................")
    print("hello dear user, welcome to the smartphone directory system")
    print("you may now proceed to explore the directory")
    print("...........................................................")
    ch==1
    pb = intial_phonebook()
    while ch in (1, 2, 3, 4, 5):
        ch = menu()
        if ch == 1:
            pb = add_contact(pb)
        elif ch == 2:
            pb = remove_contact(pb)
        elif ch == 3:
            pb = delete_all(pb)
        elif ch == 4:
            pb = search_existing(pb)
        elif ch == 5:
            diplay_all(pb)
        else
            thanks()