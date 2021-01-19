def fibonacci(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


if __name__ == "__main__":
    print(fibonacci(int(input())))