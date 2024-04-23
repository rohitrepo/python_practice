class SumList:
    def __init__ (self, list_2d):
        self.list_2d = list_2d
    
    def sum_of_rows(self):
        self.row_sum = []
        
        for i in range ( len (self.list_2d) ):
            #for j in range ( len (self.list_2d[i]) ):
            #self.row_sum = self.row_sum.append(sum(self.list_2d[i]))
            self.row_sum.append(sum(self.list_2d[i]))
        return self.row_sum

list_a = SumList([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print( list_a.sum_of_rows() )