from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you dont want that, hit CNTRL-C (^C).")
print("If you dont want that, hit RETURN.")

input("?")

print("Opening the file ...")
target = open (filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am going to ask you for three lines.")

line1 = input("Line1 :")
line2 = input("Line2 :")
line3 = input("Line3 :")

print("I am gonna write this into file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("And finally we close it.")

target.close()
