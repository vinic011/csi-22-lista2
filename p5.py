import numpy as np

def dot_prod(list1,list2):
    dot_prod = 0
    for l1,l2 in zip(list1,list2):
        dot_prod += l1*l2
    return dot_prod

def mutiply_matrices(matrix1,matrix2):
    size = len(matrix1)
    prod = []
    transposed_matrix2 = np.array(matrix2).T.tolist()
    for i in range(size):
        line = []
        for j in range(size):
            line.append(dot_prod(matrix1[i],transposed_matrix2[j]))
        prod.append(line)
    return prod


print(mutiply_matrices([[1,1],[4,1]],[[2,5],[0,3]]))