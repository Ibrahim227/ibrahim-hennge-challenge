import sys
from io import StringIO

# Simulate input
test_input = """2
4
3 -1 1 14
5
9 6 -53 32 16"""

sys.stdin = StringIO(test_input)


def main():
    input_data = sys.stdin.read().splitlines()
    N = int(input_data[0])

    def process_test_case(input_lines, idx):
        X = int(input_lines[idx])
        integers = map(int, input_lines[idx + 1].split())  # read space-separated integers
        positives = filter(lambda x: x > 0, integers)  # filter out negative integers
        squares = map(lambda x: x * x, positives)  # square the positive integers
        return sum(squares)  # Calculate the sum of squares and store the results

    def recursive_process(idx, remaining):
        if remaining == 0:
            return []
        current_result = process_test_case(input_data, idx)
        return [current_result] + recursive_process(idx + 2, remaining - 1)

    results = recursive_process(1, N)
    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()
