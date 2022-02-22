Year= int(input ('Enter year: '))

if Year%4!=0:
    print ('This is not a leap year')
elif Year%100==0 and Year%400!=0:
    print('This is not a leap')
else:
    print('This is a leap year')