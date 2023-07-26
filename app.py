x = input("What is your weight: ")
y = input("(k)g or (l)bs: ")
if y=='k':
    print("You have " + str(int(float(x)*2.2)) + " lbs")
elif y=='l':
    print("You have " + str(int(float(x)/2.2)) + " kg")
else:
    print("Enter a valid letter")
