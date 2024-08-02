class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades

    def average(self):
        return (sum(self.grades)/len(self.grades))
    

student1=Student("Rolf",24,(22,44,64,75,46,88,99))
student2=Student("Ron",23,(93,56,67,75,44,78,80))

print(f"Average of {student1.name}: {student1.average():.2f}")
print(f"Average of {student2.name}: {student2.average():.2f}")