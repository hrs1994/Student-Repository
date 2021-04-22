"""
@author:- Harsh Shah
This is the implementation of the homework 08
"""
import os
from os import path
from datetime import datetime, timedelta
from typing import Tuple , Iterator, IO , List
from prettytable import PrettyTable

def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ function to return the tuple with three values of datetime """
    three_days_after_02272020: datetime = (datetime.strptime("Feb 27, 2020" , "%b %d, %Y") + timedelta(days= 3)).strftime("%b %d, %Y")
    three_days_after_02272019: datetime = (datetime.strptime("Feb 27, 2019", "%b %d, %Y") + timedelta(days=3)).strftime("%b %d, %Y")
    days_passed_02012019_09302019: int = (datetime.strptime("Sep 30, 2019" , "%b %d, %Y") - datetime.strptime("Feb 1, 2019" ,"%b %d, %Y")).days

    return three_days_after_02272020, three_days_after_02272019,abs(days_passed_02012019_09302019)




def file_reader(path, fields, sep, header=False) -> Iterator[Tuple[str]]:
    """ function to return the tuple separated with separator , if any value error comes it should display the error on the line and expected value"""
    try:
        fp:IO = open(path , 'r')
    except FileNotFoundError:
        raise FileNotFoundError("path not found")
    else:
        with fp:
            if header:
                next(fp)
            lines = fp.readlines()
            for x in range(len(lines)):
                line = lines[x].rstrip('\n').split(sep)
                if fields is not len(line) and header is True:
                    raise ValueError(f" {path} has {len(line)} in line {x+2} but expected {fields} ")
                elif fields is not len(line) and header is False:
                    raise ValueError(f" {path} has {len(line)} in line {x+1} but expected {fields} ")
                else:
                    yield tuple(line)




from typing import Dict
class FileAnalyzer:
    """ Classs to scan the directories and file"""
    def __init__(self, directory: str) -> None:
        """ Constructor to intialize directory and file summary"""
        self.directory: str = directory # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict() 
        self.analyze_files() # summerize the python files data

    def analyze_files(self) -> None:
        """ This function return the count of character , line , class and function of the each file in directory"""
        dir : str = os.path.isdir(self.directory)
        if not dir:
            raise FileNotFoundError("Directory doesnt exist")
        files:List[str] = os.listdir(self.directory)
        if not files:
            raise FileNotFoundError("Directory is empty")
        for file in files:
            if file.endswith(".py"):
                    fp:IO = open(os.path.join(self.directory,file), 'r' )
                    with fp:
                        lines = fp.readlines()
                        no_char : int =0
                        no_func: int =0
                        no_line: int =0
                        no_class: int =0
                        for line in lines:
                            if line.strip().startswith('def '):
                                no_func +=1 
                            if line.startswith('class '):
                                no_class +=1 
                            no_char += len(line)
                            no_line +=1
                    self.files_summary[file] ={
                        'class': no_class,
                        'functions' : no_func,
                        'line': no_line,
                        'Characters': no_char
                        }
        



    def pretty_print(self) -> None:
        """ This function return the pretty table with the details which is passed in file summary"""
        pt:PrettyTable = PrettyTable(field_names=['File Name' , 'Classes' , 'functions' , 'lines' , 'characters'])
        for file_name , stats in self.files_summary.items():
            pt.add_row([file_name , stats['class'] , stats['functions'] , stats['line'] , stats['Characters'] ])
        print(pt)

