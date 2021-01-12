if __name__ == "__main__":
    S = input()
    list_alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    dial_time = 0

    for i in range(len(S)):
        for j in list_alphabet:
            if S[i] in j :
                dial_time += list_alphabet.index(j) +3

    print(dial_time)
