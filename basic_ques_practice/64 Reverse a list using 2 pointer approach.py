class ListReversal:
    def __init__(self, org_list):
        self.org_list = org_list
    
    def reverse_list (self):
        
        if self.org_list == []:
            return False

        self.new_list = [None] * len(self.org_list) #important to initialize the new list with same no. of elements

        for i in range (0, len(self.org_list) ):
            self.new_list [ len(self.org_list) - i - 1  ] = self.org_list[i]
        return self.new_list

list_a = ListReversal([1,2,3,4,5, 's', 5, 'd'])

print (list_a.reverse_list())
