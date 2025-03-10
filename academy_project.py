class Academy:
    DANCE_STYLES = ["salsa","bachata","sevillanas","ballet","hip-hop", "kizomba", "sardana"]

    def __init__(self, name: str, dance_style: list = None):
        self.name = name
        self.teachers = []
        self.students = []
        self.dance_styles = dance_style or []
        self.courses = []
        self.prohibited_dances = ["kizomba"]
        self.workshops = []

    def __repr__(self):
        return (f"Academy [{self.name}]: dance_styles={self.dance_styles}")
    
    def add_dance_style(self, dance_style):
        if dance_style not in self.DANCE_STYLES:
            raise ValueError("tienen que ser bailes")
        if not dance_style in self.dance_style:
            self.estilos_de_baile.append(dance_style)

    def show_dance_styles(self):
        return self.dance_style  

    def change_name(self, new_name):
        self.name = new_name

    def add_course(self, course):
        self.courses.append(course)

    def show_courses(self):
        return self.courses
    
    def add_workshop(self,new_workshop):
        if new_workshop not in self.workshops:
            self.workshops.append(new_workshop)
            print("Workshop added.")
        else:
            print(f"{new_workshop} already exists.")    
        

class DanceStyle:
    dance_styles = ["salsa","bachata","sevillanas","ballet","hip-hop"]

    def __init__(self, style):
        self.style = style

    def __str__(self):
        return self.style

    def add_dance_style(self,style):
        if style not in self.DANCE_STYLES:
            self.dance_style.append(style)
        else:
            print(f"The dance style {style} is already added.")

    def show_dance_styles(self):
        print(self.DANCE_STYLES)              

class Student:
    def __init__(self, name, age, course, email, phone):
         self.name = name
         self.age = age
         self.course = []
         self.email = email
         self.phone = phone

    def __str__ (self):
        return f"{self.name}, {self.age}"     

    def change_name(self, new_name):
        self.name = new_name

    def enroll_in_course(self, course):
        if course not in self.course:
            self.course.append(course)
        else:
            print(f"{self.name} is already enrolled in {course}.")

    def drop_course(self, course):
        if course in self.course:
            self.course.remove(course)
        else:
            print(f"{self.name} is not enrolled in {course}.")  
        
class Teacher:
    def __init__(self,name,specialty,age, email, phone,courses:list=None):
        self.name = name
        self.age = age
        self.courses = courses or []
        self.email = email
        self.phone = phone
        self.specialty = specialty

    def __str__(self):
        return f"{self.name}, {self.specialty}"  

class Course:
    def __init__(self, dance_style, teachers, students = None, max_students = 10):
        self.dance_style = dance_style
        self.teachers = teachers or []
        self.students = students or []
        self.max_students = max_students

    def __str__(self):
        return f"{self.dance_style}, {self.teacher}"  

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            print("Class is full, you cannot add more students")  
   
    def show_students(self):
        return self.students
    
class Workshop:
    def __init__(self, teachers:list, dance_style, date_hour, cost,students:list, max_students = 20):
        self.teachers = teachers or []
        self.dance_style = dance_style
        self.date_hour = date_hour
        self.cost = cost
        self.students = students or []
        self.max_students = max_students
       
    def __repr__(self):
        return f"{self.dance_style}, {self.teachers}"
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            print("Class is full, you cannot add more students")  

    def show_students(self):
        return self.students           
    
 
