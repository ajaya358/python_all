class Student:
    school = "Python Learning School"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__marks = 0

    def study(self):
        return f"{self.name} is studying."

    def get_marks(self):
        return self.__marks

    def update_marks(self, marks):
        self.__marks = marks

    @classmethod
    def school_name(cls):
        return cls.school

    @staticmethod
    def welcome_message():
        return "Welcome to Python OOP!"


class CollegeStudent(Student):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        return f"{self.name} is studying {self.course}."


def show_polymorphism(students):
    for student in students:
        print(student.study())


if __name__ == "__main__":
    s1 = Student("Ajay", 21)
    s2 = CollegeStudent("Ravi", 19, "AI")

    print(s1.study())
    s1.update_marks(90)
    print("Marks:", s1.get_marks())
    print(Student.school_name())
    print(Student.welcome_message())
    print(s2.study())

    show_polymorphism([s1, s2])
