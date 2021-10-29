print('enter 1 for rectangle, 2 for triangle, 3 for circle')
sign=int(input())
if sign==1:
    print('enter 2 sides')
    a=float(input())
    b=float(input())
    s=a*b
    print('area', s)
elif sign==2:
    print('input 3 sides of trial')
    a=float()
    b=float()
    c=float()
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print("area of trial", s)
elif sign==3:
    print('enter radius')
    R=float(input())
    S=3.14*R**2
    print("area of circus", S)
else:
    print('wrong entering')
