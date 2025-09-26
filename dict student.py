n=int(input("how many students?"))
students = {}
for i in range(n):
    name=input(f" enter name of students{i+1}:")	
    mark=int(input(f"enter mark of {name}:"))
    students[name]=mark
    print("\nDictionary:",students)
    
                