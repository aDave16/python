'''23. ""Student Result System:"" Dictionary with student names as keys and marks as values. Write functions to:
* Find topper * Calculate average marks * List students who failed (marks < 40)'''
stu={"ami":56,"riya":67,"sneha":34,"disha":70}
def topper():
        top=max(stu,key=stu.get)
        print(top,stu[top])

def avg_marks():
        total=sum(stu.values())
        avg=total/len(stu)
        return avg

def failed():
    f=0
    for i,j in stu.items():
        if j<40:
            f=1
            print(i,j)
    if f==0:
        print("no fail students")


while True:
    print("1.find topper")
    print("2.average marks")
    print("3.failed students")
    print("4.exit")
    ch=int(input("enter ur choice: "))
    
    match ch:
        case 1:
            topper()
        case 2:
            ans=avg_marks()
            print(ans)
        case 3:
            failed()
        case 4:break
        case _:
            print("invalid choice")