# creating list in dictionary

phone = {'name': 'iphone 7',
        'specs': ['matte black', '128GB']
        }


print(phone['name'].title())

# printing specs
for spec in phone['specs']:
    print("\t" + spec)