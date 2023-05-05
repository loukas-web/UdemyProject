feet_inches = input("Enter feet and inches: ")


def convert(func_feet_inches):
    parts = func_feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    
    meters = feet * 0.3048 + inches * 0.0254
    
    return meters


result = convert(feet_inches)

if result < 1:
    print("Kid id too small")
else:
    print("Kid can use the slide")
