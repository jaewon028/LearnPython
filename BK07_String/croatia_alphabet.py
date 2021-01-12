if __name__ == "__main__":
    a = 'c='
    b = 'c-'
    c = 'dz='
    d = 'd-'
    e = 'lj'
    f = 'nj'
    g = 's='
    h = 'z='
    list_croatia = [a,b,c,d,e,f,g,h]
    S = input()

    for i in list_croatia:
        S = S.replace(i, 'a')
    print(len(S))