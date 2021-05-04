bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_hight = 442 # Height (meters)
num_bills = 1
day = 1

while bill_thickness * num_bills < sears_hight:
    print("On day", day, "I put", num_bills,"bills on the sidewalk")
    day = day + 1
    num_bills = num_bills * 2

print("On day", day, "the bill stack of", num_bills, "bills reached the hight of", (bill_thickness * num_bills), "meters")