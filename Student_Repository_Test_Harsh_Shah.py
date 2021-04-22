"""
This is to test the function written in HW09 
@author: Harsh Shah
"""
import unittest
from HW10_Harsh_Shah import Repository
from typing import Dict , List

class testFunctions(unittest.TestCase):
    def test_major_pretty_table(self) -> None:
        """testing major pretty table"""
        rep:Repository = Repository("/Users/harsh/OneDrive/Desktop/My Files/Assignment")
        expected = {
            'SFEN': ['SFEN', {'SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'} ,{'CS 501', 'CS 513', 'CS 545'}],
            'SYEN': ['SYEN', {'SYS 612', 'SYS 671', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}]
        }
        unexpected = {
            'SFEN': ['SFEN', {'SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'} ,{'CS 501', 'CS 513', 'CS 545'}],
            'SYEN': ['SYEN', {'SYS 612', 'SYS 671', 'SYS 800'}, ]
        }
        res = {m: mj.major_info() for m, mj in rep._majors.items()}
        
        self.assertEqual(expected, res)
        self.assertNotEqual(unexpected , res)
  

 
    def test_student_pretty_table(self) -> None:
        """testing student table"""
        rep: Repository = Repository("/Users/harsh/OneDrive/Desktop/My Files/Assignment")
        res = list()
        expected  = [
            ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, [], 3.44],
            ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, [], 3.81], 
            ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], {'SSW 540', 'SSW 564'}, {'CS 501', 'CS 513', 'CS 545'}, 3.88], 
            ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, {'CS 501', 'CS 513', 'CS 545'}, 3.58], 
            ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], {'SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'},{'CS 501', 'CS 513', 'CS 545'}, 4.0], 
            ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], {'SYS 612', 'SYS 671', 'SYS 800'}, [], 3.0], 
            ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], {'SYS 612', 'SYS 671'}, {'SSW 540', 'SSW 565', 'SSW 810'}, 3.92],
            ['11658', 'Kelly, P', 'SYEN', [], {'SYS 612', 'SYS 671', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}, 0], 
            ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], {'SYS 612', 'SYS 671', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}, 3.0], 
            ['11788', 'Fuller, E', 'SYEN', ['SSW 540'],{'SYS 612', 'SYS 671', 'SYS 800'}, [], 4.0]]

        unexpected  = [
            ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, [], 3.44],
            ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, [], 3.81], 
            ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], {'SSW 540', 'SSW 564'}, {'CS 501', 'CS 513', 'CS 545'}, 3.88], 
            ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, {'CS 501', 'CS 513', 'CS 545'}, 3.58], 
            ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], {'SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'},{'CS 501', 'CS 513', 'CS 545'}, 4.0], 
            ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], {'SYS 612', 'SYS 671', 'SYS 800'}, [], 3.0], 
            ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], {'SYS 612', 'SYS 671'}, {'SSW 540', 'SSW 565', 'SSW 810'}, 3.92],
            ['11658', 'Kelly, P', 'SYEN', [], {'SYS 612', 'SYS 671', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}, 0], 
            ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], {'SYS 612', 'SYS 671', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}, 3.0], 
            ]
       
        
        for  cwid , student in rep._students.items():
            res.append(student.student_info())
            
        self.assertEqual(expected, res)
        self.assertNotEqual(unexpected, res)


    def test_instructor_pretty_table(self):
        """ This function is to test the instructor pretty table output"""
        rep: Repository = Repository("/Users/harsh/OneDrive/Desktop/My Files/Assignment")
        expected:Dict = {
            ('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
            ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
            ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
            ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
            ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
            ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
            ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
            ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1),
        }
        expected1: Dict={
            ('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
            ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
            ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
            ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
            ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
            ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
            ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
            ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
            ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),

        }

        res:Dict = {tuple(x) for  instructor in rep._instructors.values() for x in instructor.instructor_info()}
        self.assertEqual( res , expected)
        self.assertNotEqual( res , expected1)



if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)