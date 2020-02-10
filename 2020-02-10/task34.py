# Program that removes character from string.
# 2020-02-10
program_title = "Character Remover"
print("-"*len(program_title))
print(program_title)
print("-"*len(program_title))

userstr = input("Enter a string: ")
userchr = input("Enter a character: ")

if len(userchr) != 1:
    print("Please enter a single character.")
else:
    output = ""

    for c in userstr:
        if c != userchr:
            output += c

    print("input :", userstr)
    print("output :", output)
