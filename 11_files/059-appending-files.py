# "a" - Append. Opens a file for appending, creates the file if it does not exist

f = open("text.txt", "a")
f.write("\nThis is appended text")
f.close()