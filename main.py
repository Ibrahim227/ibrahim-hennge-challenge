from typing import List


def main(*args: List[int]):
    return sum(*args)

t = main(1, 2, 4, 50, 100)
print(t)
#
# dist s

if __name__ == '__main__':
    main()
