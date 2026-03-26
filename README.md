Object-Oriented Python Practice
---
This is a practice assignment for Coding Temple with the following codes and functions:

Part 1: Class Definition

1. Create a class called Student with the following attributes:

    * name (string)

    * email (string)

    * grades (list of integers)

2. Add the following methods:

    * add_grade(self, grade): Adds a grade to the grades list.

    * average_grade(self): Returns the average of all grades.

    * display_info(self): Prints the student’s name, email, and grades.

Part 2: Working with Objects

1. Create 3 student objects with different names, emails, and initial grades.

2. Add 2 new grades to each student using the add_grade method.

3. Print the information and average grade for each student using display_info.

Part 3: Dictionary & Set Integration

1. Create a dictionary called student_dict that maps each student’s email to their corresponding Student object.

2. Write a function get_student_by_email(email) that retrieves a student object from the dictionary safely using .get().

3. Create a set of all unique grades across all students and print it.

Part 4: Tuple Practice

1. Add a method to the Student class called grades_tuple(self) that returns the grades as a tuple.

2. Demonstrate that tuples are immutable by trying to change a value (catch the exception with try/except and print a message).

Part 5: List Operations

1. Remove the last grade from each student’s grades list using .pop().

2. Access and print the first and last grade for each student.

3. Print the number of grades each student has using len().

(Note: Notes are provided within the code to explain each part)
