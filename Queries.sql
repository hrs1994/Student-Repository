
----------------- 4.1---------------------------------------------------------
select Name from students where CWID = '10115';

--------------------4.2-------------------------------------------------------

select Major, count(*) from students  group by Major;

-------------------4.3--------------------------------------------------------
select Grade, count(Grade) as grade_count from grades where Course='SSW 810' group by Grade limit 1;

---------------------4.4------------------------------------------------------------------
select CWID , Name , count(Course) as Total_Course from students  join grades  on students.CWID = grades.StudentCWID group by CWID, Name

--------------------4.5----------------------------------------------------------

select students.Name , students.CWID , grades.Course , grades.Grade, instructors.Name from students join grades on students.CWID = grades.StudentCWID join instructors on grades.InstructorCWID = instructors.CWID order by students.Name asc ;

