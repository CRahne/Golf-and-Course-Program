from csv import writer
from csv import reader
import numpy as np

def levenshtein_ratio(s, t):
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 2
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
    return Ratio


def addCourse():
    name = str(input("Name: "))
    city = str(input("City: "))
    state = str(input("State: "))
    Par = str(input("Par: "))
    Slope = str(input("Slope: "))
    Rating = str(input("Rating: "))
    addNewCourse(name, city, state, Par, Slope, Rating)
    
def addNewCourse(Name, City, State, Par, Slope, Rating):
    Location = CombineCityAndState(City, State)
    with open('GolfCourses.csv', 'a+', newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerow([GetNewCode(), Name, Location, Par,Slope,Rating])

# Need String Searching Algorithm
#def SearchCoursesByName(Name):
    
    
def SearchCoursesByLocation(City, State):
    TargetLocation = CombineCityAndState(City, State)
    with open('GolfCourses.csv','r',newline='') as file:
        csv_reader = reader(file, delimiter=',')
        MatchingCourses= []
        for course in csv_reader:
            if levenshtein_ratio(course[2], TargetLocation) > 0.4:
                MatchingCourses.append(course)
        return MatchingCourses
    
    
def SearchCoursesByName(Name):
    with open('GolfCourses.csv','r',newline='') as file:
        csv_reader = reader(file, delimiter=',')
        MatchingCourses= []
        for course in csv_reader:
            if levenshtein_ratio(course[1], Name) > 0.4:
                MatchingCourses.append(course)
        return MatchingCourses

def GetCourseWithCode(Code):
    with open('GolfCourses.csv','r',newline='') as file:
        csv_reader = reader(file, delimiter=',')
        MatchingCourse = []
        for course in csv_reader:
            if course[0] == Code:
                MatchingCourse = course
                break
        return MatchingCourse
    
def GetAllCourses():
     with open('GolfCourses.csv','r',newline='') as file:
        csv_reader = reader(file, delimiter=',')
        Courses = []
        for course in csv_reader:
            Courses.append(course)
        return Courses

def GetNewCode():
    data = GetAllCourses()
    code = list(data[-1][0])
    if int(code[3]) < 9:
        code[3] = str(int(code[3]) + 1)
    else:
        if int(code[2]) < 9:
            code[3] = "0"
            code[2] = str(int(code[2]) + 1)
        else:
            if int(code[1]) < 9:
                code[3] = "0"
                code[2] = "0"
                code[1] = str(int(code[1]) + 1)
            else:
                if int(code[0]) < 9:
                    code[3] = "0"
                    code[2] = "0"
                    code[1] = "0"
                    code[0] = str(int(code[0]) + 1)
    separater = ''
    return separater.join(code)

def CombineCityAndState(City, State):
    return (City + "+" + State)