"""Comp110 Tea Party Exercise"""

__author__: str = "730653037"
# docstring and author variables


def tea_bags(people: int) -> int:
    """defining the function tea bags"""
    return int(people + people)


# the tea_bags function is defined with the integer parameter people to return an integer 2 times the number of people


def treats(people: int) -> int:
    """defining the function treat"""
    return tea_bags(people=people * 1.5)


# callled the tea bags function inside the treats definition
# the treats function is defined with the integer parameter people to return an integer 1.5 times the value of people


def cost(tea_count: int, treat_count: int) -> float:
    """defining the function cost"""
    return (treat_count * (0.75)) + (tea_count * (0.5))


# the cost function is defined with parameters tea_count and treat_count


def main_planner(guests: int) -> None:
    """main planning loop"""
    print("A Cozy Tea Party for " + str(guests) + " People")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(format(cost(tea_bags(people=guests), treats(people=guests)), ".2f"))
    )


# the main planning loop calls and prints the previously defined functions with phrases around them


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    """main loop begins"""
    # function to begin the code
