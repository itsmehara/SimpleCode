# Simple Dictionary Operations in Python

# Creating a dictionary
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Daisy": 88
}

# Adding a new entry
student_grades["Eve"] = 95

# Modifying an existing entry
student_grades["Charlie"] = 82

# Iterating through the dictionary
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# Calculating the average grade
average_grade = sum(student_grades.values()) / len(student_grades)
print(f"Average Grade: {average_grade:.2f}")
