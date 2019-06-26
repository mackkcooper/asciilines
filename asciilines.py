import sys

background = ' '

# find tvg file
if (len(sys.argv) != 2): 
    print("ERROR: No argument provided. Please provide the path to the file you wish to have translated.")
    exit(2)
filename = sys.argv[1]
file = open(filename, 'r')
content = file.readlines()
file.close()

# parse tvg file
line = content[0].split(' ')
if(len(line) != 2):
    print("ERROR: File provided was unable to be parsed due to formatting.")
    exit(1)
height = int(line[0])
width = int(line[1])
if(height < 1 or width < 1):
    print("ERROR: File provided has canvas height and/or width values less than 1.")
    exit(1)

# generate graphical array
canvas = [[background] * width for i in range(height)]

# fill graphical array

# ouput graphical array to user
for row in canvas:
    for element in row:
        print(element, end='')
    print()