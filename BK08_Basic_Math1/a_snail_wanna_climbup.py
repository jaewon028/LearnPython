import math

if __name__ == "__main__":
    A, B, V = map(int, input().split())
    days = math.ceil((V - B) / (A - B))
    print(days)