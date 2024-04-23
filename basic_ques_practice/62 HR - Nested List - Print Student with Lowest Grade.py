
class SchoolMarks:
    def __init__  (self, student_marks):
        self.student_marks = student_marks

    def marks_compare(self):
        lowest_marks = 0

        for i in range(len(self.student_marks)-1):
            if self.student_marks[i][1] > self.student_marks[i+1][1]:
                lowest_marks = self.student_marks[i+1][1]
            else:
                lowest_marks = self.student_marks[i][1]

        list_of_lowest_marks = []

        for i in range( len(self.student_marks) ):
            if self.student_marks[i][1] == lowest_marks:
                list_of_lowest_marks += self.student_marks[i]
                return list_of_lowest_marks


subject1 = SchoolMarks( [ ['Rohit', 98], ['Rajat', 93], ['Rohan', 43], ['Abhishek', 40], ['Ash', 40] ] )

print(subject1.marks_compare())

## can use min() function as well to calculate lowest marks
## not able to print if more than 2 students have lowest marks then their name is not printed