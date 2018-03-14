while True:
    try:
        N, Q = map(int, raw_input().split())

        grades = []

        for i in range(N):
            grades.append(int(raw_input()))

        new_grades = sorted(grades, reverse=True)

        for i in range(Q):
            print new_grades[int(raw_input())-1]
    except EOFError:
        break