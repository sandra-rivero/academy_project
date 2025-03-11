Dance Academy Project
This project is a management system for a dance academy. It facilitates the administration of courses, teachers, and students, allowing efficient management and scheduling of activities.

Features
Course Management: Create, update, and delete courses.
Teacher Registration: Add and manage teacher profiles.
Student Enrollment: Register students and manage their course enrollments.



Usage Examples

#Test to add a dance style to our academy and show them

academy = Academy("Victorys")

academy.add_dance_style("Pasos libres")

academy.add_dance_style("bachata")

academy.add_dance_style("salsa")

academy.add_dance_style("sevillanas")

print(academy.dance_styles)

#Test to change the name of the academy and show them

academy.change_name("Infinit")

print(academy.name)

#Test to add a course and show them

academy.add_course("Bachata inicio 1")

academy.add_course("Bachata medio 1")

academy.add_course("Bachata medio 2")

print(academy.courses)

#Test to add a student, and show them

academy.add_student("Pepe")

academy.add_student("Maria")

academy.add_student("Noelia")

academy.add_student("Luis")

print(academy.students)
