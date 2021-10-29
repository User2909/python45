print('enter digit one, from 3 before 23')
no1=input()
print('enter digit two')
no2=input()
print('enter sign    +, -, *, / ')
sign=input()
if no1.isdigit() and no2.isdigit():
    if ( float(no1) >= 3 and float(no1) <= 23) and (float(no2) >= 3 and float(no2) <= 23):
        if sign=='+':
            print(float(no1)+float(no2))
        elif sign=="-":
            print(float(no1)-float(no2))
        elif sign=="*":
            print(float(no1)*float(no2))
        elif sign=="/":
            print(float(no1)/float(no2))
        else:
            print('wrong sign')
    else:
        print('wrong entering')
        pass
else:
    print('it is not a number')
    pass

