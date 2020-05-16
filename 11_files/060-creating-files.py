# "x" - Create. Creates the specified file, returns an error if the file exists

f = open("text1.txt", "x")
f.write("\nThis is new file")
f.close()