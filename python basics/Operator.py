year = int(input("Enter a year: "))

# Check if it is a leap year
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# sub1 = int(input("Enter Subject 1 Marks: "))
# sub2 = int(input("Enter Subject 2 Marks: "))
# sub3 = int(input("Enter Subject 3 Marks: "))
# sub4 = int(input("Enter Subject 4 Marks: "))
# sub5 = int(input("Enter Subject 5 Marks: "))

# sum = sub1 + sub2 + sub3 + sub4 + sub5
# avg = sum/5

# if avg > 85:
#     print(" Grade Obtained is: A")
# elif avg >= 70:
#     print("Grade Obtained is: B")
# elif avg >= 45:
#     print(" Grade Obtained is: C")
# elif avg >= 35:
#     print("Grade Obtained is: D")
# else:
#     print(" Grade Obtained is: E")