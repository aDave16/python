#22. ""Inventory System:"" Create a dictionary of products with quantities. Write functions to:
#* Add stock* Remove stock* Check availability
product={"pen":45,"notebook":50}
def add(item,q):
    product[item]=q
    print("item added succesfully")
    print(product)

def rmv(item):
    del product[item]
    print("item removed succesfully")
    print(product)

def check():
    for k,v in product.items():
        print(k, v) 

while True:
    print("1.add stock")
    print("2.remove stock")
    print("3.check availability")
    print("4.exit")
    ch=int(input("enter ur choice: "))
    
    match ch:
        case 1:
            item=input("enter item: ")
            q=int(input("enter quantity: "))
            add(item,q)
        case 2:
            item=input("enter item: ")
            rmv(item)
        case 3:
            check()
        case 4:break
        case _:
            print("invalid choice")