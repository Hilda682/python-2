name=input("enter your name")
print("my name is",name)
salary=input("enter amount")
salary=int(salary)
print("my salary is",salary )






if salary <0:
    print("invalid entry")

elif salary > 10000 and salary <= 200000:
    tax =0.3*salary
    print(" your tax rate is :",tax)
elif salary >20000 and salary <=50000:
    tax =0.5*salary
    print(" your tax rate is :",tax)
elif salary > 50000:
    tax=0.6*salary
    print(" your tax rate is :",tax)



