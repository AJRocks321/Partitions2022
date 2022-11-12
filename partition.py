n=int(input("Enter the number: "))
p=1#generator for +ve integers
q=3#generator for odd integers
temp=1
array=[1]  
switch=0

#map array [1, 2, 5, 7, 12, 15, 22,....] this array is used on main parray to find p(n), it tells which number to add and subtract from last.
while temp<n:
    if switch%2==0:
        temp+=p
        array.append(temp)
        p+=1
        switch+=1
    else:
        temp+=q
        array.append(temp)
        q+=2
        switch+=1
parray=[1,1]

#function nextnum calculates P(a) with input A as array [p(0),p(1),p(2),p(3),...,p(a-1)] and map array
#alternate sign pattern > using mod4 switch2> + + - - + + - - 
def nextnum(A,map):
    t=0
    switch2=1
    temp=0
    while map[t]<=len(A):
        sign=1
        if switch2%4==3 or switch2%4==0:
            sign=-1
        temp+=sign*A[-map[t]]
        t+=1
        switch2+=1
    return temp

#loop for finding next P in array until P(n) is found
for i in range(2,n+1):
    parray.append(nextnum(parray,array))
print("P(",n,") =",parray[-1])