def clearZeros(Mat, row, col):
    """
    Given a matrix and the row and column index
    This will clear out all the elements in the
    row and column. Returns the matrix in the end
    """
    M = len(Mat)
    N = len(Mat[0])
    Mat[row][:] = [0 for _ in xrange(N)]
    for i in xrange(M):
        Mat[i][col] = 0

    return Mat

if __name__ == "__main__":
    zero_arr = []
    Mat = [[1,2,0], [4,5,6],[0,2,3]],
    print "Original Matrix: "
    print Mat
    M = len(Mat)
    N = len(Mat[0])
    for i in xrange(M):
        for j in xrange(N):
            if Mat[i][j] == 0:
                zero_arr.append((i,j))

    for idx in zero_arr:
        Mat = clearZeros(Mat, idx[0], idx[1])
    print "Cleared Matrix: ",
    print Mat
