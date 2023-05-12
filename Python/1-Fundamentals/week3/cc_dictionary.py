inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def total_inches(inches_snow):

    total_inches = 0

    for inches in inches_snow.values():

        total_inches = total_inches + inches

    return total_inches


inches = total_inches(inches_snow)
print("Total snowfall inches: ", inches)

thursday_snowfall = input("How many inches of snow fell on Thursday? ")
inches_snow["Thursday"] = int(thursday_snowfall)

inches = total_inches(inches_snow)
print("Total snowfall inches: ", inches)
