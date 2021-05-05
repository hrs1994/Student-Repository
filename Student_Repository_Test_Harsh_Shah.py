"""
This is to test the function written in HW11
@author: Harsh Shah
"""
import unittest
from HW11_Harsh_Shah import Repository
from typing import Dict , List

class testFunctions(unittest.TestCase):
    def test_major_pretty_table(self) -> None:
        """testing major pretty table"""
        rep:Repository = Repository(r"C:\Users\harsh\OneDrive\Desktop\My Files\Assignment")
        expected: Dict[str] = {
            'SFEN': ['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']],
            'CS': ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]
        }
       
        res = {m: mj.major_info() for m, mj in rep._majors.items()}
        
        self.assertEqual(expected, res)
        
  

 
    def test_student_pretty_table(self) -> None:
        """testing student table"""
        rep: Repository = Repository(r"C:\Users\harsh\OneDrive\Desktop\My Files\Assignment")
        res = list()
        expected:List[str]  = [
            ['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], 3.38],
            ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546'], 4.0], 
            ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546'], 4.0], 
            ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5], 
        ]

        for  cwid , student in rep._students.items():
            res.append(student.student_info())
            
        self.assertEqual(expected, res)



    def test_instructor_pretty_table(self):
        """ This function is to test the instructor pretty table output"""
        rep: Repository = Repository(r"C:\Users\harsh\OneDrive\Desktop\My Files\Assignment")
        expected:Dict[str] = {
            ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
            ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4),
            ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
            ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
            ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
            ('98762', 'Hawking, S', 'CS', 'CS 570', 1)
        }
       

        res:Dict = {tuple(x) for  instructor in rep._instructors.values() for x in instructor.instructor_info()}
        self.assertEqual( res ,expected)



    def test_instructor_table_db(self) -> None:
        """testing student grade summary pretty table"""
        rep: Repository = Repository(r"C:\Users\harsh\OneDrive\Desktop\My Files\Assignment")

        expected: List[str] = [
            ('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'),
            ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'),
            ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'),
            ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'),
            ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'),
            ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'),
            ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'),
            ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'),
            ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J')
        ]

        res = list()

        for row in rep.instructor_table_db(r'C:\Users\harsh\OneDrive\Desktop\My Files\Assignment\810_startup.db'):
            res.append(row)

        self.assertEqual(expected, res)



if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
