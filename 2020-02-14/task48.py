# Program that prints a grid
# 2019-11-18
program_title = "Grid"
print("-"*len(program_title))
print(program_title)
print("-"*len(program_title))
print("")

n = 5
for x in range(n):
    rstart = x*2+1
    print("")
    cval = rstart
    for y in range(n):
        print(cval%10, end=" ")
        cval += 2

print("\n")

nums = [2*i+1 for i in range(n)]
for row in range(n):
    for val in nums:
        print(val, end=" ")
    print()
    # print(nums)
    nums.append(nums.pop(0))