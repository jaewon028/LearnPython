if __name__ == "__main__":
    S = input()
    upper_S = S.upper()
    list_check = []

    words = [chr(n) for n in range(ord('A'), ord('Z')+1)]

    for i in range(ord('A'), ord('Z') + 1):
        list_check.append(upper_S.count(chr(i)))

    if list_check.count(max(list_check)) > 1 :
        print("?")
    else:
        max_index = list_check.index(max(list_check))
        print(words[max_index])
