if __name__ == '__main__':
    name_li = []
    score_li = []
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        name_li.append(name)
        score_li.append(score)
    score_li = list(set(score_li))
    score_li.sort()
    second_low = score_li[1]
    res = [i[0] for i in records if i[1] == second_low]
    res.sort()
    for i in res:
        print(i)