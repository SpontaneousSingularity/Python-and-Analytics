stack = []
def add():
    id = int(input("Enter id: "))
    name = input("Enter name: ")
    rollno = int(input("Enter rollno: "))
    city = input("Enter city: ")
    stack.append([id,name,rollno,city])
    print("Record added successfully")


def display():

    print("ID\tName\tRollno\tCity")
    print("----------------------------------")

    for i in stack:
        for j in i:
            print(j,end="\t")
        print("\n----------------------------------")


def update():
    id = int(input("Enter id: "))
    wp = input('''Enter what you want to update: 
               1. name
               2. rollno
               3. city
               4. id
               choice: ''')
    for i in stack:
        if i[0] == id:
            if wp == 4:
                i[0] = int(input("Enter id: "))
            elif wp == 1:
                i[1] = input("Enter name: ")
            elif wp == 2:
                i[2] = int(input("Enter rollno: "))
            elif wp == 3:
                i[3] = input("Enter city: ")
            else:
                print("Invalid choice")
            
            print("Record updated successfully")
            break
    else:
        print("Record not found")


def delete():
    id = int(input("Enter id: "))
    for i in stack:
        if i[0] == id:
            stack.remove(i)
            print("Record deleted successfully")
            break
    else:
        print("Record not found")
