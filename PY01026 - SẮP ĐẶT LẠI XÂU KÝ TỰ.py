if __name__ == "__main__":
    for i in range(int(input())) :
        a = sorted(input())
        b = sorted(input())
        print('Test ' + str(i + 1) + ': ' + ('YES' if a == b else 'NO'))
