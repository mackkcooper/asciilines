import sys

background = '.'

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
if (len(line) != 2):
    print("ERROR: File provided was unable to be parsed due to formatting.")
    exit(1)
height = int(line[0])
width = int(line[1])
if (height < 1 or width < 1):
    print("ERROR: File provided has canvas height and/or width values less than 1.")
    exit(1)

# generate graphical array
canvas = [[background] * width for i in range(height)]

# fill graphical array
for l in range(1,len(content)):
    line = content[l].split(' ')
    if (len(line) != 5):
        print("ERROR: File provided was unable to be parsed due to formatting.")
        exit(1)
    char = line[0]
    h = int(line[1])
    w = int(line[2])
    direction = line[3]
    length = int(line[4])
    if (direction == 'v'): #vertical
        if (w > -1 and w < width):
            for i in range(length):
                if ((h + i) > -1 and (h + i) < height):
                    canvas[h + i][w] = char
    elif (direction == 'h'):  #horizontal
        if (h > -1 and h < height):
            for i in range(length):
                if ((w + i) > -1 and (w + i) < width):
                    canvas[h][w + i] = char
    else:
        print("ERROR: File provided was unable to be parsed due to formatting.")
        exit(1)

# ouput graphical array to user
for row in canvas:
    for element in row:
        print(element, end='')
    print()