if __name__ == "__main__":
    input()
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    print(*sorted(a.intersection(b)))
    print(*sorted(a.difference(b)))
    print(*sorted(b.difference(a)))
