import sys

name = sys.argv[1]
file_name = sys.argv[2]
lines = sys.argv[3]

# open file, readlines, and assign list to readMe
readMe = open(file_name).readlines()
#print(readMe)

# uses the slice notation with the negative integer variable (lines) to get the last elements in the list
lines = int(lines)
last_line_slice = readMe[-(lines):]
print(last_line_slice)
