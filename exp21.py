def add(a, b):
	print(f"Adding {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"subtracting {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"multiplying {a} * {b}")
	return a * b

def divide(a, b):
	print(f"dividing {a} / {b}")
	return a / b

print ("Lets do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, height: {height}, weight: {weight}, iq = {iq}")


#A puzzle for the extra credit type it in anyway.

print("Here is the puzzle")

what = add(age, subtract(height,multiply(weight,divide(iq,2))))

print("That becomes: ", what, "can you do it by hand?")




