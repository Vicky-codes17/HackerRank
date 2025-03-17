if __name__ == '__main__':

    student = []

    for _ in range(int(input())):
        name = sorted(input())
        score = float(input())

    score  = sorted(set(score for name,score in student))
    s_lowest = score[1]

    name = sorted([name for name,score in student if score == s_lowest])

    for s_lowest_name in name:
        print(s_lowest_name)
        
