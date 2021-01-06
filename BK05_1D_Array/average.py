if __name__ == "__main__":
    int(input())
    list_score = list(map(int, input().split()))

    max_score = max(list_score)
    manipulated_score = []
    for i in range(len(list_score)):
        manipulated_score.append((list_score[i]/max_score) *100)

    result = 0
    for i in range(len(list_score)):
        result += manipulated_score[i]

    print(result/len(manipulated_score))