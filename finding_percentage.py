n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
b=list(student_marks[query_name])
a=sum(b)/len(b)
print('%.2f'%a)
    