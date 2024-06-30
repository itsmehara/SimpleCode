def basic_calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice(1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")


def fibonacci_sequence():
    def fibonacci(n):
        sequence = [0, 1]
        while len(sequence) < n:
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
        return sequence

    n = int(input("Enter the number of terms: "))
    fib_sequence = fibonacci(n)
    print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")


def simple_class_and_object():
    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print(f"{self.name} says Woof!")

        def get_age(self):
            return self.age

    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Lucy", 5)

    dog1.bark()
    dog2.bark()

    print(f"{dog1.name} is {dog1.get_age()} years old.")
    print(f"{dog2.name} is {dog2.get_age()} years old.")


def file_operations():
    # Writing to a file
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")

    # Reading from a file
    with open("example.txt", "r") as file:
        content = file.read()
        print("File Content:\n", content)


def dictionary_operations():
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


def main():
    print("1. Basic Calculator")
    print("2. Fibonacci Sequence")
    print("3. Simple Class and Object")
    print("4. File Operations")
    print("5. Dictionary Operations")
    choice = input("Select a function to run (1/2/3/4/5): ")

    if choice == '1':
        basic_calculator()
    elif choice == '2':
        fibonacci_sequence()
    elif choice == '3':
        simple_class_and_object()
    elif choice == '4':
        file_operations()
    elif choice == '5':
        dictionary_operations()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
