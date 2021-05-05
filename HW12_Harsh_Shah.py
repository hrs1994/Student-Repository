"""
This is the implementation of HW12
"""

from flask import Flask , render_template
import sqlite3
from typing import List

app = Flask(__name__)


@app.route('/students')

def student_grade_summary():
    """ This is the function to print student grade summary"""
    db_path = r"C:\Users\harsh\OneDrive\Desktop\My Files\Assignment\HW12_Harsh_Shah\810_startup.db"
    try: 
        db:sqlite3 = sqlite3.connect(db_path)
    except Exception as e:
        return render_template('error.html' , error_msg = e)
    else:
        query:str = "select students.Name , students.CWID , grades.Course , grades.Grade, instructors.Name from students join grades on students.CWID = grades.StudentCWID join instructors on grades.InstructorCWID = instructors.CWID order by students.Name asc"
        try:
            result:sqlite3 = db.execute(query)
        except Exception as e:
            return render_template('error.html' , error_msg = e)
        else:
            res:List[str] = []
            for row in result:
                res.append({'Student': row[0] , 'CWID': row[1] , 'Course': row[2] , 'Grade': row[3] , 'Instructor': row[4]})
            db.close()
            return render_template('student.html' , header="Stevens Repository" , table ='Student , Course , Grade , and Instructor' , output = res)   

if __name__ == "__main__":
  app.run(debug = True)

