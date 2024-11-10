"""Comp110 dictionary exercise6"""

__author__: str = "730653037"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate values are not allowed in the input dictionary!")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Finds the most frequent color in a dictionary of names and colors"""
    color_counts = {}
    first_occurrence = {}

    for i, (name, color) in enumerate(colors.items()):
        if color not in color_counts:
            color_counts[color] = 0
            first_occurrence[color] = i
        color_counts[color] += 1

    max_count = 0
    most_frequent_color = ""
    min_index = float("inf")

    for color, count in color_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_color = color
            min_index = first_occurrence[color]
        elif count == max_count and first_occurrence[color] < min_index:
            most_frequent_color = color
            min_index = first_occurrence[color]

    return most_frequent_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the frequency of each unique value in a list of strings."""
    result = {}
    for item in input_list:
        if item not in result:
            result[item] = 1  # If the item is not found, assign initial count of 1
        else:
            result[item] += 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorizes a list of words into different lists based on their starting letter"""
    if not words:
        return {}

    alpha_dict = {}
    for word in words:
        if not word:  # Handle empty strings
            continue
        first_letter = word[0].lower()
        if "a" <= first_letter <= "z":
            if first_letter in alpha_dict:
                alpha_dict[first_letter].append(word)
            else:
                alpha_dict[first_letter] = [word]
    return alpha_dict


def update_attendance(
    attendance_dict: dict[str, list[str]], day: str, student: str
) -> None:
    """Updates the attendance dictionary with new attendance information"""
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return None
