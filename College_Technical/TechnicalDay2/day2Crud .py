import crud_functions as cf

while True:
    print(''' Choose the operation you want to perform:
    1. Add
    2. Display
    3. Update
    4. Delete
    5. Exit''')
    inp = int(input("Enter your choice: "))
    if inp == 1:
            cf.add()
    elif inp == 2:
            cf.display()
    elif inp == 3:  
            cf.update()
    elif inp == 4:
            cf.delete()
    elif inp == 5:
            break
    else:
            print("Invalid choice")   
        
