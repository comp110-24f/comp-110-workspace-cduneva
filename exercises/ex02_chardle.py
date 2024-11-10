def find_car_renter(names: list[str], ages: list[int]) -> str:
    """Find the name of first person who is at least 25"""
    if len(names) != len(ages):
        raise ValueError("The length of names and ages must be the same.")
    # Loop through ages list
    for idx in range(0, len(ages)):
        if ages[idx] >= 25:  # If >= 25, print and return their name!
            print(names[idx] + " is at least 25!")
            return names[idx]
    print("Looks like nobody is old enough to rent a car...")


def find_eligible(names: list[str], ages: list[int]) -> dict[str, int]:
    eligibles: dict[str, int]
    for idx in range(0, len(names)):
        if ages[idx] >= 25:
            eligibles[names[idx]] = ages[idx]
    return eligibles


names = ["Allan", "Ken", "Barbie"]
ages = [23, 26, 25]
driver = find_car_renter(names, ages)
