while True:
    try:
        N, C, T1, T2 = map(int, raw_input().split())

        distances = map(int, raw_input().split())

        from_t1 = []
        from_t2 = []

        size = len(distances)

        for i in range(size):
            j = distances[i]
            count = 1
            while j - distances[i] <= T1:
                #print distances[(i+count) % N], j
                if distances[(i+count) % N] == j % C:
                    count += 1
                j += 1
            from_t1.append(count)

        for i in range(size):
            j = distances[i]
            count = 1
            while j - distances[i] <= T2:
                if distances[(i+count) % N] == j % C:
                    count += 1
                j += 1
            from_t2.append(count)

        best_result = 99999999999
        print from_t1
        print from_t2
        for i in range(size):
            dist = 0
            holes_fixed = 0
            j = i
            while holes_fixed < N:
                left = N - holes_fixed
                if from_t1[j] > from_t2[j]:
                    if from_t1[j] > left:
                        if from_t2 >= left:
                            if T1 < T2:
                                best = from_t1[j]
                                chosen = T1
                            else:
                                best = from_t1[j]
                                chosen = T1
                        else:
                            best = from_t1[j]
                            chosen = T1
                        
                elif from_t1[j] < from_t2[j]:
                    best = from_t2[j]
                    chosen = T2
                    j = (j + from_t2[j]) % size
                else:
                    holes_fixed += from_t1[j]
                    dist += min(T1, T2)
                    j = (j + from_t1[j]) % size

                holes_fixed += best
                dist += chosen
                j = (j + best) % size
            if dist < best_result:
                best_result = dist

        for i in range(size):
            dist = 0
            holes_fixed = 0
            j = i
            while holes_fixed < N:
                holes_fixed += from_t2[j]
                dist += T2
                j = (j + from_t1[j]) % size
            if dist < best_result:
                best_result = dist

        print best_result

    except EOFError:
        break