"""
Implementation of the homework 09
@author: Harsh Shah
"""


from typing import Dict , DefaultDict
from collections import defaultdict
import os
from HW08_Harsh_Shah import file_reader
from prettytable import PrettyTable

class Student:
    """Class for inserting the student data"""

    def __init__(self, cwid: int, name: str, major: str) -> None:
        """creating an instance of student after reading each line in the file"""

        self._cwid: int = cwid
        self._name: str = name
        self._major: str = major
        self._courses = defaultdict()
    
    def store_course_grade(self, course: str, grade: str):
        """add a course and grade to the container of courses and grades"""

        self._courses[course]: Dict[str, str] = grade
    
    def student_info(self):
        """return the student values"""

        return [self._cwid, self._name, sorted(self._courses.keys())]

class Instructor:
    """Class to add the instructor """

    def __init__(self, cwid: int, name: str, department: str) -> None:
        """creating new instance of instructor after reading the file"""

        self._cwid: int = cwid
        self._name: str = name
        self._department: str = department
        self._courses: DefaultDict[str, int] = defaultdict(int)
    
    def store_course_student(self, course: str):
        """increamenting the count of student for the course taken under the instructor"""

        self._courses[course] += 1

    def instructor_info(self):
        """return the  records of instructor"""
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._department, course, count]
        

             

class Repository:
    """ Store all students, instructors for a university and print pretty tables """
    def __init__(self, dir: str) -> None:
        """ store all students , instructors 
        read students.txt , grades.txt , instructors.txt
        print prettytables"""

        self._dir: str = dir
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self._read_students(os.path.join(dir, 'students.txt'))
        self._read_instructors(os.path.join(dir, 'instructors.txt'))
        self._read_grades(os.path.join(dir, 'grades.txt'))

    
    def _read_students(self, path: str):
        """reading the file and adding student to the container"""
        try:
            file = list(file_reader(path, 3, sep = '\t', header = False))
            for cwid, name, major in file :
                self._students[cwid] = Student(cwid, name, major)
        except(FileNotFoundError , ValueError) as e:
            print(e)

    def _read_instructors(self, path: str):
        """reading the file and adding instructor to the container"""
        try:
            file = list(file_reader(path, 3, sep = '\t', header = False))
            for cwid, name, department in file :
                self._instructors[cwid] = Instructor(cwid, name, department)
        except(FileNotFoundError , ValueError) as e:
            print(e)

    def _read_grades(self, path: str):
        """reading the file and adding grades to respective student"""
        try:
            file = list(file_reader(path, 4, sep = '\t', header = False))
            for student_cwid, course, grade, instructor_cwid in file:
                if student_cwid in self._students:
                    self._students[student_cwid].store_course_grade(course, grade)
                else:
                    print(f"{student_cwid} is unknown")
                    
                if instructor_cwid in self._instructors:
                    self._instructors[instructor_cwid].store_course_student(course)
                else:
                    print(f"{instructor_cwid} is unknow")
        except(FileNotFoundError , ValueError) as e:
            print(e)
            
    def student_pretty_table(self):
        """ This is the pretty table for the student info"""
        pt = PrettyTable(field_names=['CWID', 'NAME', 'COMPLETED COURSES'])

        for student in self._students.values():
            pt.add_row(student.student_info())
        print(pt)

    def instructor_pretty_table(self):
        """ This is the pretty table for the instructor"""
        pt = PrettyTable(field_names=['CWID', 'NAME', 'DEPARTMENT', 'COURSE', 'COUNT'])
        
        for instructor in self._instructors.values():
            for x in instructor.instructor_info():
                pt.add_row(x)
        print(pt)

