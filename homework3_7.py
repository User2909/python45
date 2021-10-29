print('you first pay:')
a=float(input())
print('how many years in count:')
years=int(input())
for x in range(years):
    a=a+a*0.1
print('reasult', a)
