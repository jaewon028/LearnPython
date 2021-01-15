if __name__ == "__main__":
    result = int(input())
    for j in range(result):
        word = input()
        for i in range(1, len(word)):
            if word.find(word[i - 1]) > word.find(word[i]):
                result -= 1
                break
    print(result)
