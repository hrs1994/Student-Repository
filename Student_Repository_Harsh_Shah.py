"""
This is to test the function written in HW09 
@author: Harsh Shah
"""
import unittest
from HW09_Harsh_Shah import Repository
from typing import Dict , List


class testFunctions(unittest.TestCase):
    """ To implement different test cases"""
    def test_student_pretty_table(self):
        """This function is to test the student pretty table output"""
        rep: Repository = Repository("/Users/harsh/OneDrive/Desktop/My Files/Assignment")
        expected:Dict = {'10103': ['10103','Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567' ,'SSW 687']],
                    '10115': ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                    '10172': ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
                    '10175': ['10175', 'Erickson, D', [ 'SSW 564', 'SSW 567', 'SSW 687']],
                    '10183': ['10183', 'Chapman, O', ['SSW 689']],
                    '11399': ['11399', 'Cordova, I', ['SSW 540']],
                    '11461': ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']],
                    '11658': ['11658', 'Kelly, P', ['SSW 540']],
                    '11714': ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
                    '11788': ['11788', 'Fuller, E', ['SSW 540']]}

        expected1:Dict = {
                    '10103': ['10103','Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567' ,'SSW 687']],
                    '10115': ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                    '10172': ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
                    '10175': ['10175', 'Erickson, D', [ 'SSW 564', 'SSW 567', 'SSW 687']],
                    '10183': ['10183', 'Chapman, O', ['SSW 689']],
                    '11399': ['11399', 'Cordova, I', ['SSW 540']],
                    '11461': ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']],
                    '11658': ['11658', 'Kelly, P', ['SSW 540']],
                    '11714': ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
                    }
        res:Dict = {cwid: student.student_info() for cwid , student in rep._students.items()}
        self.assertEqual(res, expected)
        self.assertNotEqual(res , expected1)
        
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

