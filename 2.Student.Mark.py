class Person:
	def __init__(self, person_name, person_dob):
		self.name =  person_name
		self.dob = person_dob

# This class displays information about Student and use inheritance of class Person
class Student(Person):
	def __init__(self, person_id, person_name, person_dob):
		# Using polymorphism
		super().__init__(person_name, person_dob)
		self.id = person_id
	

# This class displays information about Course 
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
		studentNum = int(input("Enter studentNumber: "))
		for i in range(studentNum):
			id = input("Student ID: ")
			name = input("Student Name: ")
			dob = input("Student Dob: ")
			self.student[id] = Student(id, name, dob)

	def addCourse(self):
		courseNum = int(input("Enter courseNumber: "))
		for i in range (courseNum):
			id = input("Course ID: ")
			name = input("Course Name: ")
			self.course[id] = Course(id, name)

	def addMark(self):
		courseID = input("Enter the Course ID: ")
		if courseID not in self.course:
			print("No such course found!")
			return

		for studentID in self.student:
			mark = float(input("Mark: "))
			if studentID not in self.mark:
				self.mark[studentID] = {}
			self.mark[studentID][courseID] = mark

		# Print the marks for each student
		for studentID in self.mark:
			mark = self.mark[studentID].get(courseID)
			studentName = self.student[studentID].name
			print(f"Mark of {studentName}: {mark}")






		def outputStudent(self):
			for id in self.student:
				print(f"{id} :  {self.student[id]['name']['dob']}")
		def outputMark(self):
			for id in self.course:
				print(f"{id} : {self.course[id]['name']}")
				
	def outputMark(self):
		for studentID in self.mark:
			for courseID in self.mark[studentID]:
				mark = self.mark[studentID][courseID]
				studentName = self.student[studentID].name
				print(f"Student ID: {studentID}, Student Name: {studentName}, Course ID: {courseID}, Mark: {mark}")


yooo = Major()
yooo.addStudent()
yooo.addCourse()
yooo.addMark()
yooo.outputMark()




# {"BI12-406": (id, name, dob)
#  {"BI12-407": {courseID: {5}}

# # Input Number, ID, Name, Dob of Student
# n = int(input("Number of Student: "))
# for i in range(0,n):
# 	x = input("ID of Student " + str(i+1) +": " )
# 	y = input("Name of Student " + str(i+1) +": " )
# 	z = input("Day of Birth of Student " + str(i+1) +": " )
# 	# Display all attribute of Student
# 	k = Student(x,y,z)	


# # Input Number, ID, Name of Course
# m = int(input("Number of Course"))
# for i in range(0,n):
# 	a = input("ID of Course " + str(i+1) +": " )
# 	b = input("Name of Course " + str(i+1) +": " )
# 	# Display all attribute of Course
# 	c = Course(a,b)
