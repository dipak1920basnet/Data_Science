import math
# unoptimize way
def main():
    number = int(input("Enter a number: "))
    if number  <= 1:
        print("The number is not prime")
        return
    
    # unoptimize check
    uncheck = unprime(number)
    check(number, uncheck)

    # optimize check
    opcheck = opprime(number)
    check(number, opcheck)

    # both optimize and unoptimze check funtion.
    both_check = bothPrime(number, optimize=False)
    check(number, both_check)

    both_check = bothPrime(number, optimize=True)
    check(number, both_check)

def unprime(n):
    # check if number is prime in unoptimized way

    if n == 2:
        return True
    i = 2
    while i <= (n-1):
        if n % i == 0:
            return False
        i +=1
    return True

def opprime(n):
    # check if number is prime in optimized way
    if n == 2:
        return True
    limit = int(math.sqrt(n))
    i = 2
    while i <= (limit):
        if n % i == 0:
            return False
        i +=1
    return True

def bothPrime(n, optimize=False):
    if n == 2:
        return True
    
    if optimize ==  True:
        limit = int(math.sqrt(n))
    else:
        limit = n-1

    i = 2
    while i <= (limit):
        if n % i == 0:
            return False
        i +=1
    return True


def check(number, condition:bool):
    if condition:
        print(f"The number: {number} is prime")
    else:
        print(f"The number: {number} is not prime")

if __name__ == "__main__":
    main()