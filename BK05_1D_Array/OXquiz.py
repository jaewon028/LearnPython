if __name__ == "__main__":
    num = int(input())

    for i in range(num):
        quiz_list = list(input())
        score_sum = 0
        cnt = 1
        for j in quiz_list:
            if j == 'O':
                score_sum += cnt
                cnt += 1
            else:
                cnt = 1
        print(score_sum)
