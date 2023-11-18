name = input("what's your name?").strip().title()
#Remove whitespace from str and capitalize user name

#split user's name into first name and last name

first, last= name.split(" ")

#say hello to user
print(f"hello, {first,last}")

