if __name__ == '__main__':
    l1 = []
    N = int(input())
    for _ in range(N):
        value = map(str,input().split())
        value_list = list(value)
        if value_list[0] == 'insert':
           l1.insert(int(value_list[1]), int(value_list[2]))
        elif value_list[0] == 'print':
            print(l1)
        elif value_list[0] == 'remove':
            l1.remove(int(value_list[1]))
        elif value_list[0] == 'append':
            l1.append(int(value_list[1]))
        elif value_list[0] == 'sort':
            l1.sort()
        elif value_list[0] == 'pop':
            l1.pop()
        elif value_list[0] == 'reverse':
            l1.reverse()