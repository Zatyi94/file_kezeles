
my_list = ['test', 'line']

# w azt jelenti write
with open('my_file.txt', 'w') as file:
    for item in my_list:
        file.write('{}\n'.format(item))
