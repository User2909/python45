print('enter two something ')
no1=input()
no2=input()

if no1.isdigit() and no2.isdigit():
    if (float(no1) >= 3 and float(no1) <= 21) and (float(no2) >= 3 and float(no2) <= 21):
        print(abs(float(no1)-float(no2)))
    else:
        print(no1+no2)
else:
    print(no1+no2)