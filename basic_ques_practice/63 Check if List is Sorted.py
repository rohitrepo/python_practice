class SortedListCheck:
    def __init__ (self, list):
        self.list = list

    def islistsorted(self):
        if self.list == sorted(self.list):
            return True
        else:
            return False

list_a = SortedListCheck([1, 2, 3, 4, 4])

print ( list_a.islistsorted() )

#can also iterate through list and check