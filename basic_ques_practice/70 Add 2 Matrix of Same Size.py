class AddMatrix:
    def __init__ (self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def matrix_addition(self):
        
        #need to underrstand the concept about following line of code about initialization of sum matrix
        self.sum_matrix =  [[0 for _ in range(len(self.matrix_a[0]))] for _ in range(len(self.matrix_a))]

        if  ( len(self.matrix_a) != len(self.matrix_b) ) and (len(self.matrix_a[i])!= len(self.matrix_b[i]) ):
            return "Matrix Size is not equal."     ##validate this scenario
        else:
            for i in range (len(self.matrix_a)):
                for j in range (len(self.matrix_a[i])):
                    self.sum_matrix[i][j] = self.matrix_a[i][j] + self.matrix_b[i][j]
            return self.sum_matrix

problem1 = AddMatrix([[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]] )

print(problem1.matrix_addition() )