age = int(input("Age in years: "))

if age > 1 or age < 99:
    seconds = str(age * (365 * 24 * 60 * 60))
    print("your age in seconds is", seconds)
    
else:
    print("Input valid age")

