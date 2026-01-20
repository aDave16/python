#Write a program to check if a given string is a valid phone number (e.g., str_phone: (123) 456-7890 output True)
str="1332wd3333"
if str.isdigit() and len(str)<=10:
    print("True")
else:
    print("False")