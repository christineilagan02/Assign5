# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

tine = int(input("Enter the money of tine: "))
jelenie = int(input("Enter the money of jelenie: "))
jiyanie = int(input("Enter the money of jiyanie: "))

if tine < jelenie and tine < jiyanie:
    print("The lowest money is tine!")
elif jelenie < tine and jelenie < jiyanie:
    print("The lowest money is jelenie!")
else:
    print("The lowest money is jiyanie")

print("May libre ka!")
