l=[1,2,3,4,5]

sum = 0
for i in l:
    sum=sum+i
print(sum)

product = 1
for i in l:
    product=product*i
print(product)

"""According to Big Oh notation, Time Complexity is 1(linear)."""

l=[1,2,3,4,5]

for i in l:
    for j in l:
        print("({},{}).format(i,j)")

"""According to Big Oh notation, Time Complexity is 2(quadratic)."""

def int_TO_str(i):
    digits = "0123456789"
    if i == 0:
        return "0"
    result=""
    while i > 0:
        result = digits[i%10] + result
        i=i//10
    return result

"""If we check this program in detail, we can see that the values are getting divided and getting smaller, therefore the Time complexity is log."""


a=[1,2,3,4]
b=[2,3,4,5,6]

for i in a:
    for j in b:
        if i<j:
            print({},{}.format(i,j))

"""According to Big Oh notation, Time Complexity is 2(quadratic)O(ab)."""

a=[1,2,3,4]
b=[2,3,4,5,6]

for i in a:
    for j in b:
        for k in range(100000):
            print({},{}.format(i,j))

"""According to Big Oh notation, Time Complexity is 2(quadratic):last loop is constant"""

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

"""If we use graph, Time Complexity is 1(linear)."""

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(5))

"""If we check the input AND function calls we will see that function calls are way grater than the input, Time Complexity is <2n (exponential.)"""

def mod(a,b):
    if b<=0:
        return -1
    div =a//b
    return a-div*b

print(mod(5,2))

"""No loop No recursion, only arithmatic operation therefore it is constant in time complexity."""
