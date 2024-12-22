import re
import random 
random_functions=["x**3 + 2*x**2 - x + 5",
"4*x**4 - 3*x**3 + x - 7",
"x**5 - 2*x**3 + 3*x**2 - x + 1",
"2*x**6 - x**4 + 5*x - 10",
"-x**3 + 4*x**2 - 6*x + 9"]
def calc_deriative(function):
    function=function.replace(" ","")
    s=re.split(r"(?=[+-])", function)
    res=[]
    for i in s:
        if i.count("*")==2:
            check=None
            if i[0]=="-":
                i=i[1:]
                check=True
            if i[0]=="+":
                i=i[1:]
                check=False 
            mult=str(i[-1])
            i=mult + i[:-1] + str(int(i[-1])-1)
            if i[-1]=="1":
                i=i[:-3]
            if check==True:
                i="-"+i
            elif check==False:
                i="+"+i
            res.append(i)
        elif "*x**" in i:
            check=None
            mult=int(i[-1])
            if i[0]=="-":
                i=i[1:]
                check=True
            if i[0]=="+":
                i=i[1:]
                check=False
            i=str(int(i[0])*mult)  + i[1:-1] + str(int(i[-1]) - 1)
            if i[-1]=="1":
                i=i[:-3]
            if check:
                i="-"+i
            elif check==False:
                i="+"+i
            res.append(i)
        elif i.count("*")==1:
            if i[-1].isdigit():
                res.append(i[-1])
            elif i[1].isdigit():
                res.append(i[:2])
            elif i[0].isdigit():
                res.append(i[0])
        elif i=="x" or i=="-x" or i=="+x":
            check=None
            if i[0]=="-":
                res.append(-1)
            elif i[0]=="+":
                res.append(1)
            else:
                res.append(1)          
    return "".join(res)
def evaulate_slope(function,number):
    repla=function.replace("x",number)
    return eval(repla)
while True:
    function=input(f"Enter the function for instance({random.choice(random_functions)}): ")
    derivative=calc_deriative(function)
    print(f"The derivative of the function is: {derivative}")
    number=input("Enter the value of x: ")
    if number.isdigit():
        slope=evaulate_slope(derivative,number)
        print(f"The slope at x={number} is: {slope}")
    else:
        print("Invalid input. Please enter a valid number.")
    cont=input("Do you want to calculate again? (y/n): ")
    if cont.lower()!="y":
        break


            



