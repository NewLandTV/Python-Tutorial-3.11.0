class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ShowInfo(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

class Student(Person):
    school = ""
    grade = 1
    ban = 1
    number = 1

    def __init__(self, name, age, school, grade, ban, number):
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade
        self.ban = ban
        self.number = number

    def ShowSchoolInfo(self):
        print(f"School : {self.school}")
        print(f"Grade : {self.grade}")
        print(f"Ban : {self.ban}")
        print(f"Number : {self.number}")

# 사람 인스턴스
person1 = Person("깁스립", 25)
person2 = Person("갈람식", 53)
person3 = Person("이다룬", 30)

# 학생 인스턴스
student1 = Student("채연사", 11, "갑스진초등학교", 4, 2, 7)
student2 = Student("김투어", 14, "아스키중학교", 2, 1, 16)
student3 = Student("김은혜", 10, "엘리펀초등학교", 3, 3, 18)

person1.ShowInfo()
person2.ShowInfo()
person3.ShowInfo()

print("Students")

student1.ShowInfo()
student1.ShowSchoolInfo()
student2.ShowInfo()
student2.ShowSchoolInfo()
student3.ShowInfo()
student3.ShowSchoolInfo()