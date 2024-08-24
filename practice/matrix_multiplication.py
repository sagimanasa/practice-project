def matrix(matrix1,matrix2):
    output=[]
    for i in range(len(matrix1)):
        temp=[]
        for j in range(len(matrix2[0])):
            temp_value=0
            for k in range(len(matrix2)):
                temp_value=temp_value+matrix1[i][k]*matrix2[k][j]
            temp.append(temp_value)
        output.append(temp)
    return output
matrix1=[1,2,3],[3,4,5],[5,6,7]
matrix2=[7,8,9],[9,0,1],[1,2,3]
print(matrix(matrix1,matrix2))
