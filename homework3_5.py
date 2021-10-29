print('enter number of 3 signs')
num=int(input())
if num<1000:
    razr1=num//100
    razr2=(num%100)//10
    razr3=(num%100)%10
    print(razr1)
    print(razr2)
    print(razr3)
    sum=razr1+razr2+razr3
    print('sum is ', sum )
    
else:
    s=0
    while num>0:
        ost=num%10
        
        s=s+ost
        num=num//10
        
        
    print('sum is', s)