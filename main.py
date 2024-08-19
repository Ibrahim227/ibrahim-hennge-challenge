"""Import required Modules"""
import sys
from io import StringIO


def process_test_case(input_lines, idx):
    X = int(input_lines[idx])  # Read X (number of integers)
    integers = map(int, input_lines[idx + 1].split())  # Get the integers
    positives = filter(lambda x: x > 0, integers)  # Filter out negative integers
    squares = map(lambda x: x * x, positives)  # Square the positive integers
    return sum(squares)  # Sum the squares


def recursive_process(input_lines, idx, remaining):
    if remaining == 0:
        return []
    current_result = process_test_case(input_lines, idx)
    return [current_result] + recursive_process(input_lines, idx + 2, remaining - 1)


def main():
    # Read all input at once
    input_data = sys.stdin.read().splitlines()

    # Get the number of test cases
    N = int(input_data[0])

    # Start recursive processing of test cases
    results = recursive_process(input_data, 1, N)  # Start from the first test case

    # Print all results without blank lines between them
    print("\n".join(map(str, results)))


# Test input
test_input = """2
4
3 -1 1 14
5
9 6 -53 32 16"""

if __name__ == "__main__":
    # Mock stdin for testing
    sys.stdin = StringIO(test_input)

    # Run the main function
    main()
