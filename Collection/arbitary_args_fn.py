def sum(*all_numbers):
    print(all_numbers)
    print(type(all_numbers))
    add = 0
    for i in all_numbers:
        add += i
    
    print(f"sum is {add}")