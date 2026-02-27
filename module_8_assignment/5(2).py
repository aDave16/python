try:
    num=int(input("enter number: "))
    print(num/0)
    d={"age":20}
    print(d)
    print(d["name"])
except ZeroDivisionError:
    print("number canot be divided by 0")
except ValueError:
    print("pls enter valid number")
except KeyError:
    print("key not found")

finally:
    print("finally block will always exexcutes no matter error occurs or not")
