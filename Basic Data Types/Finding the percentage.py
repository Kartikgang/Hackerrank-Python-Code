if __name__ == '__main__':
    n = int(input())

    student_marks = {}

    for _ in range(n):
        name, *marks = input().split()
        scores = list(map(float,marks))
        student_marks[name] = scores
    
    query_name = input()

    query_marks = student_marks[query_name]
    avg_marks = sum(query_marks) / len(query_marks)
    
    print(f"{avg_marks:.2f}")

