from datetime import datetime

name=input("enter name :")

#list of items
lists='''
rice    Rs 20/kg
sugar   Rs 20/kg
wheat   Rs 40/kg
soaps   Rs 50/each
oil     Rs 80/li
colgate Rs 60/each
maggie  Rs 20/pack
salt    Rs 10/kg
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalamount=0
ilist=[]
qlist=[]
plist=[]

items={'rice':20,'sugar':20,'wheat':40,'soaps':50,'oil':80,'colgate':60,'maggie':20,'salt':10}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp=int(input("if you want to buy items press 1 or press 2 for exit"))
    if inp==2:
        break
    if inp==1:
        item=input("enter your items:")
        quantity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry! you entered item is not available")
    else:
        print("OOPS! you entered wrong number")

    inp1=input("Can i bill the items yes or no")
    if inp1=='yes':
        pass
        if finalamount!=0:
            print(30*"*","Niharika SuperMart",30*"*")
            print(30*" ","Kalimandir")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(100*"-")
            print("SNo",8*" ","Items",5*" ","Quantity",3*" ","Price")
            for i in range(len(pricelist)):
                print(i,8*" ",ilist[i],10*" ",qlist[i],10*" ",plist[i])
            print(100*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount:",50*" ",'Rs',gst)
            print(100*"-")
            print(50*" ",'FinalAmount:','Rs',finalamount)
            print(100*"-")
            print(30*" ",'Thanks for Visiting',30*" ")
            print(100*"-")
            
            

    

