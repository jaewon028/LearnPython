def sum_of_n(n):
    return(sum(n))

if __name__ == "__main__":
    a = list(map(int, input().split()))
    print(sum_of_n(a))