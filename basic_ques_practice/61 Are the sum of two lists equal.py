class SumOfList:
    def __init__ (self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def are_sums_equal(self):
        if self.list1 == [] or self.list2 == []: #can also use to check empty list - 'not self.list1'
            return False
        
        if sum(self.list1) == sum(self.list2):
            return True
        else:
            return False


a = SumOfList([], [])

print ( a.are_sums_equal() )