if __name__ == "__main__":
    S = input()
    reverse_S = ''.join(reversed(S)) # list 나 string 들어왔을때, join으로 문자열 구분가능.
    list_S = list(map(int, reverse_S.split()))

    if list_S[0] > list_S[1]:
        print(list_S[0])
    else:
        print(list_S[1])
