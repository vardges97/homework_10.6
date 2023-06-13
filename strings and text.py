types_of_people = 10
#using f string adds a var in input
x = f"There are {types_of_people} types of people."

#using f strings adds 2 vars
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

#prints 2 strings of text adds vars in text using f
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#prints text using .format and chooses var that needs adding
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#concatination
print(w + e)

#2. Find all the places where a string is put inside a string.
# everywhere where {} is used except hilarious
#3Are you sure there are only four places? How do you know? Maybe I like lying
#not in 4 but in 5 places
#4Explain why adding the two strings w and e with + makes a longer string
#using + with strings creates a new string that is both combined
