balance =1000

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{1000}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrawn ₹{400}")
    else:
        print("Insufficient Balance!")

def check_balance():
    print(f"Current Balance: ₹{balance}")

#
def update(n):
    print("Before-Inside of the function:",n)
    n=n+10
    print("After-Inside of the function:",n)

n=10
update(n)  
print("outside of the function:",n) 



#Before-Inside of the function: 10
#After-Inside of the function: 20
#outside of the function: 10



def update(n):
    print("Before-Inside of the function:",n)
    n=(3,4)
    print("After-Inside of the function:",n)

n=(1,2,3)
update(n)  
print("outside of the function:",n)

#Before-Inside of the function: (1, 2, 3)
#After-Inside of the function: (3, 4)
#outside of the function: (1, 2, 3)


def update(n):
    print("Before-Inside of the function:",n)
    n=False
    print("After-Inside of the function:",n)

n=True
update(n)  
print("outside of the function:",n)


#Before-Inside of the function: True
#After-Inside of the function: False
#outside of the function: True



def update(n):
    print("Before-Inside of the function:",n)
    n=n.copy()
    n.append(20)
    print("After-Inside of the function:",n)

n=[1,2,3]
update(n)  
print("outside of the function:",n)



#Before-Inside of the function: [1, 2, 3]
#After-Inside of the function: [1, 2, 3, 20]
#outside of the function: [1, 2, 3]



def factorial(n):

    if n==1:
        return 1

    return n* factorial(n-1)

n=int(input("Enter the value:"))
print(factorial(n))


#Enter the value:5
#120


def shoot(n):
    if n==1:
        return 1
    print("Before recursion:",n)

    shoot(n-1)
    print("After recursion:",n)



n=int(input("Enter the value:"))
shoot(n)





shoot(1)
shoot(2)
shoot(3)
shoot(4)
shoot(5)
stack







n=int(input("Enter the num:"))

sum=0

for i in n:
    sum+=int(i)

'''while n>0:
    sum=sum+ (n%10)
    n=n//10
    '''
print(sum)




#Enter the value:3
#6



n=int(input("Enter the num:"))
a=0
b=1
if n==1:
    print(a)

  
elif n > 2:
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c




def evenorodd(n):
    if n%2==0:
        return"Even"
    else:
        return"odd"
    
n=int(input())
print(evenoroddd(n))



def div(a,b):
    return a/b

a=int(input())
b=int(input())
print(div(a,b))

a=20
divl= lambda a,b=3:a/b
print(divl(a))

def squares(l):
    for i in range(len(1)):
        l [i]=l[i]**2
    return l

l=[1,2,3,4,5]
print(squares(l))
squ=list(map(lambda i: i**2,l))