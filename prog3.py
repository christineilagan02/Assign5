# Create a program that ask for an age of a person
# Display the life stage of the person.
# Rules:
# 0 - 12 : Kid
# 13 - 17 : Teen
# 18 : Debut
# 19 above : Adult

age = int(input("Age: "))

if age > -1 and age <= 12:
    print("Kid")
elif age >= 13 and age <= 17:
    print("Teen")
elif age == 18:
    print("Debut")
else: 
    print("Adult")

print("Done")