if __name__ == "__main__":
    num = int(input())
    cnt = 1
    count_sixs = 6
    count_room = 1
    while num > cnt:
        count_room += 1
        cnt += count_sixs
        count_sixs += 6

    print(count_room)