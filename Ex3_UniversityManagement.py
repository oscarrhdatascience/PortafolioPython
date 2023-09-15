"""
University Management System Description:

This university management system, developed in Python, manages the registration of students and courses, oversees the academic process, and handles various functionalities like tuition payments and notifications. Each course has a set capacity, professor, and schedule. Administrative roles are also incorporated for access control and task management within the platform.

Integrated Concepts:

    Object-Oriented Programming
    Encapsulation
    Lists
    Dictionaries
    Flow Control
    Class Relationships
    Decorators
    Property Access
    Role-Based Access Control
"""
class Student:
    def __init__(self, name, student_id, tuition_fees):
        self.name = name
        self.student_id = student_id
        self.tuition_fees = tuition_fees
        self.grades = {}
        self._paid_amount = 0

    def pay_tuition(self, amount):
        self._paid_amount += amount
        self.send_notification(f"Payment received: {amount}")

    def send_notification(self, message):
        print(f"Notification for {self.name}: {message}")

    @property
    def paid_amount(self):
        return self._paid_amount


class Course:
    def __init__(self, course_id, course_name, max_students, professor, schedule, fee):
        self.course_id = course_id
        self.course_name = course_name
        self.max_students = max_students
        self.enrolled_students = []
        self.professor = professor
        self.schedule = schedule
        self.fee = fee

    def enroll_student(self, student):
        if len(self.enrolled_students) < self.max_students:
            self.enrolled_students.append(student)
            return True
        return False


class University:
    def __init__(self):
        self.students = []
        self.courses = []
        self._admin_roles = {}

    def register_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def add_course(self, course):
        self.courses.append(course)

    def find_course(self, course_id):
        for c in self.courses:
            if c.course_id == course_id:
                return c
        return None

    def assign_admin_role(self, admin_id, role):
        self._admin_roles[admin_id] = role

    @property
    def admin_roles(self):
        return self._admin_roles


if __name__ == "__main__":
    # Test the system here
    pass
