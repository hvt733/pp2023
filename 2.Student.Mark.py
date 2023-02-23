# This class displays information about Person 
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
	def output(self):
		return self.id, self.name, self.dob

# This class displays information about Course 
class Course:
	def __init__(self, course_id, course_name):
		self.id = course_id
		self.name = course_name
	def output(self):
		return self.id, self.name

# Input Number, ID, Name, Dob of Student
n = int(input("Number of Student: "))
for i in range(0,n):
	x = input("ID of Student " + str(i+1) +": " )
	y = input("Name of Student " + str(i+1) +": " )
	z = input("Day of Birth of Student " + str(i+1) +": " )
	# Display all attribute of Student
	k = Student(x,y,z)	

# Input Number, ID, Name of Course
m = int(input("Number of Course"))
for i in range(0,n):
	a = input("ID of Course " + str(i+1) +": " )
	b = input("Name of Course " + str(i+1) +": " )
	# Display all attribute of Course
	c = Course(a,b)