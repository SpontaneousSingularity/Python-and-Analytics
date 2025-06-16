n= int(input("enter number: "))
num = n
reverse = 0
while n!= 0:
    remainder =n % 10
    reverse = reverse*10 + remainder
    n = n//10

if num == reverse:
    print(f" The number {n} is palindrome")
else: 
    print(f" The number {n} is not palindrome")