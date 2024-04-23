class SearchIndex:
    def __init__ (self, list_2d, target):
        self.list_2d = list_2d
        self.target = target

    def index_search(self):
        self.index_value = []                               #intiiate it before for loop
        for i in range(len(self.list_2d)):
            for j in range (len(self.list_2d[i])):
                if self.list_2d [i][j] == self.target:
                    self.index_value.append((i, j))         #did mistake here. need toa ppend properly
                else:
                    return (-1, -1)
        return self.index_value

list_a = SearchIndex([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 91)

print( list_a.index_search() )