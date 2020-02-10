# Program that swaps letter cases in a string.
# 2020-02-10
program_title = "Case Swapper"
print("-"*len(program_title))
print(program_title)
print("-"*len(program_title))

userinput = input("Enter a mixed case string: ")
output = ""
for i, c in enumerate(userinput):
    # print(i, c, c.upper(), c.lower())
    if c.isupper():
        output += c.lower()
    else:
        output += c.upper()

print("input :", userinput)
print("output :", output)
