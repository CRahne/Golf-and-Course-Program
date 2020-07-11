from datetime import date
import numpy as np
import AddGolfCourse as gc
from tabulate import tabulate
from csv import writer

#def add9HoleScore():

def add18HoleScore():
    year = input("YEAR FOUR DIG NUM: ")
    month = input("MONTH TWO DIG NUM: ")
    day = input("DAY TWO DIG NUM: ")
    date = DateFormat(year, month, day)
    
    course = FindCourse()
    score = input("SCORE: ")
    with open('Scores.csv','a+',newline='') as file:
        csv_writer = writer(file)
        print(tabulate([date, course[0], score], headers=["Date","Course Code", "Score"]))
        choice = input("Good = Y, Bad = N: ")
        if choice.upper() == "Y":
            csv_writer.write([date, course[0], score])
    

def FindCourse():
    while True:
        print("1. Search By Name")
        print("2. Search By Location")
        print("3. Search By Code")
        print("4. Print All Courses")
        choice = int(input("> "))
        
        if choice == 1:
            name = input("Name: ")
            results = gc.SearchCoursesByName(name)
            PrintCourseQueryResults(results)
        if choice == 2:
            city = input("City: ")
            state = input("State (abbv.): ")
            results = gc.SearchCoursesByLocation(city, state)
            PrintCourseQueryResults(results)
        if choice == 3:
            code = input("Code: ")
            result = gc.GetCourseWithCode(code)
            if isThisMyCourse(result):
                return result
        if choice == 4:
            counter = 1
            PrintCourseQueryResults(gc.GetAllCourses())
            input("\n >")
    

def PrintCourseQueryResults(results, will_input=True):
    print("\n",tabulate(results, headers=["Code", "Name", "Location", "Par", "Slope", "Rating"]))
    if will_input:
        input("> ")

def isThisMyCourse(FoundCourse):
    PrintCourseQueryResults([FoundCourse], will_input=False)
    print('')
    print("Y = This is the course")
    print("N = Continue My Search")
    choice = input("> ")
    if choice.upper() == "Y":
        return True
    else:
        return False
    
def DateFormat(year, month, day):
    return {str(year)}- + str(month) + "-" + str(day)

add18HoleScore()