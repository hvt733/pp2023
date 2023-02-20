n = int(input("Number of Student: "))
student_name = []
student_id = []
student_dob = []
for i in range(n):
    k=input("ID of Student "+str(i + 1)+": ")
    student_id.append(k)
    k=input("Name of Student "+str(i + 1)+": ")
    student_name.append(k)
    k=input("Date of birth of Student "+str(i + 1)+": ")
    student_dob.append(k)

m = int(input("Number of Course: "))
course_id = []
course_name = []
for i in range(m):
    k=input("ID of Course "+str(i + 1)+": ")
    course_id.append(k)
    k=input("Name of Course: ")
    course_name.append(k)

diemso = []
for i in range(m):
    for j in range(n):
        k = float(input(course_name[i]+" score of "+student_name[j]+": "))
        diemso.append(k)

cnt=0

print("\n")
print("List of Student:")
for i in range(n):
    print(student_id[i],student_name[i],student_dob[i])

for i in range(m):
    print("\nID course:",course_id[i])
    print("Name course:",course_name[i])
    for j in range(n):
        print(student_id[j],student_name[j]+": ",diemso[cnt])
        cnt+=1
