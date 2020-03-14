# 6259 Dic 07
def is_num_or_alp(dicInput):
    ansDic = dict(letters=0, digits=0)
    for words in dicInput:
        if ((words >= 'A') and (words <= 'Z')) or ((words >= 'a') and (words <= 'z')):
            ansDic["letters"] += 1
        elif (words >='0') and (words <= '9'):
            ansDic["digits"] += 1
    return ansDic


input_dic = input("딕셔너리 입력 07 : ")
print(is_num_or_alp(input_dic))
ans = is_num_or_alp(input_dic)
print("LETTERS {}\nDIGITS {}".format(*ans.values()))
