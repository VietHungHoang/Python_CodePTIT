if __name__ == "__main__":
    a = input()
    b = input()
    p = int(input()) - 1
    print(a[:p:] + b + a[p::])