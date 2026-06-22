if __name__ == '__main__':
    n = int(input().strip())
    students = []

    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name,score])

    scores = []
    for s in students:
        if s[1] not in scores:
            scores.append(s[1])

    scores.sort()

    second_score = scores[1]
    result = []
    for s in students:
        if s[1] == second_score:
            result.append(s[0])
    result.sort()
    for name in result:
        print(name)


