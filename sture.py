class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        total=sum(self.marks)
        avg=total/len(self.marks)
        print(f"Results:{total}{avg}")
students =[]
for i in range(5):
    print("Enter the details of students{i+1}:")
    name= input("Enter the name:")
    marks=[]
    for j in range(3):
        marks = int(input(f"Enter the marks"))
        marks.append(marks)
    student= student(name,marks)
    students.append(student)
print("\n student report:")
for student in students:
    student.display()