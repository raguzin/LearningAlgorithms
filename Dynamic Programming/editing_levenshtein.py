def editing_lev(A, B):
    """Description function
    """

    # sequence length calculation
    n = len(A)
    m = len(B)

    # greating an empty two-dimensional array
    D = [0][0]
    for i in range(0, n):
        for j in range(0, m):
            if i == 0:
                D[i][j] = j
            elif j == 0:
                D[i][j] = i
            else:
                D[i][j] = 0
    print (D)

    # subsequence length calculation
    #for i in range(1, n + 1):
    #    for j in range(1, m + 1):
    #        if A[i-1] == B[j-1]:
    #            D[i][j] = D[i-1][j-1]
    #        else:
    #            D[i][j] = min(D[i-1][j-1]+1,D[i-1][j]+1,D[i][j-1]+1)
                #print (F[i][j])
    #print (F)

    return #(D[-1][-1])




if __name__ == "__main__":
    print("--------------------START-----------------------")
    A = str(input("Input sequnce A: "))
    B = str(input("Input sequnce B: "))
print("------------------------------------------------")
print("Count edits =", editing_lev(A, B))