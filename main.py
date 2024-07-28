def main(*args: int) -> int:
    return sum(args)

t = main(1, 2, -3, 4, 50, 100)
print(t)
#
dist = {'username': 'Ibrahim', 'last_name': 'Manzo', 'password': "2123334"}
sep = ':'
x = sep.join(dist)
print(str(x))

if __name__ == '__main__':
    main()
