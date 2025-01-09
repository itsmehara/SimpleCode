def add_numbers(a, b):
    # Adding two numbers
    result = a + b
    print(f"The sum of {a} and {b} is {result}")


def reverse_string(s):
    # Reversing a string
    reversed_str = s[::-1]
    print(f"The reverse of '{s}' is '{reversed_str}'")


def factorial(n):
    # Calculating factorial of a number
    def calc_factorial(x):
        if x == 0:
            return 1
        else:
            return x * calc_factorial(x - 1)

    result = calc_factorial(n)
    print(f"The factorial of {n} is {result}")


def square_elements(lst):
    # Squaring elements in a list
    squared_list = [x ** 2 for x in lst]
    print(f"The square of the elements {lst} is {squared_list}")


def count_vowels(s):
    # Counting vowels in a string
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    print(f"The number of vowels in '{s}' is {count}")


def main():
    # Initializing variables
    num1 = 5
    num2 = 10
    string1 = "hello"
    num3 = 5
    list1 = [1, 2, 3, 4, 5]
    string2 = "beautiful day"

    # Calling functions
    add_numbers(num1, num2)
    reverse_string(string1)
    factorial(num3)
    square_elements(list1)
    count_vowels(string2)


if __name__ == "__main__":
    main()


