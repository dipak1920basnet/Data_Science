def even_or_odd(n):
    if (n & 1) == 1:
        return "odd"
    else:
        return "even"

if __name__ == "__main__":
    get_num = input("Enter a number: ")
    print(even_or_odd(int(get_num)))