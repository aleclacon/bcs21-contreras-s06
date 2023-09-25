# num=[]
master=[]
baryabolP=0
baryabolF=0
#choice=("yes","no")
#def 
while True:
    x=input("Input student name: ")
    q1=int(input("Q1: "))
    q2=int(input("Q2: "))
    q3=int(input("Q3: "))
    cp=int(input("Class Participation: "))
    fe=int(input("Final Exam: "))
    grade = (q1+q2+q3)/3
    cg=(grade*0.4)+(cp*0.1)+(fe*0.5)
    if cg > 75 :
        equi = "Passed"
        baryabolP+=1
        
    elif cg < 75: 
        equi = "Failed" 
        baryabolF+=1  
        
    student=[x,q1,q2,q3,cp,fe,cg,equi]
    master.append(student)

    choice=input("Do you want to add another student? (Yes/No): ")
    if choice.lower()=="no":
        print("\nPLEASE READ : You are done grading")
        break   
    
print("GRADING BOOK")
print("\n\n==============================================")
print("Name | Q1 |t Q2 | Q3 | Class Participation | Final Exam | Grade | Equivalent")
for student in master:
    print(f"|{student[0]:^6} | {student[1]:^3} | {student[2]:^3} | {student[3]:^3} | {student[4]:^3} | {student[5]:^3} | {student[6]:^3} | {student[7]:^3} |")
  
print("==============================================")
print("\n")
print(f"Total number of Students PASSED : {baryabolP} ")
print(f"Total number of Students FAILED : {baryabolF}")
print("Made by : CONTRERAS, Aleianna Clarisse C. ")
# choice = input("Do you want to add students? : ")
# if choice.lower() == "yes":
#     while choice.lower == "yes":
#         x=input("Input student name: ")
#         q1=int(input("Q1: "))
#         q2=int(input("Q2: "))
#         q3=int(input("Q3: "))
#         q4=int(input("Q4: "))
#         fe=int(input("Final Exam: "))
#         student=[x,q1,q2,q3,q4,fe]
#         print(f"|{student}",end="")
        
# elif choice.lower=="no":
#     print("Please add students")

        #for choice in
    # rows=int(input("Number of rows: "))
        # columns=int(input("Number of students: "))
# for i in range(R):          # A for loop for row entries
#     a =[]
#     for j in range(C):      # A for loop for column entries
#          a.append(int(input()))
#     matrix.append(a)













#x=input("Input student name")