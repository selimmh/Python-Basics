#method 'strip' deletes all empty spaces in string

address = "     18 Main Street     "
print(address.strip())


#method 'rstrip' deletes empty spaces just from right
#method 'lstrip' deletes empty spaces just from left

address = "18 Main Street     "
print(address.rstrip())

address = "     18 Main Street"
print(address.lstrip())