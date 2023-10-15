if __name__ == '__main__':

    for _ in range(int(input())):
        cnt = [0] * 1005
        for _ in range(int(input())): cnt[int(input())] += 1
        res = 1
        for x in range(1, 1001):
            if cnt[x] > cnt[res]: res = x
        print(res)
        