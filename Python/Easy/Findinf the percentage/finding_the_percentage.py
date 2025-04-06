if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = student_marks[query_name] / student_marks[query_name]

    print(format(result), "%.2f")




#     for j in student_marks[query_name]:
#         total = total + j

# per = total/len(student_marks[query_name])
# print("%.2f" % per)