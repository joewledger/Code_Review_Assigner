def string_alignment(str1, str2, **score):
    row = len(str1) + 1
    col = len(str2) + 1
    m = score.get('match', 1)
    s = score.get('miss', -1)
    g = score.get('gap', 0)

    align_mat = create_mat(row, col)
    for i in range(1, row):
        align_mat[i][0] = align_mat[i - 1][0] + g
    for j in range(1, col):
        align_mat[0][j] = align_mat[0][j - 1] + g

    for i in range(1, row):
        for j in range(1, col):
            s1 = align_mat[i - 1][j - 1] + char_comp(str1[i - 1], str2[j - 1], m, s)
            s2 = align_mat[i - 1][j] + g
            s3 = align_mat[i][j - 1] + g

            if s1 == max(s1, s2, s3):
                align_mat[i][j] = s1
            elif s2 == max(s1, s2, s3):
                align_mat[i][j] = s2
            else:
                align_mat[i][j] = s3
    return align_mat[row - 1][col - 1]


def char_comp(c1, c2, m, s):
    if c1 == c2:
        return m
    else:
        return s


def create_mat(m, n):
    return [[0 for x in range(n)] for y in range(m)]


def path2list(file_path):
    return file_path.split("/")


def main():
    str1 = 'AG/TA/ttt'
    str2 = 'fvf/bgbb/tr/ee/TA/tat'
    score1 = string_alignment(path2list(str1), path2list(str2), match=1, miss=-1, gap=0)
    score2 = string_alignment(str1, str2, match=1, miss=-1, gap=0)
    print(score1)
    print(score2)


if __name__ == '__main__': main()
