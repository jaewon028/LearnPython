if __name__=="__main__":
    C = int(input())

    for i in range(C):
        sum_score = 0
        rate_over_cnt = 0

        list_score = list(map(int, input().split()))
        student_num = len(list_score)-1
        for j in range(1, len(list_score)):
            sum_score += list_score[j]

        average = sum_score/student_num

        for j in range(1, len(list_score)):
            if list_score[j] > average :
                rate_over_cnt += 1

        SORROW_FACT = (rate_over_cnt/student_num)*100
        print("%0.3f%%" %SORROW_FACT)