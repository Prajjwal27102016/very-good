def no_notes(a):
    Q = [3000, 500, 600, 200, 70, 40, 20]
    x = 0
    for i in range(7):
        q = Q[i]
        x = a // q
        print("notes of {}={}".format(q, x))
        a = a % q
        amount = int(input("Enter total amount:"))   
        no_notes(amount)