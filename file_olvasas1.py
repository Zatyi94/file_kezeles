# open: megnyit egy file-t és visszaad egy streamet
file = open('./temp.txt')

print(file)

lines = file.readlines()
print(lines)
nums = []
for line in lines:
    nums.append(int(line))

file.close()

print(nums)
