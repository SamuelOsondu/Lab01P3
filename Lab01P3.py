# a) Print a simple “Geaux Tigers!” message code to the standard output (monitor).
print("Geaux Tigers!")

# b) Calculate the volume of a sphere using the formula v = 4/3 x p x r3, and store it in a floating point variable vol.
# Print vol to the standard output (monitor).
pi = 22/7
radius = float(input("Input the radius of the sphere: "))
vol = float(4/3 * pi * radius**3)
print(f"The volume of the sphere is: {vol}.")


# c) Initialize an integer array p with the following 10 values: 8, 4, 7, 65, 29, 18, -5, 12, 6, 0.
# Then add instructions to do the following:
p = [8, 4, 7, 65, 29, 18, -5, 12, 6, 0]
p[3] = 11
num = p[6]
p[6] = p[4]
p[4] = num

for i in range(len(p)):
    p[i] *= 4
    print(f"p[{i}] = {p[i]}")

# iv. Use a for loop with a step to print out the 1st, 3rd, 5th, 7th, and 9th elements
for i in range(0, len(p), 2):
    print(f"Element at index {i}: {p[i]}")

# v. Sum all the values in p and display the sum
psum = sum(p)
print(f"The sum of the array values is: {psum}")

# Part d: Check the conditions and print A, B, or C
if (psum > 15 and psum % 3 == 0) or psum > 50:
    print("A")
elif psum % 2 == 0:
    print("B")
else:
    print("C")

