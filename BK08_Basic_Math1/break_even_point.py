if __name__ == "__main__":
    A, B, C = map(int, input().split())
    # total_fee = A + B*x
    # price = C*x

    break_even_pint = 0
    if B >= C:
        print(-1)
    else:
        break_even_pint = (A // (C - B)) + 1
        print(break_even_pint)