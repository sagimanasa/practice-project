def matrix(matrix1,matrix2):
    result=[]
    for i in range(len(matrix1)):
        print(i)
        tmp=[]
        for j in range(len(matrix2[0])):
            print(j)
            tmp_val=0
            print(tmp_val)
            for k in range(len(matrix2)):
                print(k)
                tmp_val=tmp_val+matrix1[i][k]*matrix2[k][j]
                print(tmp_val)
            tmp.append(tmp_val)
        result.append(tmp)
    return result
matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[3,2,1],[6,5,4],[9,8,7]]
result=matrix(matrix1,matrix2)
print(result)