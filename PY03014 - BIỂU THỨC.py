if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        st = []
        idx = 1
        for x in s:
            if x == '(': 
                print(idx, end=' ')
                st.append(idx)
                idx += 1
            elif x == ')':
                print(st.pop(), end=' ')
        print()
        