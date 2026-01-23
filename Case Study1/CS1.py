import json
import csv
import time
from abc import ABC, abstractmethod

def log_method(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper

def admin_only(func):
    def wrapper(self, *args, **kwargs):
        if not self.is_admin:
            print("Access Denied: Admin privileges required")
            return
        return func(self, *args, **kwargs)
    return wrapper

class MarksDescriptor:
    def __get__(self, obj, objtype=None):
        return obj._marks

    def __set__(self, obj, value):
        for m in value:
            if m < 0 or m > 100:
                raise ValueError("Error: Marks should be between 0 and 100")
        obj._marks = value

class SalaryDescriptor:
    def __get__(self, obj, objtype=None):
        raise PermissionError("Access Denied: Salary is confidential")

class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"Cleaning up object {self.name}")

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def get_details(self):
        print("Student Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department}")

    @log_method
    def calculate_performance(self):
        avg = sum(m for m in self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self._salary = salary

    def get_details(self):
        print("Faculty Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Faculty")
        print(f"Department: {self.department}")

class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits

class CourseIterator:
    def __init__(self, courses):
        self.courses = list(courses)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.courses):
            raise StopIteration
        course = self.courses[self.index]
        self.index += 1
        return course

def student_generator(students):
    print("Fetching Student Records...")
    print("--------------------------------")
    for s in students.values():
        yield f"{s.pid} - {s.name}"

class University:
    def __init__(self):
        self.students = {}
        self.faculty = {}
        self.courses = {}
        self.is_admin = True

    def add_student(self):
        sid = input("Student ID: ")
        if sid in self.students:
            print("Error: Student ID already exists")
            return
        name = input("Student Name: ")
        dept = input("Department: ")
        sem = int(input("Semester: "))
        marks = list(map(int, input("Marks (5 subjects): ").split()))
        try:
            self.students[sid] = Student(sid, name, dept, sem, marks)
            print("Student Created Successfully")
        except ValueError as e:
            print(e)

    def add_faculty(self):
        fid = input("Faculty ID: ")
        name = input("Faculty Name: ")
        dept = input("Department: ")
        salary = int(input("Monthly Salary: "))
        self.faculty[fid] = Faculty(fid, name, dept, salary)
        print("Faculty Created Successfully")

    def add_course(self):
        code = input("Course Code: ")
        name = input("Course Name: ")
        credits = int(input("Credits: "))
        fid = input("Faculty ID: ")
        self.courses[code] = Course(code, name, credits, self.faculty[fid])
        print("Course Added Successfully")

    def enroll_student(self):
        sid = input("Student ID: ")
        cid = input("Course Code: ")
        self.students[sid].courses.append(self.courses[cid].name)
        print("Enrollment Successful")

    def calculate_performance(self):
        sid = input("Student ID: ")
        avg, grade = self.students[sid].calculate_performance()
        print("Average:", round(avg, 2))
        print("Grade:", grade)

    def compare_students(self):
        s1 = input("Student ID 1: ")
        s2 = input("Student ID 2: ")
        print(f"{self.students[s1].name} > {self.students[s2].name} :", self.students[s1] > self.students[s2])

    def generate_reports(self):
        with open("students_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
            for s in self.students.values():
                avg, grade = s.calculate_performance()
                writer.writerow([s.pid, s.name, s.department, round(avg, 2), grade])
        print("CSV Report Generated")

        with open("students.json", "w") as f:
            json.dump({k: vars(v) for k, v in self.students.items()}, f, indent=4)
        print("Student data successfully saved to students.json")

    def run(self):
        while True:
            print("\n1 Add Student\n2 Add Faculty\n3 Add Course\n4 Enroll Student\n5 Calculate Performance\n6 Compare Students\n7 Generate Reports\n8 Exit")
            ch = input("Enter choice: ")
            if ch == "1":
                self.add_student()
            elif ch == "2":
                self.add_faculty()
            elif ch == "3":
                self.add_course()
            elif ch == "4":
                self.enroll_student()
            elif ch == "5":
                self.calculate_performance()
            elif ch == "6":
                self.compare_students()
            elif ch == "7":
                self.generate_reports()
            elif ch == "8":
                print("Thank you for using Smart University Management System")
                break

if __name__ == "__main__":
    University().run()
