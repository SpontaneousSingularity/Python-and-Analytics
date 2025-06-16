 # Dict -> Collection of data in key value pair

# Phone Book
# Key - Name, Values - Phone Numbers
contacts={
    "Yuvraj":"+91 12121 12121",
    "Rohit":"+91 32323 32323",
    "Umar":"+91 56565 65656",
    "Sultan":"+91 87878 78787",
    "Umar":"+91 42042 04204"    
} 

print(contacts)

# INSERT
contacts["Pranjal"] = "+91 52525 25252"
print(contacts)

# if the Key already exist then its value will be updated
contacts["Rohit"] = "+91 87575 87575"
print(contacts)

#gives the value of the key
print(contacts.get("Pranjal"))

contacts.pop("Umar")

print(contacts)

for key in contacts:
    print(f"{key} = {contacts.get(key)}")