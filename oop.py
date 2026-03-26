#create a class Student with the following attributes: name(string), email(string), grades(list of integers)
class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

#add methods add_grade(self, grade), average_grade(self), and display_info(self)
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")

    def grades_tuple(self):
        return tuple(self.grades)

#create 3 student objects with different names, emails, and grades
student1 = Student("Alice", "alice@example.com", [85, 90, 78])
student2 = Student("Bob", "bob@example.com", [92, 88, 79])
student3 = Student("Charlie", "charlie@example.com", [75, 80, 85])

#add 2 new grades to each student using add_grade method
student1.add_grade(95)
student1.add_grade(88)
student2.add_grade(91)
student2.add_grade(87)
student3.add_grade(82)
student3.add_grade(90)

#display the information and average grade for each studnet using display_info and average_grade methods
student1.display_info()
print(f"Average Grade: {student1.average_grade()}\n")
student2.display_info()
print(f"Average Grade: {student2.average_grade()}\n")
student3.display_info()
print(f"Average Grade: {student3.average_grade()}\n")

#create a dictionary called students_dict that maps each student's email to their corresponding student object
students_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}   

#write a function get_student_by_email(email) that retreives a student object from the dictionary safely using .get() method
def get_student_by_email(email):
    return students_dict.get(email, None)

#create a set of all unique grades acrsss all students and print it
unique_grades = set()
for student in students_dict.values():
    unique_grades.update(student.grades)
print(f"Unique Grades: {unique_grades}")

#Demonstrate that tuples are immutable by trying to change a value (catch the exception with/try/except and print a message)
try:
    student1.grades_tuple()[0] = 100
except TypeError as e:
    print(f"Cannot modify grades tuple: {e}")

#Remove the last grade from each student's grades list using .pop()
for student in students_dict.values():
    if student.grades:
        student.grades.pop()

#Access and print the first and last grade of each student
for student in students_dict.values():
    if student.grades:
        print(f"{student.name}'s first grade: {student.grades[0]}")
        print(f"{student.name}'s last grade: {student.grades[-1]}")

#Print the number of grades each student has uing len()
for student in students_dict.values():
    print(f"{student.name} has {len(student.grades)} grades.")
    