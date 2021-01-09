if __name__ == "__main__":
    S = input()
    list_check = []

    for i in range(ord('a'), ord('z')+1):
        list_check.append(S.find(chr(i)))

    for i in range(len(list_check)):
        print(list_check[i], end=" ")