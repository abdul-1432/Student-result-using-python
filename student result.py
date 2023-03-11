# Program to generate student result

students = []
pass_count = 0
fail_count = 0

n = int(input("Enter How Many Students : "))
for i in range(n):
    marks = {}
    marks["rollno"] = input("Enter Roll Number : ")
    marks["name"] = input("Enter Student Name : ")
    marks["Tel"] = int(input("Enter Marks Obtained in Telugu : "))
    marks["Eng"] = int(input("Enter Marks Obtained in English : "))
    marks["Mat"] = int(input("Enter Marks Obtained in Mathematics : "))
    marks["Sci"] = int(input("Enter Marks Obtained in Science : "))
    marks["Soc"] = int(input("Enter Marks Obtained in Social : "))
    marks["tot"] = marks["Tel"] + marks["Eng"] + marks["Mat"] + marks["Sci"] + marks["Soc"]
    marks["avg"] = marks["tot"] / 5
    if marks["Tel"]>=35 and marks["Eng"]>=35 and marks["Mat"]>=35 and marks["Soc"]>=35 and marks["Sci"]>=35:
        marks["result"] = "Pass"
        pass_count += 1
    else:
        marks["result"] = "Fail"
        fail_count += 1
    students.append(marks)

print("Student Results : ")
print("-------------------------------------------------------------")
print("RollNo Name    Tel  Eng  Mat  Sci  Soc  Total Average  Result")
print("-------------------------------------------------------------")

for stud in students:
    print(" %s   %s   %3d  %3d  %3d  %3d  %3d  %3d  %5.2f    %s"%(stud["rollno"],stud["name"],stud["Tel"],stud["Eng"],stud["Mat"],stud["Sci"],stud["Soc"],stud["tot"],stud["avg"],stud["result"]))

print("-------------------------------------------------------------")
print("No. of Students Attended : ",n)
print("No. of Students Passed : ",pass_count)
print("No. of Students Failed : ",fail_count)
print("-------------------------------------------------------------")
