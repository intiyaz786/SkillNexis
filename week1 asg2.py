"""
Student Grade Calculator:
Take marks as input, calculate average & assign grades.
"""
def student_grade():
    mar1=float(input("Enter the marks for Subject1: "))
    mar2=float(input("Enter the marks for Subject2: "))
    mar3=float(input("Enter the marks for Subject3: "))
    mar4=float(input("Enter the marks for Subject4: "))
    mar5=float(input("Enter the marks for Subject5: "))
    average=(mar1+mar2+mar3+mar4+mar5)/5
    if(average>=90):
        grade='S'
    elif(average>=80):
        grade='A'
    elif(average>=70):
        grade='B'
    elif(average>=60):
        grade='C'
    elif(average>=50):
        grade="D"
    elif(average>=40):
        grade="E"
    else:
        grade="F"
    
    print("Average Marks: ",average)
    print("Grade: ",grade)

student_grade()