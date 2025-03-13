if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


m1 = [x for x in range(n) for y in range(n) for z in range(n)]
print(m1)