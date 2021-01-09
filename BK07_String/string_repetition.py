if __name__ == "__main__":
    for i in range(int(input())):
        R, S = input().split()
        R = int(R)
        for j in range(R*len(S)):
            print(S[j//R], end="")
        print()