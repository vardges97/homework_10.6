tabby_cat = "\tI'm tabbed in white,black,orange."
persiancat = "I'm split\nblack and white."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persiancat)
print(backslash_cat)
print(fat_cat)

#2. Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
#you can use both but there are drawbacks to '''
#3Combine escape sequences and format strings to create a more complex format.
country = 'Armenia'
print(f"I live in \n {country}")
print('I live in {}'.format(country))