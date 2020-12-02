
nums = []

# a with kulcsszóval nem kell close-olni a file-t
# (nem kell külön meghívni a close fgv-t), hanem a
# blokk végén automatikusan bezárul a file
# r = reed (olvasásra nyitottuk meg)
with open('./temp.txt', 'r') as file:
    for line in file:
        nums.append(int(line))

print(nums)
