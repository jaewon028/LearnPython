if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())

    list_result = list(str(A * B * C))
    for i in range(10):
        print(list_result.count(str(i)))