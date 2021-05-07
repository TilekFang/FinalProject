students = []

class Student:

    group_name = "Male"

    def __init__(self, name, student_last_name, student_id=3332):
        
        self.name = name
        self.student_id = student_id
        self.last_name = student_last_name
        students.append(self)

    def __str__(self):
        return "Student " + self.name


    def get_name_capitalize(self):
        return self.name.capitalize()


    def get_school_name(self):
        return self.university_name