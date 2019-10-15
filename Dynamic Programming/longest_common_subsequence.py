def lcs(A, B):
    """Description function
    """

    # sequence length calculation
    n = len(A)
    m = len(B)

    # greating an empty two-dimensional array
    F=[[0]*(m + 1) for i in range(n + 1)]
    #print (F)

    # subsequence length calculation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1+F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j],F[i][j-1])
                #print (F[i][j])
    #print (F)

    # subsequence calculation
    seq = ''
    i = n
    j = m
    while F[i][j] > 0:
        if F[i][j] == F[i][j - 1]:
            j -= 1
        elif F[i][j] == F[i - 1][j]:
            i -= 1
        else:
            seq = A[i - 1] + seq
            i -= 1
            j -= 1
    return (F[-1][-1], seq)




if __name__ == "__main__":
    print("--------------------START-----------------------")
    A = str(input("Input sequnce A: "))
    B = str(input("Input sequnce B: "))
print("------------------------------------------------")
print("Longest common subsequence =", lcs(A, B))