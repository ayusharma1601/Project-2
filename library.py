dic={"Utopia":"Thomas More",
     "Odyssey":"Homer",
     "Othello":"William Shakespeare"}

while True:
    print("Welcome to the Library Management System")
    
    options=input("Enter what do you want to do?\n1. Check what books we have\n2. Add books of your choice\n3. search a particular book\n4 exit ")


    def add():
        while True:
            book = input("Enter the name of the book you want to add: ").title()
            author = input("Enter the name of the author: ").title()
            if book in dic:
                print("Book already exists")
            else:
                dic[book] = author
                print(f"{book} by {author} added successfully")
            more = input("Add another book? (y/n): ").lower()
            if more != "y":
                break

     
    def show(item_view):
        for key ,value in item_view.items():
            print(f"{key}:{value}")

     
    def search():
        find=input("what book you wanna search?: ").title()
        if find in dic:
            x=dic.get(find)
            print(x)
            print(f"{find} by {dic[find]} found")
        else:
            print("Book not found")
             
    if options=="1":
        show(dic)
         
    elif options=="2":
        add()
         
    elif options=="3":
        search()
         
    elif options=="4":
        print("Thank you for using the Library Management System")
        break
         
    else:
        print("Invalid Input")
