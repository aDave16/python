stu={"ami@gmail.com":["Ami",20,120],
     "riya@gmail.com":["Riya",34,200]
     }
while True:
    print("1.Add student")
    print("2.Search student")
    print("3.Delete student")
    print("4.view all student")
    print("5.exit")

    ch=int(input("enter ur choice: "))
    match ch:
        case 1:
            email=input("enter email: ")
            name=input("enter name: ")
            age=int(input("enter age: "))
            marks=int(input("enter marks"))
            stu[email] = [name, age, marks]
            print("Student added successfully")
        case 2:
            search=input("enter email to search: ")
            for i,j in stu.items():
                if search in i:
                    for i1 in j:
                        print(i1)
                    break
            else:
                print("Student not found")
        case 3:
            search=input("enter email to delete: ")
            for i,j in stu.items():
                if search in i:
                    del stu[search]
                    print("Student Deleted successfully")
                    break
            else:
                print("Student not found")
        case 4:
            for i,j in stu.items():
                print(i,j)
        case 5:break
        case _:
            print("invalid choice")

