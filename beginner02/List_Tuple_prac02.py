# 6295 List 18
input18 = input("리스트 18번 입력 : ").split(",")
print("{} => {}".format(type(input18), input18))
list18=[]
for i in range(int(input18[0])):
    matrix = []
    for j in range(int(input18[1])):
        matrix.append(i*j)
    list18.append(matrix)

print(list18)

inputSub18 = input("더 간단한 리스트 18번 입력 : ").split(",")
listSub18 = [[row*col for col in range(int(inputSub18[1]))] for row in range(int(inputSub18[0]))]
print(listSub18)

# 6296 List 19
list19 = sorted(input("리스트 19번 입력 : ").split(","))
print(list19)
