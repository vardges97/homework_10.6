formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "i had this thing",
    "that you could type up right",
    "but it didnt sing",
    "so i said goodnight"
))
#1 Take the formatter string defined on line 1.
#{}{}{}{}{}
#3. Pass to format four arguments, which match up with the four {} in the formatter variable. This is like passing arguments to the command line command format

print(formatter.format('house', 'home', 'greg', 'apartment'))
