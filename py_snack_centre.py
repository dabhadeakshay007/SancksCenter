import random
import datetime

print("** Sai Sancks Center **")
print("Sr No   Food Item        Rate")
print("1         Pohe         Rs.15/plate")
print("2         Shira        Rs.20/plate")
print("3         Tea          Rs.10/cup")
print("4         Coffee       Rs.25/cup")
name = str(input("\nEnter Customer Name : ")) 
snack = ['Pohe','Shira','Tea','Coffee']
price = [15, 20, 10, 25]
pt = st = tt = ct = 0
order = []
ch = "yes"
while(ch=="yes"):
    item = int(input("Enter Food Item Code : "))
    qt = int(input("Enter Quantity : "))
    if item not in (1,2,3,4):
        print("Enter Correct Choice.")
    else:
        if item == 1:
            pt = 15 * qt
            order.append(f"    Pohe          15      {qt}          {pt}")
        elif item == 2:
            st = 20 * qt
            order.append(f"    Shira         20      {qt}          {st}")
        elif item == 3:
            tt = 10 * qt
            order.append(f"    Tea           10      {qt}          {tt}")
        elif item == 4:
            ct = 25 * qt
            order.append(f"    Coffee        25      {qt}          {ct}")
        else:
            print("Wrong Choice")
    ch = str(input("\nDo you want to add more food items in this order? (yes/no) : "))
    
sum = pt + ct + st + tt
print("\n******* Your Bill ***********")
print(f"\nCustome Name : {name}") 
print(f"Bill Number : {random.randint(201, 250)}") 
current_time = datetime.datetime.now()
print (f"Date Time : {current_time}")
print("Sr No    Food Item     Rate   Quantity    Total")

for i in range(len(order)):
    print(f"{i+1}    "+order[i])

print("-----------------------------------------------")                                    
print(f"                       Grand Total      Rs.{sum}\n")

print(f"Your Total Bill is Rs {sum}/- only.\n")
print("Thanks for visting!!!!! Come Again!!!!!!")

print("*********************")