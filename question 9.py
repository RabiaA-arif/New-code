list_of_student={"rabia":"A Grade","farha":"A Grade","Arsalan":"B Grade","Haseeb":"B Grade","Muzammil":"A","tooba":"C Grade"}
print(list_of_student)
student_name=input("enter the name of :")
if student_name in list_of_student:
    print(list_of_student[student_name])
else:
    print("student is not found in list")