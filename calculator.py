name=input("enter your name")
print("my name is",name)
children=input("enter the number of children")
children=int(children)
print("number of children")
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
net_income=salary-tax
if children>3:
    net_income=net_income-1000*children
else:
    net_income=net_income 
if net_income<0:
    print("invalid income")
else:
    net_income=net_income 
    print("my net_income is {net_income}")  

print(f"my name is {name},my salary is {salary},tax {tax},net_income {net_income}")
print(f"happy coding with juuma😃✨")





