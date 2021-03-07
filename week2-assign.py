print("Q1.")

def calculate(min,max):
    sum=0
    for n in range(min,max+1):
        sum = sum + n
    print(sum)

calculate(1,3)
calculate(4,8)

print("=============")
print("Q2.")

def avg(data):
    count=data["count"]
    employees=data["employees"]
    num=[]
    for employee in employees:
        salary=employee["salary"]
        floatSalary=float(salary)
        num.append(floatSalary)
    result=sum(num)/count
    print(result) 

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000  
        },
        {
            "name":"Jenny",
            "salary":50000  
        }
    ]
})

print("=============")
print("Q3.")

def maxProduct(nums):
    num=sorted(nums,reverse=True)
    if num[-1]<0 and num[-2]<0 and num[-1]*num[-2] > num[0]*num[1]:
        print(num[-1]*num[-2])
    else:
        print(num[0]*num[1])

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])

print("=============")
print("Q4.")

def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]


result=twoSum([2,11,7,15],9)
print(result)
