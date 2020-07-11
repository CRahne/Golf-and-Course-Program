from csv import writer
from csv import reader

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
            if course[2] == TargetLocation:
                MatchingCourses.append(course)
        return MatchingCourses
    
    
def SearchCoursesByName(Name):
    with open('GolfCourses.csv','r',newline='') as file:
        csv_reader = reader(file, delimiter=',')
        MatchingCourse = []
        for course in csv_reader:
            if course[1] == Name:
                MatchingCourse = course
                break
        return MatchingCourse

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