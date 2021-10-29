print('input 2 numbers and we search')
a=int(input())
b=int(input())
res=0
while a!=b:
    if a > b:
        res=a-b
        a=res
    else:
        res=b-a
        b=res
print('your nod is', a)
    