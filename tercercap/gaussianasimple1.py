import math

def trunc(num, ndec):
    num = num * 10 ** ndec
    num = int(num)
    return num / 10 ** ndec

def truncMat(matrix, dec):
    le = len(matrix)
    for i in range(0, le):
        for j in range(0, le+1):
            matrix[i][j] = trunc(matrix[i][j], dec)
    return matrix

def gaussiana(matrix, red):
    tam = len(matrix)
    matrix = truncMat(matrix, red)
    for k in range(0, tam-1):
        print("matrix "+str(matrix))
        for i in range(k+1, tam):
            mult = trunc(matrix[i][k] / matrix[k][k], red)
            print("mult "+str(mult))
            for j in range(k, tam+1): 
                matrix[i][j] = trunc(matrix[i][j], red) - trunc( (mult * trunc(matrix[k][j], red)) , red)
                matrix[i][j] = trunc(matrix[i][j], red)
    print("matrix "+str(matrix))

def equix(matrix):
    le = len(matrix)
    x = [0]*3
    for i in reversed(range(0, le)):
        suma = 0
        for j in range(i+1, le):
            suma = suma + matrix[i][j] * x[j]
        x[i] = (matrix[i][le] - suma) /matrix[i][i]
    print(x)            

def main():
    matrix = [[1,1/2,1/3,1],
              [1/2,1/3,1/4,0],
              [1/3,1/4,1/5,0]]
    """matrix = [[34,-5,6,12,37],
              [-9,43,21,8,123],
              [-12,4,75,22,16],
              [7,5,13,65,9]]"""
    gaussiana(matrix, 2)
    #equix(matrix)

main()
