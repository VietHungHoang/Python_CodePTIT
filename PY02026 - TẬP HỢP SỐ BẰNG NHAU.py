if __name__ == "__main__":
    input()
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    print("YES" if sorted(a) == sorted(b) else "NO")
