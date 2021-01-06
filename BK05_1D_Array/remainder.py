if __name__ == "__main__":
    list_num = [int(input()) % 42 for i in range(10)]
    print(len(set(list_num)))