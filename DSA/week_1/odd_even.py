def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__ == "__main__":
    print(even_or_odd(int(input("Enter a number to check:"))))
