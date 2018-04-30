name = ARGV[0]
file_name = ARGV[1]
lines = ARGV[2]
lines = lines.to_i

#puts name
#puts file_name
#puts lines

# reads file_name and display last lines of the file
readMe = IO.readlines(file_name).last(lines)
puts readMe