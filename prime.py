n=int(input())
count=0
sum_=2
a=[]
b=[]
for i in range(3,n+1):
       for j in range(2,i):  
           if (i % j == 0):  
               break  
       else:
            a.append(i)
for i in range(0,len(a)):
    sum_=sum_ + a[i]
    b.append(sum_)
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if(a[i]==b[j]):
            count+=1
print(count)
