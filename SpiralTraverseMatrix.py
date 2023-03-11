#[[1, 2, 3, 4,],
# [5, 6, 7 , 8],
# [9, 10, 11, 12],
# [13, 14, 15, 16]
# ]

def solution(A):
    lbound = 0
    rbound = len(A[0])
    tbound = 0
    bbound = len(A)
    while lbound < rbound and tbound < bbound:
        # going from top left to top right
        for i in range(lbound, rbound):
            print(A[tbound][i])
        tbound += 1
        # going from top right to bottom right
        for i in range(tbound, bbound):
            print(A[i][rbound - 1])
        rbound -= 1

        if not(lbound < rbound and tbound < bbound):
            break
        # going from bottom right to bottom left
        for i in range(rbound-1, lbound-1, -1):
            print(A[bbound-1][i])
        bbound -= 1
        # going from bottom left to top right
        for i in range(bbound-1, tbound-1, -1):
            print(A[i][lbound])
        lbound += 1




A = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]

solution(A)
