from datetime import date
import AddGolfCourse as gc

#def add9HoleScore():

def add18HoleScore():
    #year = input("YEAR FOUR DIG NUM: ")
    #month = input("MONTH TWO DIG NUM: ")
    #day = input("DAY TWO DIG NUM: ")
    #date = DateFormat(year, month, day)
    FindCourse()
    

def FindCourse():
    FoundCourse = False
    Course = []
    while not FoundCourse:
        print("1. Search By Name")
        print("2. Search By Location")
        print("3. Search By Code")
        print("4. Print All Courses")
        choice = int(input("> "))
        
        if choice == 1:
            name = input("Name: ")
            results = gc.SearchCoursesByName(name)
            if results == []:
                print("No Results \n")
                continue
            if isThisMyCourse(results):
                Course = results
                FoundCourse = True
                continue
            else:
                continue
        if choice == 2:
            city = input("City: ")
            state = input("State (abbv.): ")
            results = gc.SearchCoursesByLocation(city, state)
            if results[0] == []:
                print("No Results \n")
                continue
            if isThisMyCourse(results[0]):
                Course = results
                FoundCourse = True
                continue
            else:
                continue
        if choice == 3:
            code = input("Code: ")
            results = gc.GetCourseWithCode(code)
            if results == []:
                print("No Results \n")
                continue
            if isThisMyCourse(results):
                Course = results
                FoundCourse = True
                continue
            else:
                continue
        if choice == 4:
            counter = 1
            for course in gc.GetAllCourses():
                print(f"{counter}. ", end="")
                PrintCourse(course)
                counter += 1
            input("\n > ")
            print("")
        
            

def isThisMyCourse(FoundCourse):
    PrintCourse(FoundCourse)
    print("Y = This is the course")
    print("N = Continue My Search")
    choice = input("> ")
    if choice.upper() == "Y":
        return True
    else:
        return False

def PrintCourse(course):
    city = []
    state = []
    isCity = True
    for char in course[2]:
        if char != "+" and isCity:
            city.append(char)
        elif char != "+" and not isCity:
            state.append(char)
        else:
            isCity = False
    separator = ""
    print(f"{course[1]} in {separator.join(city)}, {separator.join(state)}")
    
def DateFormat(year, month, day):
    return str(year) + "-" + str(month) + "-" + str(day)

add18HoleScore()
