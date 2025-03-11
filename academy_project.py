import datetime

class Academy:
    DANCE_STYLES = ["salsa","bachata","sevillanas","ballet","hip-hop", "kizomba","Pasos libres"]

    def __init__(self, name: str, dance_styles: list = None):
        self.name = name
        self.teachers = []
        self.students = []
        self.dance_styles = dance_styles or []
        self.courses = []
        self.prohibited_dances = ["kizomba"]
        self.workshops = []

    def __repr__(self):
        return (f"Academy [{self.name}]: dance_styles={self.dance_styles}")
    
    def add_dance_style(self, dance_style):
        #Before adding a dance style, we verify that it is a correct style, then we check whether it has already been added or not
        if dance_style not in self.DANCE_STYLES:
            raise ValueError("Must be dance style")
        if not dance_style in self.dance_styles:
            self.dance_styles.append(dance_style)
        else:
            raise ValueError(f"{dance_style} already exist")    

    def show_dance_styles(self):
        return self.dance_styles

    def change_name(self, new_name):
        self.name = new_name

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            raise ValueError(f"{course} already exist")    

    def show_courses(self):
        return self.courses
    
    def add_workshop(self,new_workshop):
        if new_workshop not in self.workshops:
            self.workshops.append(new_workshop)
            print("Workshop added.")
        else:
            raise ValueError(f"{new_workshop} already exists.")  

    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
            return True
        else:
            raise ValueError(f"{student} already exist")     
        

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
            raise ValueError(f"The dance style {style} is already added.")

    def show_dance_styles(self):
        return self.dance_styles              

class Student:
    def __init__(self, name, age, courses, email, phone):
         self.name = name
         self.age = age
         self.courses = []
         self.email = email
         self.phone = phone

    def __str__ (self):
        return f"{self.name}"     

    def change_name(self, new_name):
        self.name = new_name

    def enroll_in_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            raise ValueError(f"{self.name} is already enrolled in {course}.")

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            raise ValueError(f"{self.name} is not enrolled in {course}.")  
        
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

    def add_student(self, new_student):
        if len(self.students) < self.max_students:
            self.students.append(new_student)
        else:
            raise ValueError("Class is full, you cannot add more students")  
   
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
            raise ValueError("Class is full, you cannot add more students")

    def show_students(self):
        return self.students           
    
 