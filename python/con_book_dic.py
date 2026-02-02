#21. ""Contact Book:"" Store names as keys and phone numbers as values.
 #Add functions to: add, search, update, and delete contacts.
con_book={"Ami":4545,"neha":65675}

def add(name,num):
    con_book[name]=num
    print("contact added succesfully")
    print(con_book)

def search(name):
        if name in con_book:
             print(con_book[name])
        else:
             print("not found")
             
def updt(name,num):
    if name in con_book:
          con_book[name]=num#updates key's value if exist
          print("contact updated successfully")
          print(con_book)
    else:
        print("contact not found")
    
def delete(name):
    if name in con_book:
          del con_book[name]
          print("contact deleted successfully")
          print(con_book)
    else:
         print("not deleted")
        
while True:
    print("1.add contact")
    print("2.search contact")
    print("3.update contact")
    print("4.delete contact")
    print("5.exit")
    ch=int(input("enter ur choice: "))
    
    match ch:
        case 1:
            name=input("enter name: ")
            num=int(input("enter number: "))
            add(name,num)
        case 2:
            name=input("enter name: ")
            search(name)
        case 3:
            name=input("enter name: ")
            num=int(input("enter number: "))
            updt(name,num)
        case 4:
            name=input("enter name: ")
            delete(name)
        case 5:break
        case _:
              print("invalid choice")    