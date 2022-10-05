print("Welcome to our community")
print("Please fill the following required fields:)")
name = str(input("Your name: "))
while not name.isalpha():
    print("Please enter right information")
    name = input("Your name: ")
    if name.isalpha():
        continue

age = input("Your age: ")
while not age.isdigit():
    print("Please enter right information")
    age = input("Your age: ")
    if age.isdigit():
        continue

address = input("Your address: ")
while not address.isalpha():
    print("Please enter right information")
    address = input("Your address: ")
    if address.isalpha():
        continue

print("Hello Mr/Ms ", name, " age ", age, " located in ", address, ".",
      '''
Thanks for being one of our community, Enjoy.
''')
