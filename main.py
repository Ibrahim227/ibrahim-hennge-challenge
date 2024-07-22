def main(*args: int) -> int:
    return sum(args)

t = main(1, 2, -3, 4, 50)
print(t)
if __name__ == '__main__':
    main()
