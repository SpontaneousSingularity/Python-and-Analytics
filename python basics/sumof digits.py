n= int(input("enter number: "))
sum = 0
while n!= 0:
    remainder =n % 10
    sum += remainder
    n = n//10

print(f"sum of Digits is {sum}")