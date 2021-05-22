# simple student management system with Dictionaries 
# memory is volatile, only for input and output.

Name = []
Class=[]
Grno=[]
phone_number = []
fathers_name = []
mothers_name = []
Blood_group = []
parents_number = []

Student_Dict={"Student Name": Name, "Class":Class, "Grno":Grno, "Phonenumber":phone_number, "fathersname":fathers_name,
"mothersname":mothers_name,"Bloodgroup":Blood_group,"parentsnumber":parents_number}
print("********Student Management System*********")

while True:
    print(" 1- Add Student Details")
    print(" 2- Show Student Details")
    print(" 3- Search Student Details")
    print(" 4- Sort Student Details")
    print(" 5- Update Student Details")
    print(" 6- Remove Student Detail")
    print(" 7- Clear Student Details")
    print(" 8- Exit")
    print()
    choice=int(input("Select from 1-8 : "))
    
    if choice==1:
        print()
        print("********Add Student *********")
        name=input("Enter Name of the Student :")
        clas=input("Enter Class of the Student : ")
        grno=input("Enter GR No of the Student : ")
        phoneno = input("Enter students phone no:")
        fathersname = input("Enter student's fathers name:")
        mothersname = input("Enter students mothers name:")
        bloodgrp = input("Enter students blood group:")
        parentsnumber = input("Enter students parents number:")
        
        Name.append(name)
        Class.append(clas)
        Grno.append(grno)
        phone_number.append(phoneno)
        fathers_name.append(fathersname)
        mothers_name.append(mothersname)
        Blood_group.append(bloodgrp)
        parents_number.append(parentsnumber)

        print("Record Added Successfully")
        print("----------------")
        
    
    elif choice==2:
        print()
        print("********Show Student Details*********")
        na=Student_Dict['Student Name']
        cl=Student_Dict['Class']
        gr=Student_Dict['Grno']
        pn=Student_Dict['Phonenumber']
        fn=Student_Dict['fathersname']
        mn=Student_Dict['mothersname']
        bg=Student_Dict['Bloodgroup']
        pan=Student_Dict['parentsnumber']

        print("-----------------")
        for i in Student_Dict:
            print(i, ":", Student_Dict[i])
        print("-----------------")
    
    elif choice==3:
        print()
        print("********Search Student Details*********")
        detail=input("Enter detail to Search")
        if detail in Student_Dict:
            print("Record Found")
        else:
            print("Record Found")
        print("-----------------")
        
    elif choice==4:
        print()
        print("********Sort Student Details*********")
        Name.sort()
        Class.sort()
        Grno.sort()
        phone_number.sort()
        fathers_name.sort()
        mothers_name.sort()
        Blood_group.sort()
        parents_number.sort()

        print("-----------------")
        for i in Student_Dict:
            print(i, ":", Student_Dict[i])
        print("-----------------")
        
    elif choice==5:
        print()
        print("********Update Student Details*********") 
        ch=input("Enter detail to be Updated : ")
        update=input("Enter a New Name : ")
        print()
        if ch in Name:
            s=Name.index(ch)
            n=Name[s]
            Name[s]=update
        if ch in Class:
            s=Class.index(ch)
            n=Class[s]
            Class[s]=update
        if ch in Grno:
            s=Grno.index(ch)
            n=Grno[s]
            Grno[s]=update
        if ch in phone_number:
            s=phone_number.index(ch)
            n=phone_number[s]
            phone_number[s]=update
        if ch in fathers_name:
            s=fathers_name.index(ch)
            n=fathers_name[s]
            fathers_name[s]=update 
        if ch in mothers_name:
            s=mothers_name.index(ch)
            n=mothers_name[s]
            mothers_name[s]=update       
        if ch in Blood_group:
            s=Blood_group.index(ch)
            n=Blood_group[s]
            Blood_group[s]=update
        if ch in parents_number:
            s=parents_number.index(ch)
            n=parents_number[s]
            parents_number[s]=update
        
            print("-----------------")
        for i in Student_Dict:
            print(i, ":", Student_Dict[i])
        print("-----------------")
    
    elif choice==6:
        print()
        print("********Remove a Student*********") 
        ch=input("Enter a detail to Remove from the List : ")
        if ch in Name:
            Name.remove(ch)
        if ch in Class:
            Class.remove(ch)
        if ch in Grno:
            Grno.remove(ch)
        if ch in phone_number:
            phone_number.remove(ch)
        if ch in fathers_name:
            fathers_name.remove(ch)
        if ch in mothers_name:
            mothers_name.remove(ch)
        if ch in Blood_group:
            Blood_group.remove(ch)
        if ch in parents_number:
            parents_number.remove(ch)

            print("-----------------")
        for i in Student_Dict:
            print(i, ":", Student_Dict[i])
        print("-----------------")
        
    elif choice==7:
        print()
        print("********ClearStudent List*********") 
        Name.clear()
        Class.clear()
        Grno.clear()
        phone_number.clear()
        fathers_name.clear()
        mothers_name.clear()
        Blood_group.clear()
        parents_number.clear()
        
        print("-----------------")
        for i in Student_Dict:
            print(i, ":", Student_Dict[i])
        print("-----------------")
        
    elif choice==8:
        exit()
