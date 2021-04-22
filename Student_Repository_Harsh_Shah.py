"""
Implementation of the homework 10
@author: Harsh Shah
"""


from typing import Dict , DefaultDict , List , Tuple
from collections import defaultdict
import os
from HW08_Harsh_Shah import file_reader
from prettytable import PrettyTable

class Student:
    """Class for inserting the student data"""

    def __init__(self, cwid: int, name: str, major: str , major_inst) -> None:
        """creating an instance of student after reading each line in the file"""

        self._cwid: int = cwid
        self._name: str = name
        self._major: str = major
        self._major_inst: str = major_inst
        self._courses: Dict[str , str] = dict() 
        
        
    
    def store_course_grade(self, course: str, grade: str):
        """add a course and grade to the container of courses and grades"""

        self._courses[course]: Dict[str, str] = grade
    
    
    def student_info(self):
        """return the student values"""
        cousrse_completed ,remaining_required , remaining_electives ,GPA = self._major_inst.calculate_course(self._courses)
        return [self._cwid, self._name, self._major, sorted(cousrse_completed),remaining_required ,remaining_electives, GPA]

class Instructor:
    """Class to add the instructor """

    def __init__(self, cwid: int, name: str, department: str) -> None:
        """creating new instance of instructor after reading the file"""

        self._cwid: int = cwid
        self._name: str = name
        self._department: str = department
        self._courses: DefaultDict[str, int] = defaultdict(int)
    
    def store_course_student(self, course: str)->None:
        """increamenting the count of student for the course taken under the instructor"""

        self._courses[course] += 1

    def instructor_info(self):
        """return the  records of instructor"""
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._department, course, count]
        
class Major:
    """ This is the major class for the major which will conatin the two function add_course and calculate_course"""

    def __init__(self , major: str)->None:
        """ Creating the instances of major after reading the major file """
        self._major = major
        self._required = set ()
        self._electives = set ()

    def add_course(self , opt: str , course: str)->None:
        """This function will add the course under the right conatiner"""
        if opt.upper() == 'R':
            self._required.add(course)
        elif opt.upper() == 'E':
            self._electives.add(course)
        else:
            print(f'this is not expected {opt}')

    def calculate_course(self ,courses)->tuple:
        """ This will calculate the GPA , generate the list of remaining  , completed ourse , remaining electives, remaining required"""
        passing: List[str] = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']
        passing_gpa:Dict[str ,float] = {'A': 4.0, 'A-':3.75 , 'B+':3.25, 'B':3.0, 'B-':2.75, 'C+':2.25, 'C': 2.0 , 'C-':0 , 'D+':0 , 'D': 0 , 'D-' : 0 , 'F': 0}
        cousrse_completed = set()
        GPA:float = 0.0
        gpa:float = 0.0
        
        for course , grade in courses.items():
            if grade in passing:
                cousrse_completed.add(course)
        
        remaining_required = self._required - cousrse_completed
        if cousrse_completed.intersection(self._electives):
            remaining_electives = []
        else :
            remaining_electives = self._electives
        for grade in courses.values():
            for g , p in passing_gpa.items():
                if grade == g:
                    gpa += p
            if len(cousrse_completed)== 0:
                print(f"student has failed")
            else:
                GPA: float = round(gpa /len(cousrse_completed) , 2) 
        return cousrse_completed ,remaining_required , remaining_electives ,GPA

    def major_info(self):
        """This will help in populatinhg the pretty table for major"""
        return [self._major , self._required, self._electives]
             

class Repository:
    """ Store all students, instructors for a university and print pretty tables """
    def __init__(self, dir: str) -> None:
        """ store all students , instructors 
        read students.txt , grades.txt , instructors.txt
        print prettytables"""

        self._dir: str = dir
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self._majors = dict()
        self._read_majors(os.path.join(dir, 'majors.txt'))
        self._read_students(os.path.join(dir, 'students.txt'))
        self._read_instructors(os.path.join(dir, 'instructors.txt'))
        self._read_grades(os.path.join(dir, 'grades.txt'))
        
        print('\n Major Summary')
        self.major_pretty_table()
        print('\n Student Summary')
        self.student_pretty_table()
        print('\n Instructor Summmary')
        self.instructor_pretty_table()
        
    def _read_majors(self , path: str)->None:
        """ reading the major from the file"""
        try:
            file =list(file_reader(path, 3, sep = '\t', header = True))
            for major , req_course , course in file:
                if major not in self._majors:
                    self._majors[major] = Major(major)
                self._majors[major].add_course(req_course , course)
        except(FileNotFoundError , ValueError) as e:
            print(e)

    
    def _read_students(self, path: str)->None:
        """reading the file and adding student to the container"""
        try:
            file = list(file_reader(path, 3, sep = ';', header = True))
            for cwid, name, major in file :
                if major  not in self._majors:
                        
                        print(f"student {cwid} {name} has unknow {major} ")
                else:    
                        self._students[cwid] = Student(cwid, name , major ,self._majors[major])
                
        except(FileNotFoundError , ValueError) as e:
            print(e)

    def _read_instructors(self, path: str)->None:
        """reading the file and adding instructor to the container"""
        try:
            file = list(file_reader(path, 3, sep = '|', header = True))
            for cwid, name, department in file :
                self._instructors[cwid] = Instructor(cwid, name, department)
        except(FileNotFoundError , ValueError) as e:
            print(e)



    def _read_grades(self, path: str)-> None:
        """reading the file and adding grades to respective student"""
        try:
            file = list(file_reader(path, 4, sep = '|', header = True))
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
        pt = PrettyTable(field_names=['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives' ,'GPA'])

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

    def major_pretty_table(self):
        """ pretty table for majors """
        pt = PrettyTable(field_names=['Major' , 'Required Courses' , 'Electives'])
        for major in self._majors.values():
            pt.add_row(major.major_info())
        print(pt)



