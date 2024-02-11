def sort_students_by_scores(students_scores):
    # Sort the dictionary by its values in descending order
    # students_scores.items() return tuples with (key,value) and parameter key is used to determine on what value the sorting is performed

    sorted_tuples = sorted(
        students_scores.items(), key=lambda item: item[1], reverse=True
    )
    # Convert the sorted list of tuples back into a dictionary
    sorted_dict = dict(sorted_tuples)
    return sorted_dict


# Example usage
students_scores = {
    "Alice": 88,
    "Bob": 75,
    "Charlie": 90,
    "David": 85,
}
sorted_students_scores = sort_students_by_scores(students_scores)
print(sorted_students_scores)
