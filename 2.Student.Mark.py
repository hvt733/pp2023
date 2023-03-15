#Data
class Person:
    def __init__(self, person_name, person_dob):
        self.name = person_name
        self.dob = person_dob

class Student(Person):
    def __init__(self, person_id ,person_name, person_dob):
        super().__init__(person_name, person_dob)
        self.id = person_id

class Course:
	def __init__(self, course_id, course_name):
		self.id = course_id
		self.name = course_name

class Major:
    def __init__(self):
        self.student = {}
        self.course = {}
        self.mark = {}
    def addStudent(self):
        numStu = 0
        while True:
            try:
                numStu = int(input("Enter Number of Students: "))
                if numStu <= 0:
                    print("Please input a positive integer.")
                else:
                    break
            except ValueError:
                print("Please input a number.")

        for i in range(numStu):
            id = input("ID of Student " + str(i+1) + ": ")
            name = input("Name of Student " + str(i+1) +": ")
            dob = input("Date of Birth of Student "+ str(i+1) + ": ")
            self.student[id] = Student(id, name, dob)

        
    def addCourse(self):
        numCour = 0
        while True:
            try:
                numCour = int(input("Enter Number of Courses: "))
                if numCour <= 0:
                    print("Please input a positive integer.")
                else:
                    break
            except ValueError:
                print("Please input a number.")
        for i in range(numCour):
            id = input("ID of Course " + str(i+1) + ": ")
            name = input("Name of Course " + str(i+1) + ": ")
            self.course[id] = Course(id, name)

    def addMark(self):
        for studentID in self.student:
            for courseID in self.course:
                mark = float(input("Mark of Student " + self.student[studentID].name + " in Course "+ self.course[courseID].name + ": "))
                if studentID not in self.mark:
                    self.mark[studentID] = {}
                if courseID not in self.mark[studentID]:
                    self.mark[studentID][courseID] = {}
                self.mark[studentID][courseID] = mark
		
    def outputMark(self):
        for studentID in self.mark:
            for courseID in self.mark[studentID]:
                mark = self.mark[studentID][courseID]
                studentName = self.student[studentID].name
                print(f"Student ID: {studentID}, Student Name: {studentName}, Course ID: {courseID}, Mark: {mark}")



yoo = Major()
yoo.addStudent()
yoo.addCourse()
yoo.addMark()
yoo.outputMark()





