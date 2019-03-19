print("Lets practice everything.")
print('You\'d need to know \'bout escape \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic firmly planted
connot discern \n the need of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is some.
"""

print("--------------")
print(poem)
print("--------------")

five = 10-2+3-6
print(f"this should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans/1000
	creates = jars / 100
	return jelly_beans, jars, creates


start_point = 10000
beans, jars, creates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of :{}".format(start_point))
# its just like with an f"" string
print(f"we'd have {beans} beans, {jars} jars and creates {creates}.")

start_point = start_point / 10

print("We can also do that this way:")

formula = secret_formula(start_point)
print(formula)
#this is an easy way to apply a list to a format string

print("we'd have {}beans, {} jars, and {}creates.".format(*formula))

