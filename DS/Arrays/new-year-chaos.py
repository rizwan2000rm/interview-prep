def minimumBribes(q):
    totalBribed = 0
    for i in range(len(q)):
        # invalid case
        if(q[i] - (i + 1) > 2):
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if(q[j] > q[i]):
                totalBribed += 1
    print(totalBribed)
