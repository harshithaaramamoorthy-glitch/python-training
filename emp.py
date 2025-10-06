class Employee:
    def __init__(self,name,hour_rate,hour_work):
        self.name=name
        self.hour_rate=hour_rate
        self.hour_work=hour_work
    def calc_salary(self):
        return self.hour_rate* self.hour_work
employees=[
      Employee("ram",500,40),
      Employee("kumar",400,50),
      Employee("shithaa",450,30)
      ]
for emp in  employees:
    salary = emp.calc_salary()
    print(f"{emp.name}'s salary is ${salary}")