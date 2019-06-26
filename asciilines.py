import sys

# find tvg file
if (len(sys.argv) != 2): 
    print("ERROR: No argument provided. Please provide the path to the .tvg file you wish to have translated.")
    exit()
filename = sys.argv[1]
file = open(filename, 'r')
content = file.readlines()

# parse tvg file

# generate graphical array

# ouput to user