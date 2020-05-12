# "w" - Write. Opens a file for writing, creates the file if it does not exist
# if there is data written, will override and deletes old data

f = open("text.txt", "w")
f.write("Hello world")
f.close()